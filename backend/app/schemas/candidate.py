from pydantic import BaseModel


class CandidateCreate(BaseModel):
    full_name: str
    email: str
    university: str
    programme: str
    cgpa: str
    graduation_year: str