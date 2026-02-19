from app.models.image_generation import ImageGenerationModel
from app.schemas.image_gen import ImageGenRequest
from io import BytesIO
from PIL import Image
import base64

class ImageGenService:
    def __init__(self, model_name: str = "stabilityai/stable-diffusion-xl-base-1.0"):
        self.model = ImageGenerationModel(model_name)

    def generate_image(self, req: ImageGenRequest) -> str:
        result = self.model.generate(
            prompt=req.prompt,
            negative_prompt=req.negative_prompt,
            num_inference_steps=req.num_inference_steps,
            guidance_scale=req.guidance_scale,
            width=req.width,
            height=req.height
        )
        image = result[0]["image"] if isinstance(result, list) else result["image"]
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return img_str
