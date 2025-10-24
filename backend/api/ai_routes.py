from fastapi import APIRouter
from services.ai_service import analyze_build_log, predict_failure_risk

router = APIRouter()

@router.post("/analyze")
def analyze(payload: dict):
    # payload expected: { "job": "...", "build": {...}, "log": "..." }
    result = analyze_build_log(payload.get("log",""))
    return {"analysis": result}

@router.post("/predict")
def predict(payload: dict):
    features = payload.get("features", {})
    score = predict_failure_risk(features)
    return {"failure_probability": score}
