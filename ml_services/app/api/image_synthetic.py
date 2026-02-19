from fastapi import APIRouter, HTTPException
from app.schemas.image_synthetic import ImageSyntheticRequest, ImageSyntheticResponse
from app.services.image_synthetic_service import ImageSyntheticService

router = APIRouter()
service = ImageSyntheticService()

@router.post("/synthesize-image/", response_model=ImageSyntheticResponse)
def synthesize_image(req: ImageSyntheticRequest):
    try:
        result = service.synthesize(
            req.prompt,
            num_inference_steps=req.num_inference_steps,
            guidance_scale=req.guidance_scale,
            width=req.width,
            height=req.height
        )
        image = result[0]["image"] if isinstance(result, list) else result["image"]
        from io import BytesIO
        import base64
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return ImageSyntheticResponse(image_base64=img_str)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
