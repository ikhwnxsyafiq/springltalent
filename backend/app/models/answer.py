from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from app.core.database import Base


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(
        Integer,
        ForeignKey("assessment_sessions.id")
    )

    question_id = Column(
        Integer,
        ForeignKey("questions.id")
    )

    selected_answer = Column(String)

    is_correct = Column(Boolean)