from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.core.database import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)

    email = Column(String)

    university = Column(String)

    programme = Column(String)

    cgpa = Column(String)

    graduation_year = Column(String)


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )