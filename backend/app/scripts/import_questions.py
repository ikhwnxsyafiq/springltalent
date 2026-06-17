import csv

from app.core.database import SessionLocal
from app.models.question import Question


db = SessionLocal()

CSV_FILE = "questions.csv"


with open(CSV_FILE, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    imported = 0

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

print(f"Imported {imported} questions")