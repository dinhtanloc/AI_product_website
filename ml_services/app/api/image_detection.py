from fastapi import APIRouter, HTTPException
from app.schemas.image_detection import ImageDetectionRequest, ImageDetectionResponse
from app.services.image_detection_service import ImageDetectionService

router = APIRouter()
service = ImageDetectionService()

@router.post("/detect-image/", response_model=ImageDetectionResponse)
def detect_image(req: ImageDetectionRequest):
    try:
        detections = service.detect(req.image_base64)
        return ImageDetectionResponse(detections=detections)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
