from pydantic import BaseModel, Field

class ATSReport(BaseModel):
    ats_score:int = Field(
        description = "ATS Score out of 100"
    )

    matching_keywords:list[str]=Field(
        description = "Keywords found in both resume and JD"
    )

    missing_keywords:list[str]=Field(
        description = "Important keywords missing from resume"
    )

    suggestions:list[str] = Field(
        description = "Suggestions to improve ATS score"
    )