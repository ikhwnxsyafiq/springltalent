from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.responses import StreamingResponse

from sqlalchemy.orm import Session

from app.core.dependencies import get_db

from app.models.candidate import Candidate

from app.models.assessment_session import AssessmentSession
from app.models.question import Question
from app.models.answer import Answer

from app.schemas.assessment import (
    SubmitAnswerRequest,
    StartAssessmentRequest
)

from app.services.adaptive_engine import (
    generate_quick_assessment,
    generate_full_assessment,
    generate_domain_assessment
)

from app.services.assessment_report_service import (
    generate_assessment_report
)

from app.services.pdf_service import (
    generate_pdf_report
)

router = APIRouter()


@router.post("/start")
def start_assessment(
    request: StartAssessmentRequest,
    db: Session = Depends(get_db)
):
    print("DEBUG candidate_id:", request.candidate_id)
    session = AssessmentSession(
        candidate_id=request.candidate_id
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return {
        "session_id": session.id,
        "status": session.status
    }


@router.post("/answer")
def submit_answer(
    answer_data: SubmitAnswerRequest,
    db: Session = Depends(get_db)
):

    question = (
        db.query(Question)
        .filter(
            Question.id == answer_data.question_id
        )
        .first()
    )

    if not question:
        raise HTTPException(
            status_code=404,
            detail="Question not found"
        )

    is_correct = (
        answer_data.selected_answer
        == question.correct_answer
    )

    answer = Answer(
        session_id=answer_data.session_id,
        question_id=answer_data.question_id,
        selected_answer=answer_data.selected_answer,
        is_correct=is_correct
    )

    db.add(answer)
    db.commit()

    return {
        "correct": is_correct
    }


@router.get("/quick")
def get_quick_assessment(
    db: Session = Depends(get_db)
):

    questions = generate_quick_assessment(db)

    return {
        "assessment_type": "quick",
        "total_questions": len(questions),
        "questions": [
            {
                "id": q.id,
                "question_text": q.question_text,
                "option_a": q.option_a,
                "option_b": q.option_b,
                "option_c": q.option_c,
                "option_d": q.option_d,
                "domain": q.domain,
                "difficulty": q.difficulty
            }
            for q in questions
        ]
    }


@router.get("/full")
def get_full_assessment(
    db: Session = Depends(get_db)
):

    questions = generate_full_assessment(db)

    return {
        "assessment_type": "full",
        "total_questions": len(questions),
        "questions": [
            {
                "id": q.id,
                "question_text": q.question_text,
                "option_a": q.option_a,
                "option_b": q.option_b,
                "option_c": q.option_c,
                "option_d": q.option_d,
                "domain": q.domain,
                "difficulty": q.difficulty
            }
            for q in questions
        ]
    }


@router.get("/domain/{domain}")
def get_domain_assessment(
    domain: str,
    db: Session = Depends(get_db)
):

    questions = generate_domain_assessment(
        db,
        domain

    )

    return {
        "assessment_type": domain,
        "total_questions": len(questions),
        "questions": [
            {
                "id": q.id,
                "question_text": q.question_text,
                "option_a": q.option_a,
                "option_b": q.option_b,
                "option_c": q.option_c,
                "option_d": q.option_d,
                "domain": q.domain,
                "difficulty": q.difficulty
            }
            for q in questions
        ]
    }

@router.get("/result/{session_id}")
def get_assessment_result(
    session_id: int,
    db: Session = Depends(get_db)
):

    session = (
        db.query(AssessmentSession)
        .filter(
            AssessmentSession.id == session_id
        )
        .first()
    )

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Assessment session not found"
        )

    return generate_assessment_report(
        db=db,
        session_id=session_id
    )


@router.get("/report/{session_id}")
def download_assessment_report(
    session_id: int,
    db: Session = Depends(get_db)
):

    session = (
        db.query(AssessmentSession)
        .filter(
            AssessmentSession.id == session_id
        )
        .first()
    )

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Assessment session not found"
        )

    report_data = generate_assessment_report(
        db=db,
        session_id=session_id
    )
    candidate = (
        db.query(Candidate)
        .filter(
            Candidate.id == session.candidate_id
        )
        .first()
    )
    
    pdf_buffer = generate_pdf_report(
        session_id=session_id,
        report_data=report_data,
        candidate=candidate
    )

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            f"attachment; filename=SpringTalent_Assessment_Report_{session_id}.pdf"
        }
    )


@router.post("/complete/{session_id}")
def complete_assessment(
    session_id: int,
    db: Session = Depends(get_db)
):
    session = (
        db.query(AssessmentSession)
        .filter(
            AssessmentSession.id == session_id
        )
        .first()
    )

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Assessment session not found"
        )

    session.status = "completed"
    db.commit()

    return {
        "message": "Assessment completed",
        "session_id": session.id,
        "status": session.status
    }


@router.get("/debug/sessions")
def debug_sessions(
    db: Session = Depends(get_db)
):
    sessions = (
        db.query(AssessmentSession)
        .all()
    )
    return [
        {
            "session_id": session.id,
            "candidate_id": session.candidate_id,
            "status": session.status
        }
        for session in sessions
    ]