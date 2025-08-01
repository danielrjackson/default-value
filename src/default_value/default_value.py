"""
Provides `Default` that allows differentiating a provided value from a default.

This is useful for functions that want to distinguish between an argument that was
explicitly passed as `None` and one that was not provided at all.

Example:
-------
```python
def foo(bar: Default[int] = Default(42)):
    if bar.is_provided:
        print(f"Bar was provided with value: {bar.value}")
    else:
        print(f"Bar was not provided, using default: {bar.value}")

foo()          # Bar was not provided, using default: 42
foo(100)       # Bar was provided with value: 100
foo(None)      # Bar was provided with value: None
```
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import NoDefault
from pathlib import Path
from typing import Final, overload

from annotated_types import Annotated
from pydantic import Field

__all__ = [
    # Classes
    "Default",
    "NoDefault",
    # Type Aliases
    "Opt",
    "Req",
    # Helper Functions
    "default_factory",
    "require",
    "resolve",
]


class Default[T]:
    """
    Wrapper type to differentiate between a provided value and a default value.

    This class is useful for distinguishing between an argument that was explicitly passed
    (including None) and one that was not provided at all, allowing for more precise
    handling of default values in function signatures.
    """

    __slots__ = ("value",)

    def __init__(
        self,
        value: T | Annotated[T, Field],
    ) -> None:
        """
        Initialize the object with a given value.

        Args:
            value (T | Annotated[T, Field]): The value to be stored, which can be a type T or an
                annotated type T with a Field.

        Returns:
            None
        """
        self.value = value

    def __repr__(self) -> str:
        """Return a string representation of the Default instance."""
        return f"Default({self.value!r})"

    def __value__(self) -> T:
        """Return the value contained in this Default instance."""
        return self.value

    def is_valid(self) -> bool:
        if self.validators is None:
            return True
        if isinstance(self.validators, list):
            return all(validator(self.value) for validator in self.validators)
        return self.validators(self.value)


Unset: Final = sentinel.create(
    "Unset",
    mro=(_Default,),
    cls_dict={
        "__repr__": _Default.__repr__,
        "__bool__": _Default.__bool__,
    },
)
"""
Sentinel value to indicate that an argument was not provided.

This is used to differentiate between an argument that was explicitly set to `None`
and one that was not provided at all.

See Also
--------
`require`: Ensures that a value is provided and not `Unset`.
`resolve`: Returns a default value if the provided value is `Unset`.
"""


# -----------------------------------------------------------------------------
# Type Aliases
# -----------------------------------------------------------------------------
type Opt[T] = T | _Default
"""Optional type alias for a value that can be of type `T` or the sentinel `Unset`."""

type OptOrNone[T] = T | _Default | None
"""Optional type alias for a value that can be of type `T`, the sentinel `Unset`, or `None`."""

type Req[T] = T | _Default
"""
Required type alias for a value that must be of type `T`.

Allows for Unset to allow for checking if the value was provided,
but does not allow for `None` as a value.

This does not automatically check if the value is `Unset`. Use `require` to enforce that.

Note: This is technically equivalent to `Opt`, but is meant to indicate that the value is required.
"""

type ReqOrNone[T] = T | _Default | None
"""
Required type alias for a value that must be of type `T` or `None`.

Allows for Unset to allow for checking if the value was provided.

This does not automatically check if the value is `Unset`. Use `require` to enforce that.
This is useful for cases where the value can be `None` but you still want to check if it was
    provided.

Note: This is technically equivalent to `OptOrNone`, but is meant to indicate that the value is
    required.
"""

type OrNone[T] = T | None
"""Type alias for a value that can be of type `T` or `None`."""

# -----------------------------------------------------------------------------
# Convenient Type Shortcuts for Common Types
# -----------------------------------------------------------------------------
type OptStr = str | _Default
"""Optional string that can be unset."""

type OptInt = int | _Default
"""Optional integer that can be unset."""

type OptFloat = float | _Default
"""Optional float that can be unset."""

type OptPath = Path | _Default
"""Optional path that can be unset."""

type OptBool = bool | _Default
"""Optional boolean that can be unset."""

type ReqStr = str | _Default
"""Required string (use with `require()` to enforce)."""

type ReqInt = int | _Default
"""Required integer (use with `require()` to enforce)."""

type ReqFloat = float | _Default
"""Required float (use with `require()` to enforce)."""

type ReqPath = Path | _Default
"""Required path (use with `require()` to enforce)."""

type ReqBool = bool | _Default
"""Required boolean (use with `require()` to enforce)."""


# -----------------------------------------------------------------------------
# Methods
# -----------------------------------------------------------------------------
def require[T](
    value: T | _Default | None = Unset,
    name: str = "Argument",
    *,
    force_value: bool = False,
) -> T:
    """
    Return *value* or raise `TypeError` if it is `Unset`.

    This is useful when the caller does not necessarily need a default value,
    and you can derive the value in another way.
    That method would then call a method that uses `require` to ensure
    that the derivation succeeded if the value is not provided.

    Args:
        value: Value to check, which can be of type `T` or the sentinel `Unset`.
        name:  Name of the argument, used in the error message if it is `Unset`.
        force_value: If `True`, raises `TypeError` if the value is `None`.

    Returns:
        T: The value itself if it is not `Unset`.

    Raises:
        TypeError: If:
            -   The value is `Unset`, indicating that the argument is required.
            -   `force_value` is `True` and the value is `None`, indicating that the argument
                must not be `None`.

    """
    if value is Unset:
        raise TypeError(f"{name} is required")
    if force_value and value is None:
        raise TypeError(f"{name} must not be None")
    return value  # type: ignore[return-value]


# -----------------------------------------------------------------------------
# resolve
# -----------------------------------------------------------------------------
@overload
def resolve[T](
    value: T | _Default = Unset,
    /,
    *,
    default: T,
) -> T: ...


@overload
def resolve[T](
    value: T | _Default = Unset,
    /,
    *,
    factory: Callable[[], T],
) -> T: ...


def resolve[T](
    value: T | _Default = Unset,
    /,
    *,
    default: T | None = None,
    factory: Callable[[], T] | None = None,
) -> T:
    """
    Return `value` unless it is `Unset`.

    In that case, return either `default` or
    call `factory` with no arguments depending on which is specified.

    Args:
        value: Either a real value of type `T` or the sentinel `Unset`.
        default: Literal to use when the argument was omitted.
            Mutually exclusive with `factory`.
        factory: Callable to lazily create a default. Called with no arguments.

    Returns:
        The value itself if it is not `Unset`, otherwise the default value
        if specified, otherwise the object built by the factory.
    """
    if value is not Unset:
        return value  # type: ignore[return-value]  # explicit argument wins

    if (default is None) == (factory is None):  # XOR check
        raise TypeError("Either default= or factory= must be specified.")

    if default is not None:
        return default

    if factory is not None:
        return factory()

    # This should never be reached due to the XOR check above
    raise RuntimeError("Unreachable code")


# -----------------------------------------------------------------------------
# default_factory
# -----------------------------------------------------------------------------
def default_factory[**P, T](factory: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> T:
    """
    Call a factory function to create a default value.

    This function always calls the factory, even if the argument is not `Unset`.
    This is useful when you want to ensure a fresh instance is created every time.

    Parameters
    ----------
    factory : Callable[P, T]
        Function to call to create the default value.
    *args : P.args
        Positional arguments to pass to the factory.
    **kwargs : P.kwargs
        Keyword arguments to pass to the factory.

    Returns
    -------
    T
        The result of calling factory(*args, **kwargs).
    """
    return factory(*args, **kwargs)
