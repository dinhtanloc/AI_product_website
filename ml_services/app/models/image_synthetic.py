from diffusers import DiffusionPipeline
import torch

class ImageSyntheticModel:
    def __init__(self, model_name: str = "CompVis/ldm-text2im-large-256"):
        self.pipe = DiffusionPipeline.from_pretrained(model_name, dtype=torch.bfloat16, device_map="mps")

    def synthesize(self, prompt, **kwargs):
        result = self.pipe(prompt, **kwargs)
        return result.images[0] if hasattr(result, "images") else result
