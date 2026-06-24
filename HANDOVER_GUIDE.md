# SpringTalent System Handover Guide

## Project Information

Project Name: SpringTalent

Version: v1.0.0

Developer: Muhammad Ikhwan Syafiq

Organization: Spring Semiconductor Sdn. Bhd.

Project Type: Talent Assessment and Recruitment Platform

---

# Project Overview

SpringTalent is a web-based recruitment and talent assessment platform developed to assist Spring Semiconductor in evaluating candidates through structured technical assessments.

The system allows candidates to register, upload resumes, complete assessments, receive automated reports, and appear on a ranking leaderboard.

The platform reduces manual screening effort and provides recruiters with assessment-driven candidate insights.

---

# Current System Components

## Frontend

Technology:

* Next.js
* React
* JavaScript

Location:

```text
frontend/
```

Purpose:

* Candidate Portal
* Assessment Interface
* Results Display
* Admin Pages

---

## Backend

Technology:

* FastAPI
* SQLAlchemy

Location:

```text
backend/
```

Purpose:

* Authentication
* Candidate Management
* Assessment Engine
* Resume Upload
* PDF Report Generation
* Leaderboard API

---

## Database

Current Database:

```text
SQLite
```

Database File:

```text
backend/springtalent.db
```

Recommended Future Database:

```text
PostgreSQL
```

---

# Database Tables

## users

Stores administrator and recruiter accounts.

## candidates

Stores candidate profiles.

## candidate_resumes

Stores uploaded resume information.

## questions

Stores assessment questions.

## answers

Stores candidate answers.

## assessment_sessions

Stores assessment attempts and completion status.

---

# Main API Modules

Authentication:

```text
/api/auth
```

Candidate:

```text
/api/candidate
```

Assessment:

```text
/api/assessment
```

Questions:

```text
/api/questions
```

Resume:

```text
/api/resume
```

Leaderboard:

```text
/api/leaderboard
```

---

# Deployment Recommendation

## Frontend

Recommended Platform:

Vercel

Benefits:

* Free hosting
* Easy deployment
* Automatic GitHub integration

---

## Backend

Recommended Platform:

Render

Benefits:

* Free deployment
* FastAPI support
* Automatic GitHub deployment

---

## Database

Recommended Platform:

Neon PostgreSQL

Benefits:

* Free PostgreSQL database
* Cloud hosted
* Suitable for production deployment

---

# System Startup Procedure

Backend:

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Frontend:

```bash
cd frontend

npm install

npm run dev
```

---

# Maintenance Notes

## Adding New Questions

Questions can be inserted into:

```text
questions table
```

through API endpoints or database updates.

---

## Updating Assessment Logic

Assessment logic is located in:

```text
backend/app/services/
```

---

## Updating Leaderboard

Leaderboard API:

```text
backend/app/api/routes/leaderboard.py
```

---

## Updating Reports

PDF report generation:

```text
backend/app/services/pdf_service.py
```

---

# Known Limitations

Current version uses SQLite.

Single-server deployment only.

No email notification system.

No recruiter analytics dashboard.

---

# Future Enhancements

* PostgreSQL Migration
* AI Resume Screening
* Candidate Recommendation Engine
* Recruiter Dashboard Analytics
* Email Notifications
* Multi-Company Support

---

# Handover Contact

Developer:

Muhammad Ikhwan Syafiq

Universiti Kuala Lumpur

Bachelor of Electronic Engineering Technology (Honours)

OJT Software Developer

Spring Semiconductor Sdn. Bhd.
