from pydantic import BaseModel
from typing import List

class VideoDetectionRequest(BaseModel):
    frames_base64: List[str]

class VideoDetectionResponse(BaseModel):
    detections: List[list]
