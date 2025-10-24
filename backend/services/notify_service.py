import os
import requests
import logging

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")
TEAMS_WEBHOOK = os.getenv("TEAMS_WEBHOOK")

def send_to_slack(message: str):
    if not SLACK_WEBHOOK:
        logging.info("SLACK_WEBHOOK not configured. Message:\n%s", message)
        return
    payload = {"text": message}
    requests.post(SLACK_WEBHOOK, json=payload, timeout=5)

def send_to_teams(message: str):
    if not TEAMS_WEBHOOK:
        logging.info("TEAMS_WEBHOOK not configured. Message:\n%s", message)
        return
    payload = {"text": message}
    requests.post(TEAMS_WEBHOOK, json=payload, timeout=5)
