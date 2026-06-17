import random
#from collections import defaultdict 
from sqlalchemy.orm import Session

from app.models.question import Question




DOMAINS = [
    "digital_design",
    "analog_design",
    "backend",
    "mixed_signal",
    "verification",
    "eda_tools"
]

QUICK_TOTAL = 10

QUICK_DISTRIBUTION = {
    "digital_design": 2,
    "analog_design": 2,
    "backend": 2,
    "mixed_signal": 2,
    "verification": 1,
    "eda_tools": 1
}

FULL_TOTAL = 60

FULL_DISTRIBUTION = {
    "digital_design": 10,
    "analog_design": 10,
    "backend": 10,
    "mixed_signal": 10,
    "verification": 10,
    "eda_tools": 10
}


# Difficulty weights (used later for adaptive upgrade)
DIFFICULTY_WEIGHTS = {
    1: 1.5,  # easy
    2: 1.2,
    3: 1.0,  # medium
    4: 0.8,
    5: 0.6   # hard
}




def get_questions_by_domain(db: Session, domain: str):
    return db.query(Question).filter(
        Question.domain == domain
    ).all()


def shuffle_weighted(questions):
    """
    Weighted shuffle (bias toward easier questions slightly)
    """
    weighted = []

    for q in questions:
        weight = DIFFICULTY_WEIGHTS.get(q.difficulty, 1.0)
        weighted.extend([q] * int(weight * 10))

    random.shuffle(weighted)

    seen = set()
    result = []

    for q in weighted:
        if q.id not in seen:
            result.append(q)
            seen.add(q.id)

    return result


def pick_n(questions, n, used_ids):
    
    available = [q for q in questions if q.id not in used_ids]

    if not available:
        return []

    selected = random.sample(
        available,
        min(n, len(available))
    )

    for q in selected:
        used_ids.add(q.id)

    return selected


def generate_questions(db: Session, distribution, total_questions):

    selected_questions = []
    used_ids = set()

    domain_questions = {
        domain: shuffle_weighted(
            get_questions_by_domain(db, domain)
        )
        for domain in DOMAINS
    }

    # Balanced selection
    for domain, count in distribution.items():

        questions = domain_questions.get(domain, [])

        picked = pick_n(
            questions,
            count,
            used_ids
        )

        selected_questions.extend(picked)

    # Fill remaining slots
    all_questions = [
        q
        for qs in domain_questions.values()
        for q in qs
    ]

    remaining_slots = (
        total_questions
        - len(selected_questions)
    )

    if remaining_slots > 0:

        extra = pick_n(
            all_questions,
            remaining_slots,
            used_ids
        )

        selected_questions.extend(extra)
    random.shuffle(selected_questions)

    return selected_questions[:total_questions]

def generate_quick_assessment(db: Session):

    return generate_questions(
        db,
        QUICK_DISTRIBUTION,
        QUICK_TOTAL
    )


def generate_full_assessment(db: Session):

    return generate_questions(
        db,
        FULL_DISTRIBUTION,
        FULL_TOTAL
    )

  