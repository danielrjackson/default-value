<!-- omit in toc -->
# Contributing

Contributions are welcome, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

- [Contribution Guidelines](#contribution-guidelines)
  - [Tasks](#tasks)
- [Unset Task List](#unset-task-list)
- [Instructions](#instructions)
- [General Notes](#general-notes)
- [Task List](#task-list)
  - [Testing](#testing)
  - [Lessons Learned](#lessons-learned)
  - [General Guidelines](#general-guidelines)
  - [Coding Standards](#coding-standards)
  - [Documentation](#documentation)
  - [Finishing Up Your Change](#finishing-up-your-change)
    - [Change Report Instructions](#change-report-instructions)
    - [Pull Request Guidelines](#pull-request-guidelines)
- [Human Contributions](#human-contributions)
  - [Report Bugs](#report-bugs)
  - [Fix Bugs](#fix-bugs)
  - [Implement Features](#implement-features)
  - [Submit Feedback](#submit-feedback)
- [AI Contributions](#ai-contributions)
- [See Also](#see-also)

## Contribution Guidelines

> [!CAUTION] Before You Start
>
> Please read these guidelines before contributing.
>
> These guidelines are designed to help you contribute effectively and efficiently.
>
> - Failure to do so may result in your contribution being rolled back or rejected.
> - You don't want to waste your time or ours.

> [!WARNING] Check the Lesson Learned Section
>
> The [Lessons Learned] section in this document has important information about the project that
> was learned the hard way. Read it so you don't make the same mistakes.

### Tasks

## Unset Task List

---------------------------------------------------------------------------------------------------

This document tracks the outstanding work for the Unset project.

## Instructions

1. Pick the next task and complete it.
2. If you discover new tasks that need to be completed while completing the task, add them to the
   list in the appropriate spot, respecting priority and prerequisites.
3. If a task isn't adequately explained or is missing an important detail, update it.
4. Don't forget to update the `/docs/notes` files with details about what was done, why it was done,
   and any relevant thoughts or lessons learned.
5. Add any general notes that will apply broadly to subsequent work in the `General Notes` section
   below.
6. Update these instructions if important missing instructions that should be here are discovered.

## General Notes

1. **Do not remove or drastically abbreviate documentation**: The documentation is important for
   understanding the code and should be kept up to date. If you find a file that needs better
   documentation, add it to the task list. Document strings for modules, classes, methods, members,
   etc. should not transition from detailed to extremely brief.
2. **Follow the established formatting**: The formatting in completed files should be used as an
   example of proper formatting that should be used throughout the project.
3. **Review recent notes before starting tasks**: The `/docs/notes` directory contains important
   notes about recent changes to the project. These notes provide context and reasoning for changes
   that have been made, which can help inform your work on tasks.
4. **Changes should be documented in the `/docs/changelog` folder**: Each change should have a
   corresponding file in this folder that describes the change, its rationale, and any relevant
   details. The file name should follow the format `YYYY-MM-DD-HH-MM.md`, and the content should
   follow the template provided in `/docs/changelog/README.md`.
5. **Review `/docs/notes/README.md`** before writing notes: This file describes how to write notes
   and what to include in them. It is important to follow these guidelines to ensure consistency
   and clarity in the notes.

## Task List

- **Create Tasks**: This is a brand new project, so the first task is to create tasks.

> [!IMPORTANT] Check the Task List or Issues
>
> Before starting work on a new feature or bug fix, check the task list or issues to see if it has
> already been reported or if someone else is already working on it.
>
> Select the first uncompleted task on the list and complete it.

> [!IMPORTANT] One Change at a Time
>
> Please submit one change per pull request. These can be found in [`TASKS.md`] or the issues
> tracker.

> [!WARNING] Add Tasks When Needed
>
> If you discover an issue or task or bug that needs to be addressed, please add it to the
> [`TASKS.md`] file or the issues tracker. Do not slip it into the feature or bug fix you are
> working on. This helps keep the project organized and makes it easier for others to contribute.
>
> It also makes rollbacks easier if something goes wrong, as the change is isolated to a single
> commit.

> [!IMPORTANT] Consider Requirements When Adding New Tasks
>
> When adding new tasks to the [`TASKS.md`] file or the issues tracker:
>
> - Check if any existing tasks either depend on the new task or are prerequisites for it.
>   - If so, be sure to link the tasks together appropriately.
> - This will help prioritizing the tasks and ensure that they are completed in the correct
>   order.

### Testing

> [!IMPORTANT] Create Tests
>
> If you are adding new functionality, please create tests for it.
> If you are fixing a bug, please create a test that reproduces the bug.
> This will help ensure that the bug is fixed and that it doesn't come back in the future.
> See the [Testing] section for more information on how to write tests.

> [!IMPORTANT] Write Tests First
>
> Write tests before you write the code.
> This helps ensure that the code is correct and that it works as intended.

> [!IMPORTANT] Write Tests that Cover important Code Paths and Edge Cases
>
> Make sure to write tests that are meaningful and comprehensive, not just little stubs.
>
> Think carefully about edge cases and how the code will be used. Try to poke at the code where it
> is most likely to break.

> [!CAUTION] Add Tests for New Features and Bug Fixes
>
> If you are adding new functionality, please create tests for it.
> If you are fixing a bug, please create a test that reproduces the bug.
>
> - This will help ensure that the bug is fixed and that it doesn't come back in the future.

To run the tests, use the following command:

```bash
pytest --cov=unset --cov-report=html
```

> [!TIP] Use the Coverage Report
>
> The coverage report will be generated in the `htmlcov` directory.
> You can open the `index.html` file in a web browser to view the coverage report.
> This report will show you which lines of code are covered by tests and which are not.

Alternatively, you can run the tests with the following command to see the coverage report in the
terminal (Especially useful for AI agents):

```bash
pytest --cov=unset --cov-report=term-missing
```

Make sure that the test co

### Lessons Learned

> [!IMPORTANT] Lessons Learned
>
> Add any lessons learned from the project here.
>
> This is for things that don't belong anywhere else in the instructions in this document.

### General Guidelines

> [!IMPORTANT] Use Existing Code
>
> If possible, use any existing code in the project to implement the feature.
> It's especially useful to check the libraries to see if they already have the functionality you
> need.

> [!IMPORTANT] Remember Security
>
> If you are making changes that affect security, please be sure to follow best practices.
> Double check that you are not introducing any security vulnerabilities.
>
> If you see any security vulnerabilities, be sure to add them to the [`TASKS.md`] file or the
> issues tracker as high priority issues.

### Coding Standards

- PEP8
- Functions over classes except in tests
- Use double quotes around strings that are used for interpolation or that are natural language
    messages
- Use single quotes for small symbol-like strings (but break the rules if the strings contain
    quotes)
- Use triple double quotes for docstrings and raw string literals for regular expressions even if
    they aren't needed.
- Example:

    ```python
    LIGHT_MESSAGES = {
        'English': "There are %(number_of_lights)s lights.",
        'Pirate': "Arr! Thar be %(number_of_lights)s lights."
    }
    def lights_message(language, number_of_lights):
        """Return a language-appropriate string reporting the light count."""
        return LIGHT_MESSAGES[language] % locals()
    def is_pirate(message):
        """Return True if the given message sounds piratical."""
        return re.search(r"(?i)(arr|avast|yo ho ho)!", message) is not None
    ```

> [!IMPORTANT] Specify Parameter Types
>
> When possible, specify the types of parameters in function signatures.
>
> - This helps with code readability and understanding how to use the function.
> - It also helps static analysis tools catch potential issues.
> - The IDE can also show the parameter types when hovering over the function.

> [!IMPORTANT] Follow the Code Style
>
> Please follow the code style of the project.
> This includes things like indentation, line length, and naming conventions.
>
> The line length used in this project is 99 characters.

> [!IMPORTANT] Prefer Dry Code
>
> Avoid duplicating code.
> If you find yourself copying and pasting code, consider refactoring it into a function or
> class.

> [!IMPORTANT] Use Meaningful Names
>
> Use meaningful names for variables, functions, and classes.
> This helps make the code more readable and understandable.
>
> - Avoid using single-letter variable names except for loop counters or classical variable names
>   like `i`, `j`, `k`, or `x`, `y`, `z`. If it fits a standard scientific or mathematical formula,
>   then it's okay. But add docstrings to explain what the variable is for in case someone else
>   isn't familiar with the formula.
> - Avoid using abbreviations or acronyms unless they are well-known and widely used.
> - Use descriptive names that convey the purpose of the variable, function, or class.
> - Use consistent naming conventions throughout the codebase.
> - When possible, use names that are self-explanatory and do not require additional comments to
>   understand.
> - Avoid generic names like `data`, `info`, or `temp` unless they are used in a very specific
>   context where their meaning is clear.
> - Consider the length of the name, balancing between being descriptive and concise.

> [!IMPORTANT] Raise Issues if Code Is Atypical
>
> If you see code that is atypical or does not follow widely accepted conventions, please raise an
> issue or comment. A good location for this is in `/docs/notes`.
>
> If a convention is common for a certain type of code, such as AI/ML code, then follow the widely
> accepted conventions for that type of code. Be sure to add documentation explaining what is going
> on and why it is done that way, especially for domain specific code.

### Documentation

> [!IMPORTANT] Include Documentation
>
> Documentation is important for understanding the code and how to use it.
>
> The important part of documentation is the ***WHY***, not the ***WHAT***.
>
> - The code itself is the ***WHAT***, and it should be clear from the code what it does.
> - We're looking for context so that we can understand why the code was written the way it was and
>   what purpose it serves.
>
> Add docstrings to functions, classes, modules, and even variables.
>
> - This helps others understand the code and how to use it.
> - It also helps because then the IDE can show the documentation when hovering over the code.

> [!IMPORTANT] Update Documentation
>
> If documentation is out of date, please update it. Incorrect documentation is worse than no
> documentation at all.

> [!WARNING] Avoid Removing Documentation
>
> Avoid removing or drastically abbreviating documentation.
>
> Unless there is a compelling reason to do so, the documentation was probably put there for a
> reason.

### Finishing Up Your Change

> [!IMPORTANT] Check Diffs Before Committing
>
> Before committing your changes, check the diffs to ensure that you are only committing the
> changes you intended to make.
>
> - Look for any unintended or unnecessary changes that may have been made.
> - Check for code that may have been accidentally modified or removed.

> [!IMPORTANT] Use Meaningful Commit Messages
>
> Commit messages should be clear and concise, explaining what the change does and why it was made.
>
> - The reasoning behind the change should be in the body of the commit message.
>   - Without it, it requires much more effort to understand the change.
> - The subject line should be a brief summary of the change.
>   - It should be no more than 50 characters long.
> - The body of the commit message should explain the change in more detail.
>   - It should be wrapped at 72 characters.
> - Include a link to the issue or task that the change addresses.
>   - If one does not exist, create one in the [`TASKS.md`] file or the issues tracker.
>   - This allows others to see an overview of the changes that have been made without having to
>       read through the entire commit history.

#### Change Report Instructions

Record your contributions in the `/docs/changelog` folder.

Use the [template] at `/docs/templates/changelog/CHANGELOG_ENTRY_TEMPLATE.md` to create a new change report.

For an [example] report, see `/docs/changelog/main_1-0-0_20250801T095500Z.md`.

Filenames must follow `main_<version_slug>_<datetime_slug>.md` (e.g., `main_1-0-0_20250801T095500Z.md`).

#### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. The pull request should be contained:
   - If it's too big consider splitting it into smaller pull requests.
3. If the pull request adds functionality, the docs should be updated.
   - Put your new functionality into a function with a docstring, and add the feature to the
     list in README.md.
4. The pull request must pass all CI/CD jobs before being ready for review.
5. If one CI/CD job is failing for unrelated reasons you may want to create another PR to fix that
    first.

## Human Contributions

You can contribute in many ways:

### Report Bugs

Report bugs at <https://github.com/danielrjackson/unset/issues>.

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- If you can, provide detailed steps to reproduce the bug.
- If you don't have steps to reproduce the bug, just note your observations in as much detail as you
  can.

Questions to start a discussion about the issue are welcome.

### Fix Bugs

Look through the GitHub issues for bugs.
Anything tagged with "bug" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features.
Anything tagged with "enhancement" and "please-help" is open to whoever wants to implement it.

Please do not combine multiple feature enhancements into a single pull request.

### Submit Feedback

The best way to send feedback is to file an issue at <https://github.com/danielrjackson/unset/issues>.

If you are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions are welcome :)

## AI Contributions

Check the [Contributor Guidelines] for general guidelines on how to contribute.

Instead of using GitHub's Issues, you must use the `/docs/changelog` directory to record your
contributions.

For your next task, check the [`/docs/TASKS.md`] file for the task list and instructions on how to
complete tasks. Choose the first uncompleted task and complete it.

## See Also

- [Authors]
- [Changelog]
- [Contributors] [^1]
- [Tasks]

[//]: # (Links)

[Testing]: #testing
[Lessons Learned]: #lessons-learned
[`/docs/TASKS.md`]: TASKS.md
[template]: templates/changelog/template.md
[example]: changelog/main_1.0.0_20250801T095500Z.md
[Contributor Guidelines]: #contribution-guidelines
[Authors]: AUTHORS.md
[Changelog]: CHANGELOG.md
[Contributors]: CONTRIBUTORS.md
[Tasks]: TASKS.md
[AI Assistants]: CONTRIBUTORS.md#ai-assistants

<!-- Footnotes -->

[^1]: *See [AI Assistants] for a list of AI assistants that contributed to this project.*
