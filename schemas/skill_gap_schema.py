from pydantic import BaseModel 
from typing import List

class SkillGapReport(BaseModel):
    matching_skills: List[str]

    missing_skills: List[str]

    priority_skills:List[str]

    learning_roadmap: List[str]
    