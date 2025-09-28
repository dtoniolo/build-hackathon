# README  

## The Problem We Tackled  
Funds and founders both waste time every reporting cycle:  
- **Chasing** – VCs spend hours nudging portfolio companies across WhatsApp, Slack, and email to get KPIs submitted.  
- **Confusion** – KPI templates differ by fund, and definitions are unclear, so ~1 in 3 submissions need clarification.  
- **Wasted effort** – Analysts still have to clean and reformat data before it can be used in LP reports.  

The result is recurring friction, poor data quality, and delays in investor reporting.  

---

## The Solution and How It Works  
We built a lightweight KPI reporting tool: 

- **For founders** – upload KPI data (CSV, Excel, email, or manual form). Data is parsed and structured.  
- **For funds** – submissions can be aggregated, reviewed, and eventually exported in a consistent format.  
- **Core flow** – founders own the accuracy of their submissions, while funds gain structured data they can trust.  

---

## Core Features and Technical Choices  

**Built during hackathon (MVP):**  
- File upload (CSV, Excel, email)  
- Manual entry form  
- Data extraction into a structured format  

**Planned features (not yet built):**  
- Validation (missing values, anomaly detection, inline definitions)  
- Fund dashboards for submission tracking and portfolio views  
- Alerts for red flags (e.g. short runway)  
- Export to LP-ready reports (CSV, PDF)  

**Technical choices:**  
- Python for both backend and frontend (fast to prototype, single language for all layers)  
- Flask + Jinja2 for the web interface  
- Pandas for data handling and extraction  
- [`uv`](https://docs.astral.sh/uv/) as the package manager for lightweight dependency management  

---

## Why It Matters and Possible Impact  
- **For funds**: faster LP reporting, clean data, reduced analyst hours.  
- **For founders**: less admin burden, consistent templates, reminders to stay compliant.  
- **For the ecosystem**: creates a foundation for structured, EU-first reporting infrastructure that could expand beyond KPIs — into cap tables, ESG, and grant reporting.  

Long-term, this approach could become the default schema for portfolio reporting in Europe, bridging the 80% overlap in fund templates while allowing the 20% to remain customisable.  

---

## External APIs, Datasets, or Tools  
- **APIs**: none used in MVP  
- **Datasets**: dummy CSV/Excel files created for demo purposes  
- **Tools**:  
  - [Canva Pitch Deck](https://www.canva.com/design/DAG0La-uW4Q/rCI_mCOrrr8JycOZsCY6PQ/edit?utm_content=DAG0La-uW4Q&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)  
  - DALL·E for concept illustrations and UI mockups used in the presentation  

## Project Structure  



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
- See which companies have submitted KPIs, to track reporting status  
- View a company’s KPI history with charts, to spot trends and risks  
- Receive alerts for red flags (e.g. <12 months runway), to act quickly  
- Export portfolio data, to include in LP reports  
- Configure which KPIs are required, to keep reporting consistent  
- Upload or manually enter KPI data on behalf of founders, when founders provide data outside the system (e.g. by email), so the portfolio remains complete and up to date  
