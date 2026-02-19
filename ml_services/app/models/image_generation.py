import torch
from diffusers import DiffusionPipeline
from typing import Optional

class ImageGenerationModel:
    def __init__(self, model_name: str = "Manojb/stable-diffusion-2-1-base", device: str = "mps"):
        self.pipe = DiffusionPipeline.from_pretrained(
            model_name,
            device_map=device
        )

    def generate(self, prompt: str, **kwargs):
        result = self.pipe(prompt, **kwargs)
        return result.images[0] if hasattr(result, "images") else result
