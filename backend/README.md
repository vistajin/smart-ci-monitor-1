Smart CI Monitor - Backend

Quick start (development):

1. Create a virtualenv and install:
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

2. (Optional) configure environment variables:
    export JENKINS_URL="https://your-jenkins"
    export JENKINS_USER="user"
    export JENKINS_TOKEN="token"
    export SLACK_WEBHOOK="https://hooks.slack.com/..."
    export TEAMS_WEBHOOK="https://outlook.office.com/webhook/..."

3. Initialize DB:
    python database/db.py

4. Run:
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
