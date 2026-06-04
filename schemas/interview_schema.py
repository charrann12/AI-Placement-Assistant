from pydantic import BaseModel, Field

class InterviewQuestions(BaseModel):
    question:str
    difficulty:str
    expected_answer: str

class InterviewReport(BaseModel):
    easy_questions: list[InterviewQuestions]
    medium_questions: list[InterviewQuestions]
    hard_questions: list[InterviewQuestions]