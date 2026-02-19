from pydantic import BaseModel
from typing import Optional

class ImageSyntheticRequest(BaseModel):
    prompt: str
    num_inference_steps: Optional[int] = 25
    guidance_scale: Optional[float] = 7.5
    width: Optional[int] = 256
    height: Optional[int] = 256

class ImageSyntheticResponse(BaseModel):
    image_base64: str
