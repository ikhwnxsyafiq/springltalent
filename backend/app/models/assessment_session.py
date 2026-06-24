from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from datetime import datetime

from app.core.database import Base


class AssessmentSession(Base):
    __tablename__ = "assessment_sessions"

    id = Column(Integer, primary_key=True, index=True)

    candidate_id = Column(Integer, ForeignKey("candidates.id"))

    status = Column(
        String,
        default="in_progress"
    )

    started_at = Column(
        DateTime,
        default=datetime.utcnow
    )