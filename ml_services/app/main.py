from fastapi import FastAPI
from app.api import (
	image_gen_router,
	image_detection_router,
	image_segmentation_router,
	video_detection_router,
	image_synthetic_router,
	root_router
)

app = FastAPI(title="ML Image Generation Service")

app.include_router(root_router)
app.include_router(image_gen_router)
app.include_router(image_detection_router)
app.include_router(image_segmentation_router)
app.include_router(video_detection_router)
app.include_router(image_synthetic_router)
