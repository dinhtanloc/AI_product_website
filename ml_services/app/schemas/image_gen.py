from pydantic import BaseModel
from typing import Optional

class ImageGenRequest(BaseModel):
    prompt: str
    negative_prompt: Optional[str] = None
    num_inference_steps: Optional[int] = 25
    guidance_scale: Optional[float] = 7.5
    width: Optional[int] = 512
    height: Optional[int] = 512

class ImageGenResponse(BaseModel):
    image_base64: str
