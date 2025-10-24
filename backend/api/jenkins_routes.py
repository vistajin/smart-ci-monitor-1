from fastapi import APIRouter, HTTPException
from services.jenkins_service import fetch_all_jobs, fetch_job_builds

router = APIRouter()

@router.get("/jobs")
def get_jobs():
    jobs = fetch_all_jobs()
    return {"jobs": jobs}

@router.get("/jobs/{job_name}/builds")
def get_builds(job_name: str):
    builds = fetch_job_builds(job_name)
    if builds is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"builds": builds}
