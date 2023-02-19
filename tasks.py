"""
This script defines a series of tasks using the Invoke library to automate
common development operations such as cleaning generated files and directories,
formatting code, running tests, etc.

The tasks defined in this script include:

- clean: Remove generated files and directories.
- format: Format code using black.
- test: Run unit tests using pytest.
- lint: Check code style using flake8.
- typecheck: Run the mypy type checker.
- build: Build a distributable package.
- release: Create a new release on PyPI.

Usage: invoke <task>

For more information on each task, run 'invoke --help <task>'.
"""

import os
import pathlib
import invoke

CLEAN_DIRS = [
    "*.egg-info",
    ".mypy_cache",
    ".pytest_cache",
    "build",
    "dist",
]


@invoke.task
def clean(ctx):
    """
    Remove generated files and directories.

    Arguments:
        ctx (invoke.Context): The Invoke context.

    Raises:
        None.

    Returns:
        None.
    """
    for path in pathlib.Path(".").glob("**/__pycache__"):
        shutil.rmtree(path)

    for pattern in CLEAN_DIRS:
        for path in pathlib.Path.cwd().glob(pattern):
            if path.is_file():
                path.unlink()
            elif path.is_dir():
                shutil.rmtree(path)


@invoke.task
def format(ctx, check=False):
    """
    Format code using black.

    Arguments:
        ctx (invoke.Context): The Invoke context.
        check (bool): Whether to check the code formatting without making changes.

    Raises:
        None.

    Returns:
        None.
    """
    cmd = "black" + (" --check" if check else "") + " src"
    ctx.run(cmd)


@invoke.task
def test(ctx):
    """
    Run unit tests using pytest.

    Arguments:
        ctx (invoke.Context): The Invoke context.

    Raises:
        None.

    Returns:
        None.
    """
    ctx.run("pytest")


@invoke.task
def lint(ctx):
    """
    Check code style using flake8.

    Arguments:
        ctx (invoke.Context): The Invoke context.

    Raises:
        None.

    Returns:
        None.
    """
    ctx.run("flake8 src")


@invoke.task
def typecheck(ctx):
    """
    Run the mypy type checker.

    Arguments:
        ctx (invoke.Context): The Invoke context.

    Raises:
        None.

    Returns:
        None.
    """
    cmd = "mypy --strict --show-error-context src"
    ctx.run(cmd)


@invoke.task
def build(ctx):
    """
    Build a distributable package.

    Arguments:
        ctx (invoke.Context): The Invoke context.

    Raises:
        None.

    Returns:
        None.
    """
    cmd = "python -m build --no-isolation"
    ctx.run(cmd)


@invoke.task(pre=[clean, build])
def release(ctx):
    """
    Create a new release on PyPI.

    Arguments:
        ctx (invoke.Context): The Invoke context.

    Raises:
        None.

    Returns:
        None.
    """
    if not os.getenv("TWINE_USERNAME"):
        raise ValueError("TWINE_USERNAME environment variable not set")
    if not os.getenv("TWINE_PASSWORD"):
        raise ValueError("TWINE_PASSWORD environment variable not set")

    cmd = "python -m twine upload --skip-existing dist/*"
    ctx.run(cmd)
