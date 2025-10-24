import re
import random

# Simple heuristic-based "AI" for demo purposes.
# In production you would call an LLM (e.g., OpenAI) or use a trained model.

def analyze_build_log(log_text: str):
    # return classification, short summary, recommendations
    if not log_text:
        return {"category":"unknown","summary":"No log provided","recommendations":[]}
    lower = log_text.lower()
    # heuristic categories
    if "outofmemory" in lower or "oom" in lower:
        cat = "resource"
        recs = ["Increase build agent memory","Check for memory leaks"]
    elif "failed to connect" in lower or "connection timed out" in lower or "unable to connect" in lower:
        cat = "network"
        recs = ["Check network/proxy settings","Retry the repository access"]
    elif "test failed" in lower or "assert" in lower:
        cat = "test"
        recs = ["Inspect failing unit tests","Run tests locally with same env"]
    elif "compilation error" in lower or "cannot find symbol" in lower or "error:" in lower:
        cat = "build"
        recs = ["Check dependency versions","Inspect compilation error details"]
    else:
        cat = "unknown"
        recs = ["Inspect full log", "Check recent changes"]

    # simple summary: first 3 lines with errors or first 200 chars
    lines = log_text.strip().splitlines()
    error_lines = [l for l in lines if re.search(r'error|fail|exception|traceback', l, re.I)]
    if error_lines:
        summary = "\n".join(error_lines[:3])
    else:
        summary = (log_text[:400] + "...") if len(log_text) > 400 else log_text

    # fake confidence score
    confidence = round(random.uniform(0.6, 0.95), 2)

    return {"category":cat, "summary":summary, "recommendations":recs, "confidence":confidence}

def predict_failure_risk(features: dict):
    # Simple rule: if recent_failures > 2 or avg_duration increased, return high prob
    recent_failures = features.get("recent_failures",0)
    duration_change = features.get("duration_change_pct",0)
    score = 0.05
    score += min(0.6, 0.2 * recent_failures)
    if duration_change and duration_change > 20:
        score += 0.2
    return round(min(score,0.99),2)
