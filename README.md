# 🚨 Incident Intelligence System

An end-to-end data pipeline and analytics project that simulates real-time incident data, processes it, exposes APIs, and visualizes insights using Power BI.

---

## 📌 Project Overview

This project demonstrates a complete data workflow:

- Generate simulated incident data
- Process & transform raw data
- Store structured data in PostgreSQL
- Expose APIs using FastAPI
- Build an interactive UI using Streamlit
- Visualize insights in Power BI
- Trigger dashboard refresh using API automation

---

## 🏗️ Architecture

![Architecture](architecture.png)

---

## ⚙️ Tech Stack

- **Python** (Data generation & processing)
- **FastAPI** (Backend APIs)
- **PostgreSQL** (Database)
- **Streamlit** (Frontend UI)
- **Power BI Service** (Dashboard & Analytics)
- **Azure AD** (API Authentication)
- **On-Premises Gateway** (Secure DB connection)

---

## 🔄 Data Pipeline Flow

1. Generate raw data → `incidents_raw`
2. Process data → `incidents_processed`
3. APIs expose data
4. UI triggers pipeline actions
5. Power BI reads processed data
6. Dashboard refresh triggered via API

---

## 📊 Features

### 🔹 Data Pipeline
- Generate synthetic incident data
- Data cleaning & transformation
- Severity classification & scoring
- Response time calculation

### 🔹 Backend APIs (FastAPI)
- `/generate-data` → Generate data
- `/run-processing` → Process data
- `/incidents` → Get all incidents
- `/critical` → Get critical incidents
- `/delete-processed` → Clear processed data
- `/refresh-powerbi` → Trigger Power BI refresh

### 🔹 Frontend (Streamlit)
- Generate Data button
- Run Processing button
- Load All Incidents
- Show Critical Incidents
- Clear Processed Data
- Refresh Power BI Dashboard
- Embedded Power BI Dashboard (iframe)

### 🔹 Power BI Dashboard
- KPI Cards (Total, Critical, Open, Avg Response Time)
- Incident Trend Analysis (Time series)
- Incident Severity Distribution
- Map Visualization (Location-based insights)
- Interactive Slicers
- Custom measures & transformations

---

## 🗄️ Database Schema

### `incidents_raw`
Stores raw generated data.

### `incidents_processed`
Stores cleaned & enriched data with:
- severity_score
- priority_flag
- incident_date

---

## 🖥️ Screenshots

### 📊 Dashboard
![Dashboard](dashboard.png)

### 🧾 UI
![UI](ui.png)

### 🔌 API
![API](api.png)

---

## 🚀 How to Run

### 1️⃣ Clone Repo
```bash
git clone https://github.com/your-username/incident-intelligence-system.git
cd incident-intelligence-system
