from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)

    question_text = Column(Text, nullable=False)

    option_a = Column(String, nullable=False)
    option_b = Column(String, nullable=False)
    option_c = Column(String, nullable=False)
    option_d = Column(String, nullable=False)

    correct_answer = Column(String, nullable=False)

    domain = Column(String)  # digital / analog / backend / mixed

    difficulty = Column(Integer)  # 1 (easy) - 5 (hard)