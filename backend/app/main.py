from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.auth import router as auth_router
from app.core.database import Base, engine

from app.models.question import Question
from app.models.assessment_session import AssessmentSession
from app.api.routes.assessment import router as assessment_router

from app.models.answer import Answer

app = FastAPI(
    title="SpringTalent API",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Auth"]
)

# 🔥 THIS IS THE KEY FIX
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="SpringTalent API",
        version="1.0",
        routes=app.routes,
    )

    # 🔥 FORCE JWT AUTH SCHEME INTO SWAGGER
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


@app.get("/")
def home():
    return {"message": "SpringTalent API Running"}

from app.api.routes.questions import router as question_router

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