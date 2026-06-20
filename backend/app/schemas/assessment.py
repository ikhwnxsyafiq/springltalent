from pydantic import BaseModel


class SubmitAnswerRequest(BaseModel):
    session_id: int
    question_id: int
    selected_answer: str


class StartAssessmentRequest(BaseModel):
    candidate_id: int