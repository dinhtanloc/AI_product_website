from pydantic import BaseModel

class ImageSegmentationRequest(BaseModel):
    image_base64: str

class ImageSegmentationResponse(BaseModel):
    segments: list
