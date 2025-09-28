import os
import shutil
import subprocess
import sys
from pathlib import Path

import tomlkit
from loguru import logger


def check_and_format_toml(file_path: Path) -> None:
    """Checks and formats a single TOML file.

    Exits if any of the steps fail.

    """
    try:
        with open(file_path, "r") as f:
            original = f.read()
            parsed = tomlkit.parse(original)
    except Exception as e:
        raise RuntimeError(f"Couldn't parse the contents of '{file_path}'.") from e
    logger.info(f"The syntax of '{file_path}' is correct.")
    formatted = tomlkit.dumps(parsed)
    if formatted != original:
        with open(file_path, "w") as f:
            f.write(formatted)
        raise RuntimeError(
            f"'{file_path}' wasn't formatted correctly and has been reformatted."
        )
    logger.info(f"'{file_path}' is formatted correctly.")


def main() -> None:
    """Implements the CI pipeline.

    The pipline performs the following checks:

    #. linting with Ruff.
    #. Type checking with MyPy.
    #. Formatting the Python code and the ``pyproject.toml``.

    The pipeline completes successfully if and only if no errors are found and returns
    with error code `1` as soon as an error is found.

    """
    PYTHON_FILES = [
        "backend",
        "commons",
        "frontend",
        "pre_commit_script.py",
        "rxconfig.py",
    ]
    """Stores the paths of the files and folders that contain Python code."""

    # Lint the Python files
    logger.info("Linting the Pyhton files...")
    # Sometimes Ruff fails to update the cache, so we force it to start from scratch
    # each time
    if os.path.isdir(".ruff_cache"):
        shutil.rmtree(".ruff_cache")
    result = subprocess.run(["ruff", "check"] + PYTHON_FILES)
    if result.returncode != 0:
        logger.error("Ruff found some errors.")
        sys.exit(1)
    logger.info("No errors where found.")

    # MyPy
    # Sometimes MyPy fails to update the cache, so we force it start from scratch
    # each time
    if os.path.isdir(".mypy_cache"):
        shutil.rmtree(".mypy_cache")
    for target_idx, target in enumerate(PYTHON_FILES):
        logger.info(f"Checking the types of `{target}`...")
        result = subprocess.run(["mypy", target])
        if result.returncode != 0:
            logger.error(f"`{target}` contains some type errors.")
            sys.exit(1)
        logger.info(f"The types of `{target}` are correct.")

    # Format the Python files
    logger.info("Checking the formatting of the Pyhton files...")
    result = subprocess.run(["ruff", "format", "--check"] + PYTHON_FILES)
    if result.returncode != 0:
        logger.error(
            (
                "Some Python files of the main project aren't formatted correctly. Run "
                + "the `uv run {}` command to fix the issue."
            ).format(" ".join(["ruff", "format"] + PYTHON_FILES)),
        )
        sys.exit(1)
    logger.info("All Pyhton files of the main project are formatted correctly.")

    check_and_format_toml(Path("pyproject.toml"))


if __name__ == "__main__":
    main()
