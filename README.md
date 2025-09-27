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

---

## User Stories

### Founder User Stories

#### Submission
- As a founder, I want to receive a reminder to submit my KPIs, so I do not miss the reporting deadline
- As a founder, I want to upload my KPI data via CSV or Excel, so I do not have to re-enter everything manually  
- As a founder, I want to manually edit or add data in a web form, so I can correct mistakes or fill in missing metrics  
- As a founder, I want to save my progress as a draft, so I can return later to finish submission  
- As a founder, I want to see a review summary before submitting, so I can check my numbers are correct  

#### Validation
- As a founder, I want to be warned if I leave required KPIs blank, so I know what is missing  
- As a founder, I want to see alerts if my numbers look unusual (e.g. revenue drop >40%), so I can double-check before submitting  

#### Transparency
- As a founder, I want to see the date of my last submission, so I know I am up to date  
- As a founder, I want to know exactly how KPIs are defined, so I do not submit the wrong data  

---

### Fund Team User Stories
* See which companies have submitted KPIs, to track reporting status
* View a company’s KPI history with charts, to spot trends and risks
* Receive alerts for red flags (e.g. <12 months runway), to act quickly
* Export portfolio data, to include in LP reports
* Configure which KPIs are required, to keep reporting consistent
* Upload or manually enter KPI data on behalf of founders, when founders provide data outside the system (e.g. by email), so the portfolio remains complete and up to date



