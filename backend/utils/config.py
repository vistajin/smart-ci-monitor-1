import os

class Settings:
    JENKINS_URL = os.getenv("JENKINS_URL")
    JENKINS_USER = os.getenv("JENKINS_USER")
    JENKINS_TOKEN = os.getenv("JENKINS_TOKEN")
    SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")
    TEAMS_WEBHOOK = os.getenv("TEAMS_WEBHOOK")
    DB_PATH = os.getenv("DB_PATH","/mnt/data/smart_ci_monitor.db")

settings = Settings()
