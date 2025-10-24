from pydantic import BaseModel
from typing import Optional

class Build(BaseModel):
    job_name: str
    number: int
    result: Optional[str]
    timestamp: int
