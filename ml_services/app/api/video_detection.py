from fastapi import APIRouter, HTTPException
from app.schemas.video_detection import VideoDetectionRequest, VideoDetectionResponse
from app.services.video_detection_service import VideoDetectionService

router = APIRouter()
service = VideoDetectionService()

@router.post("/detect-video/", response_model=VideoDetectionResponse)
def detect_video(req: VideoDetectionRequest):
    try:
        detections = service.detect_in_video(req.frames_base64)
        return VideoDetectionResponse(detections=detections)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
