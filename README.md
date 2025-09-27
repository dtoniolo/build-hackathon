# BUILD Hackathon
This repository hosts the code for the BUILD Hackathon.

The code is divided in two parts: backend and frontend. Both are implemented in Python.

## Installation
We use [`uv`](https://docs.astral.sh/uv/) as our package manager. See [here](https://docs.astral.sh/uv/) for installation instructions.

## Usage
- You can run the CI checks with the `uv run pre_commit_script.py` command.

## Project Structure

```
hackathon/
├── src/                 # Source code
├── pre_commit_script.py # Runs the CI
└── pyproject.toml       # Project file
```
