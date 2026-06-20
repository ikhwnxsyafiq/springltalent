from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.core.database import Base


class CandidateResume(Base):
    __tablename__ = "candidate_resumes"

    id = Column(Integer, primary_key=True, index=True)

    candidate_id = Column(Integer)

    file_name = Column(String)

    file_path = Column(String)

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )