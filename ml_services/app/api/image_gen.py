from fastapi import APIRouter, HTTPException
from app.schemas.image_gen import ImageGenRequest, ImageGenResponse
from app.services.image_gen_service import ImageGenService

router = APIRouter()

service = ImageGenService()

@router.post("/generate-image/", response_model=ImageGenResponse)
def generate_image(req: ImageGenRequest):
    try:
        img_base64 = service.generate_image(req)
        return ImageGenResponse(image_base64=img_base64)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
