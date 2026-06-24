from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.models.question import Question

router = APIRouter()

@router.post("/seed")
def seed_questions(db: Session = Depends(get_db)):

    q1 = Question(
        question_text="What is a flip-flop used for?",
        option_a="Amplification",
        option_b="Memory storage",
        option_c="Filtering",
        option_d="Power control",
        correct_answer="B",
        domain="digital_design",
        difficulty=1
    )

    db.add(q1)
    db.commit()

    return {"message": "Question seeded"}
@router.get("/")
def get_questions(db: Session = Depends(get_db)):
    return db.query(Question).all()

@router.delete("/cleanup")
def cleanup_old_questions(db: Session = Depends(get_db)):

    deleted = (
        db.query(Question)
        .filter(Question.domain == "digital")
        .delete()
    )

    db.commit()

    return {
        "message": f"Deleted {deleted} old questions"
    }