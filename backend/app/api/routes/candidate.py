from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.dependencies import get_db

from app.models.candidate import Candidate
from app.models.assessment_session import AssessmentSession

from app.services.assessment_report_service import (
    generate_assessment_report
)

from app.schemas.candidate import CandidateCreate

router = APIRouter()


@router.post("/")
def create_candidate(
    candidate_data: CandidateCreate,
    db: Session = Depends(get_db)
):

    candidate = Candidate(
        full_name=candidate_data.full_name,
        email=candidate_data.email,
        university=candidate_data.university,
        programme=candidate_data.programme,
        cgpa=candidate_data.cgpa,
        graduation_year=candidate_data.graduation_year
    )

    db.add(candidate)
    db.commit()
    db.refresh(candidate)

    return {
        "candidate_id": candidate.id,
        "full_name": candidate.full_name
    }


@router.get("/{candidate_id}")
def get_candidate(
    candidate_id: int,
    db: Session = Depends(get_db)
):

    candidate = (
        db.query(Candidate)
        .filter(
            Candidate.id == candidate_id
        )
        .first()
    )

    if not candidate:
        return {
            "message": "Candidate not found"
        }

    return {
        "id": candidate.id,
        "full_name": candidate.full_name,
        "email": candidate.email,
        "university": candidate.university,
        "programme": candidate.programme,
        "cgpa": candidate.cgpa,
        "graduation_year": candidate.graduation_year
    }


@router.get("/")
def get_all_candidates(
    db: Session = Depends(get_db)
):

    candidates = (
        db.query(Candidate)
        .all()
    )


    return [
        {
            "id": candidate.id,
            "full_name": candidate.full_name,
            "email": candidate.email,
            "university": candidate.university,
            "programme": candidate.programme,
            "cgpa": candidate.cgpa,
            "graduation_year": candidate.graduation_year
        }
        for candidate in candidates
    ]


@router.get("/{candidate_id}/report")
def get_candidate_report(
    candidate_id: int,
    db: Session = Depends(get_db)
):

    latest_session = (
        db.query(AssessmentSession)
        .filter(
            AssessmentSession.user_id == candidate_id
        )
        .order_by(
            AssessmentSession.id.desc()
        )
        .first()
    )

    if not latest_session:

        return {
            "message": "No assessment found"
        }

    return generate_assessment_report(
        db=db,
        session_id=latest_session.id
    )

