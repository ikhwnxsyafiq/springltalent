from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine

# Models
from app.models.question import Question
from app.models.assessment_session import AssessmentSession
from app.models.answer import Answer
from app.models.user import User
from app.models.candidate import Candidate
from app.models.candidate_resume import CandidateResume

# Routes
from app.api.routes.auth import router as auth_router
from app.api.routes.questions import router as question_router
from app.api.routes.assessment import router as assessment_router
from app.api.routes.candidate import router as candidate_router
from app.api.routes.resume import router as resume_router
from app.api.routes.leaderboard import router as leaderboard_router

app = FastAPI(
    title="SpringTalent API",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://springltalent.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

# ==========================
# ROUTERS
# ==========================

app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Auth"]
)

app.include_router(
    question_router,
    prefix="/api/questions",
    tags=["Questions"]
)

app.include_router(
    assessment_router,
    prefix="/api/assessment",
    tags=["Assessment"]
)

app.include_router(
    candidate_router,
    prefix="/api/candidate",
    tags=["Candidate"]
)

app.include_router(
    resume_router,
    prefix="/api/resume",
    tags=["Resume"]
)

app.include_router(
    leaderboard_router,
    prefix="/api/leaderboard",
    tags=["Leaderboard"]
)

# ==========================
# CUSTOM SWAGGER JWT
# ==========================

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="SpringTalent API",
        version="1.0",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            openapi_schema["paths"][path][method]["security"] = [
                {"BearerAuth": []}
            ]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

# ==========================
# HOME
# ==========================

@app.get("/")
def home():
    return {
        "message": "SpringTalent API Running"
    }