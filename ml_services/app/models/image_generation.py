from transformers import pipeline
import torch
from typing import Optional

class ImageGenerationModel:
    def __init__(self, model_name: str = "stabilityai/stable-diffusion-2-1"):
        self.pipe = pipeline(
            "text-to-image",
            model=model_name,
            torch_dtype=torch.float16
        )

    def generate(self, prompt: str, negative_prompt: Optional[str] = None, num_inference_steps: int = 25, guidance_scale: float = 7.5, width: int = 512, height: int = 512):
        return self.pipe(
            prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            width=width,
            height=height
        )
