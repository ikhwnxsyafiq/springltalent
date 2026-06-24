# SpringTalent v1.0.0

## Overview

SpringTalent is a web-based talent assessment and recruitment platform developed during an On-The-Job Training (OJT) programme for Spring Semiconductor Sdn. Bhd.

The platform helps recruiters evaluate candidates through structured technical assessments, automated scoring, skill analysis, AI-generated feedback, and downloadable assessment reports.

The system is designed to streamline candidate screening and provide data-driven hiring recommendations.

---

# Objectives

The objectives of SpringTalent are:

* Digitalize candidate assessment processes
* Reduce manual candidate evaluation effort
* Provide standardized technical assessments
* Generate automated assessment reports
* Identify candidate strengths and skill gaps
* Improve recruitment decision-making

---

# Key Features

## Candidate Features

* Candidate Registration
* Resume Upload
* Quick Assessment
* Full Assessment
* Domain-Based Assessment
* Assessment Completion Tracking
* Assessment Result Viewing
* PDF Report Download

## Recruiter Features

* Candidate Profile Review
* Candidate Assessment Reports
* Assessment Performance Monitoring
* Candidate Ranking Leaderboard

## Assessment Intelligence Features

* Automated Score Calculation
* Domain Skill Analysis
* Skill Level Mapping
* Skill Gap Identification
* Recommendation Generation
* AI Feedback Generation

---

# Technology Stack

## Frontend

* Next.js 16
* React 19
* JavaScript
* CSS

## Backend

* FastAPI
* SQLAlchemy
* JWT Authentication
* REST API Architecture

## Database

Current Development Database:

* SQLite

Future Production Recommendation:

* PostgreSQL (Neon)

## Reporting

* ReportLab PDF Generation

---

# System Architecture

Candidate
↓
Frontend (Next.js)
↓
Backend API (FastAPI)
↓
Database (SQLite)

Modules:

* Authentication Module
* Candidate Module
* Resume Module
* Assessment Module
* Reporting Module
* Leaderboard Module

---

# Project Structure

fullstack/

├── backend/

│ ├── app/

│ │ ├── api/

│ │ ├── core/

│ │ ├── models/

│ │ ├── schemas/

│ │ ├── services/

│ │ └── main.py

│ │

│ ├── springtalent.db

│ └── requirements.txt

│

├── frontend/

│ ├── public/

│ ├── src/

│ │ ├── app/

│ │ └── lib/

│ │

│ └── package.json

│

└── README.md

---

# Database Tables

## users

Stores recruiter and administrator login information.

## candidates

Stores candidate profile information.

## candidate_resumes

Stores uploaded resume information.

## questions

Stores assessment questions and answer options.

## answers

Stores candidate answers.

## assessment_sessions

Stores assessment session information.

---

# Backend Installation

## Requirements

* Python 3.11+
* pip

## Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Backend

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://localhost:8000
```

Swagger API Documentation:

```text
http://localhost:8000/docs
```

---

# Frontend Installation

## Requirements

* Node.js 20+
* npm

## Install Dependencies

```bash
npm install
```

## Run Frontend

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:3000
```

---

# Environment Configuration

Frontend:

Create:

```text
frontend/.env.local
```

Example:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

# API Modules

## Authentication

```text
/api/auth
```

## Candidate

```text
/api/candidate
```

## Assessment

```text
/api/assessment
```

## Questions

```text
/api/questions
```

## Resume

```text
/api/resume
```

## Leaderboard

```text
/api/leaderboard
```

---

# Assessment Workflow

1. Candidate registers profile
2. Candidate uploads resume
3. Candidate starts assessment
4. Candidate answers questions
5. Assessment is completed
6. System calculates score
7. Skill analysis is generated
8. PDF report is generated
9. Candidate appears on leaderboard

---

# Deployment Recommendation

## Frontend

Recommended:

* Vercel

## Backend

Recommended:

* Render

## Database

Recommended:

* Neon PostgreSQL

---

# Current Version

SpringTalent v1.0.0

Released: June 2026

---

# Future Enhancements

* PostgreSQL Migration
* AI Resume Screening
* Candidate Recommendation Engine
* Recruiter Dashboard Analytics
* Assessment Question Management UI
* Email Notification System
* Multi-Company Support

---

# Developer

Muhammad Ikhwan Syafiq

Bachelor of Electronic Engineering Technology (Honours)

Universiti Kuala Lumpur

On-The-Job Training (OJT) Software Developer

Spring Semiconductor Sdn. Bhd.

---

# License

This project was developed for educational and industrial training purposes under Spring Semiconductor Sdn. Bhd.
