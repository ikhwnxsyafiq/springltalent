from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from datetime import datetime

from app.core.database import Base


class AssessmentSession(Base):
    __tablename__ = "assessment_sessions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    status = Column(String, default="in_progress")
    # in_progress / completed

    started_at = Column(DateTime, default=datetime.utcnow)