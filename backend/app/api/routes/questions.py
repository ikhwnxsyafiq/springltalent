from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import csv
from pathlib import Path

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

@router.post("/import")
def import_questions(db: Session = Depends(get_db)):

    BASE_DIR = Path(__file__).resolve().parents[3]
    csv_file = BASE_DIR / "questions.csv"

    imported = 0

    with open(csv_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:

            existing = (
                db.query(Question)
                .filter(
                    Question.question_text == row["question_text"]
                )
                .first()
            )

            if existing:
                continue

            question = Question(
                question_text=row["question_text"],
                option_a=row["Option_A"],
                option_b=row["Option_B"],
                option_c=row["Option_C"],
                option_d=row["Option_D"],
                correct_answer=row["correct_answer"],
                domain=row["domain"],
                difficulty=2
            )

            db.add(question)
            imported += 1

        db.commit()

    return {
        "message": "Questions imported successfully",
        "imported": imported
    }    