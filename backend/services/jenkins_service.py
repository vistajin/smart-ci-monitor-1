import os, requests

JENKINS_URL = os.getenv("JENKINS_URL")
JENKINS_USER = os.getenv("JENKINS_USER")
JENKINS_TOKEN = os.getenv("JENKINS_TOKEN")

# If JENKINS_URL not configured, return stub data for demo
def fetch_all_jobs():
    if not JENKINS_URL:
        return [
            {"name":"example-job-1","url":"http://jenkins/job/example-job-1","last_build": {"number":42,"result":"FAILURE"}},
            {"name":"example-job-2","url":"http://jenkins/job/example-job-2","last_build": {"number":7,"result":"SUCCESS"}}
        ]
    url = f"{JENKINS_URL}/api/json?tree=jobs[name,url,lastBuild[number,result]]"
    r = requests.get(url, auth=(JENKINS_USER, JENKINS_TOKEN))
    r.raise_for_status()
    data = r.json()
    return data.get("jobs",[])

def fetch_job_builds(job_name):
    if not JENKINS_URL:
        # sample builds
        if job_name == "example-job-1":
            return [
                {"number":41,"result":"SUCCESS","timestamp":1620000000000},
                {"number":42,"result":"FAILURE","timestamp":1620003600000}
            ]
        return None
    url = f"{JENKINS_URL}/job/{job_name}/api/json?tree=builds[number,result,timestamp]"
    r = requests.get(url, auth=(JENKINS_USER, JENKINS_TOKEN))
    r.raise_for_status()
    return r.json().get("builds",[])
