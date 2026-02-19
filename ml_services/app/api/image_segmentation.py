from fastapi import APIRouter, HTTPException
from app.schemas.image_segmentation import ImageSegmentationRequest, ImageSegmentationResponse
from app.services.image_segmentation_service import ImageSegmentationService

router = APIRouter()
service = ImageSegmentationService()

@router.post("/segment-image/", response_model=ImageSegmentationResponse)
def segment_image(req: ImageSegmentationRequest):
    try:
        segments = service.segment(req.image_base64)
        return ImageSegmentationResponse(segments=segments)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
