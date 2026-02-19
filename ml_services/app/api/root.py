from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "ML Image Generation Service is running."}
