from collections import defaultdict

from sqlalchemy.orm import Session

from app.models.answer import Answer
from app.models.question import Question


def calculate_assessment_result(
    db: Session,
    session_id: int
):
    answers = (
        db.query(Answer)
        .filter(
            Answer.session_id == session_id
        )
        .all()
    )

    if not answers:
        return {
            "overall_score": 0,
            "correct_answers": 0,
            "total_questions": 0,
            "domain_scores": {}
        }

    total_questions = len(answers)

    total_correct = sum(
        1
        for answer in answers
        if answer.is_correct
    )

    overall_score = round(
        (total_correct / total_questions) * 100,
        2
    )

    domain_total = defaultdict(int)
    domain_correct = defaultdict(int)

    for answer in answers:

        question = (
            db.query(Question)
            .filter(
                Question.id == answer.question_id
            )
            .first()
        )

        if not question:
            continue

        domain = question.domain

        domain_total[domain] += 1

        if answer.is_correct:
            domain_correct[domain] += 1

    domain_scores = {}

    for domain in domain_total:

        score = (
            domain_correct[domain]
            / domain_total[domain]
        ) * 100

        domain_scores[domain] = round(
            score,
            2
        )

    return {
        "overall_score": overall_score,
        "correct_answers": total_correct,
        "total_questions": total_questions,
        "domain_scores": domain_scores
    }