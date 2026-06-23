from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db

from app.models.candidate import Candidate
from app.models.assessment_session import AssessmentSession

from app.services.result_service import (
    calculate_assessment_result
)

router = APIRouter()


@router.get("")
def get_leaderboard(
    db: Session = Depends(get_db)
):

    sessions = (
        db.query(AssessmentSession)
        .filter(
            AssessmentSession.status == "completed"
        )
        .all()
    )

    candidate_scores = {}

    for session in sessions:

        candidate = (
            db.query(Candidate)
            .filter(
                Candidate.id == session.user_id
            )
            .first()
        )

        if not candidate:
            continue

        result = calculate_assessment_result(
            db=db,
            session_id=session.id
        )

        score = result["overall_score"]
        existing = candidate_scores.get(
            candidate.id)
        if (
            existing is None
            or score > existing["score"]
        ):
            candidate_scores[candidate.id] = {
                "candidate_id": candidate.id,
                "name": candidate.full_name,
                "domain": candidate.programme,
                "score": score
            }

    leaderboard = list(candidate_scores.values())
    leaderboard.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return leaderboard[:10]