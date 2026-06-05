from pydantic import BaseModel, Field

class ResumeAnalysisReport(BaseModel):

    strengths: list[str] = Field(
        description = "Major strengths found in the resume"
    )

    weaknesses: list[str] = Field(
        description = "Weaknesses or areas of improvement"
    )

    suggestions: list[str] = Field(
        description = "Actionable suggestions to improve the resume"
    )
    