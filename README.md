# Default Value

Provides `Default` that allows differentiating a provided value from a default.

## Installation

```bash
pip install default-value
```

## Usage

### Aliases

This module uses `dataclasses.NoDefault` as a sentinel value for when no default is provided.
It re-exports it as `default_value.NoDefault` for convenience.

```python
from default_value import Opt, Req, Default, NoDefault

# The following aliases are provided by `default_value`
type Opt[T] = T | Default[T] | NoDefault
type Req[T] = T | Default[T]

# If you want to allow multiple types, such as `None`, then just include them in the union.

def foo(param: Opt[str | None] = Default(None)) -> None:
    print(f"`param` is {param}")
    # This will print "`param` is Default(None)" if no value is provided.
    # If the caller passes `None`, it will print "`param` is None".
    # This allows for easy differentiation between "no value provided" and
    # "value explicitly set to None".
    ...
```

### Classes



### No Default

```python
from default_value import Opt, NoDefault


```

### Optional Type

```python
from default_value import Opt, Default

# type Opt[T] = T | Default[T] | NoDefault

def foo(value: Opt[str] = Default) -> None:
    if value is Default:
        print("Value is default")
    elif value is None:
        print("Value is None")
    else:
        print(f"Value is set to {value}")
```

## Usage

### Optional Type

```python
from unset import Opt, Unset

# type Opt[T] = T | Unset | None

def foo(value: Opt[str] = Unset) -> None:
    if value is Unset:
        print("Value is unset")
    elif value is None:
        print("Value is None")
    else:
        print(f"Value is set to {value}")
```

### Maybe Unset

```python
from unset import MaybeUnset, Unset

# type Maybe[T] = T | Unset

# type MaybeUnset[T] = T | Unset

def foo(value: MaybeUnset[str] = Unset) -> None:
    if value is Unset:
        print("Value is unset")
    else:
        print(f"Value is set to {value}")
```

### Explicit Types

```python
from unset import Unset, UnsetType

def foo(value: str | UnsetType | None = Unset) -> None:
    if value is Unset:
        print("Value is unset")
    elif value is None:
        print("Value is None")
    else:
        print(f"Value is set to {value}")
```

## Documentation Links

- [Author]
- [Change Log]
- [Code of Conduct]
- [Contributing]
- [Security Policy]

[//]: # (Links)

[Author]: docs/AUTHORS.md
[Change Log]: docs/CHANGELOG.md
[Code of Conduct]: docs/CODE_OF_CONDUCT.md
[Contributing]: docs/CONTRIBUTING.md
[Security Policy]: docs/SECURITY.md
