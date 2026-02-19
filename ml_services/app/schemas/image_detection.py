from pydantic import BaseModel

class ImageDetectionRequest(BaseModel):
    image_base64: str

class ImageDetectionResponse(BaseModel):
    detections: list
