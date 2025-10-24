Smart CI Monitor - Project Skeleton
===================================

This repository contains a runnable skeleton for the Smart CI/CD Monitor (backend + frontend).
The backend is a FastAPI app with simple heuristic "AI" stubs that can be replaced by real models or LLM calls.
The frontend is a minimal React app that calls the backend.

Quick start (backend):
1. cd backend
2. python -m venv venv
3. source venv/bin/activate
4. pip install -r requirements.txt
5. python database/db.py
6. uvicorn main:app --reload --host 0.0.0.0 --port 8000

Quick start (frontend):
1. cd frontend
2. npm install
3. npm start

Or use docker-compose to run backend:
docker-compose up --build
