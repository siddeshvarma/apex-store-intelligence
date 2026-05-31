# Apex Store Intelligence

AI-powered store analytics system built for Purplle Tech Challenge 2026.

## Features

- CCTV video processing
- YOLOv8 person detection
- Visitor tracking
- Event generation
- FastAPI analytics API
- Real-time dashboard
- SQLite event storage

## Architecture

CCTV Video
→ YOLOv8 Detection
→ Tracking
→ Event Generation
→ FastAPI
→ SQLite
→ Dashboard

## Setup

### 1. Clone

git clone <repo>

### 2. Install

pip install -r requirements.txt

### 3. Run API

python -m uvicorn app.main:app --reload

### 4. Run Detection

python pipeline/person_detector.py

### 5. Run Dashboard

python -m streamlit run dashboard/app.py

## API Endpoints

- POST /events/ingest
- GET /stores/{id}/metrics
- GET /stores/{id}/funnel
- GET /stores/{id}/heatmap
- GET /stores/{id}/anomalies
- GET /health

## AI-Assisted Engineering

AI was used to:
- Evaluate detection models
- Design event schema
- Generate test cases
- Review architectural tradeoffs

Final engineering decisions were reviewed and adapted manually.