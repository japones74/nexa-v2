from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "ok"
    }


@router.get("/info")
def info():
    return {
        "name": "NEXA API",
        "version": "0.1.0",
        "description": "Base API running on FastAPI"
    }
