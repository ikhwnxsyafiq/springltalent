# SpringTalent Installation Guide

## Overview

This guide explains how to install, configure, and run the SpringTalent platform locally.

---

# System Requirements

## Backend

* Python 3.11 or higher
* pip

## Frontend

* Node.js 20 or higher
* npm

## Development Tools

* Git
* Visual Studio Code

---

# Clone Repository

```bash
git clone https://github.com/ikhwnxsyafiq/springltalent.git

cd springltalent
```

---

# Backend Setup

Navigate to backend:

```bash
cd backend
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Backend

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

# Database

Current version uses SQLite.

Database file:

```text
backend/springtalent.db
```

No additional database installation is required.

---

# Frontend Setup

Navigate to frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

---

# Environment Variables

Create:

```text
frontend/.env.local
```

Add:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

# Run Frontend

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:3000
```

---

# Login

Use credentials created through the authentication module.

---

# Common Issues

## Backend Not Starting

Verify:

```bash
pip install -r requirements.txt
```

completed successfully.

---

## Frontend Cannot Reach Backend

Verify:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

and backend is running.

---

## Swagger Not Loading

Verify:

```text
http://localhost:8000/docs
```

and FastAPI is running.

---

# Deployment Recommendation

Frontend:

* Vercel

Backend:

* Render

Database:

* PostgreSQL (Neon)

---

# Maintainer

Muhammad Ikhwan Syafiq

Spring Semiconductor OJT Project

SpringTalent v1.0.0
