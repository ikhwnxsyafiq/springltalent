from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse

from app.core.dependencies import get_db

from app.models.candidate_resume import CandidateResume
import shutil
import os

router = APIRouter()


@router.post("/upload/{candidate_id}")
def upload_resume(
    candidate_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    upload_dir = "uploads"

    os.makedirs(
        upload_dir,
        exist_ok=True
    )

    file_path = os.path.join(
        upload_dir,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    resume = CandidateResume(
        candidate_id=candidate_id,
        file_name=file.filename,
        file_path=file_path
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    return {
        "message": "Resume uploaded successfully",
        "resume_id": resume.id,
        "candidate_id": candidate_id,
        "file_name": file.filename
    }


@router.get("/candidate/{candidate_id}")
def get_candidate_resume(
    candidate_id: int,
    db: Session = Depends(get_db)
):
    resume = (
        db.query(CandidateResume)
        .filter(
            CandidateResume.candidate_id == candidate_id
        )
        .order_by(
            CandidateResume.id.desc()
        )
        .first()
    )

    if not resume:
        return {
            "message": "No resume found"
        }

    return {
        "resume_id": resume.id,
        "candidate_id": resume.candidate_id,
        "file_name": resume.file_name,
        "file_path": resume.file_path
    }


@router.get("/download/{candidate_id}")
def download_resume(
    candidate_id: int,
    db: Session = Depends(get_db)
):
    resume = (
        db.query(CandidateResume)
        .filter(
            CandidateResume.candidate_id == candidate_id
        )
        .order_by(
            CandidateResume.id.desc()
        )
        .first()
    )

    if not resume:
        return {
            "message": "No resume found"
        }

    return FileResponse(
        path=resume.file_path,
        filename=resume.file_name,
        media_type="application/pdf"
    )