from fastapi import APIRouter
from services.notify_service import send_to_slack, send_to_teams

router = APIRouter()

@router.post("/slack")
def notify_slack(payload: dict):
    send_to_slack(payload.get("message",""))
    return {"status":"sent"}

@router.post("/teams")
def notify_teams(payload: dict):
    send_to_teams(payload.get("message",""))
    return {"status":"sent"}
