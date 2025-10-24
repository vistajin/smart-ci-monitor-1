from fastapi import FastAPI
from api import jenkins_routes, ai_routes, notify_routes

app = FastAPI(title="Smart CI/CD Monitor")

app.include_router(jenkins_routes.router, prefix="/jenkins")
app.include_router(ai_routes.router, prefix="/ai")
app.include_router(notify_routes.router, prefix="/notify")

@app.get("/")
def root():
    return {"status": "Smart CI/CD Monitor is running"}
