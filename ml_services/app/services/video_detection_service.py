
from app.models.video_detection import VideoDetectionModel
from app.models.image_detection import ImageDetectionModel
from PIL import Image
import base64
from io import BytesIO

class VideoDetectionService:
    def __init__(self, image_model_name: str = "hustvl/yolos-tiny"):
        self.image_model = ImageDetectionModel(image_model_name)
        self.model = VideoDetectionModel(self.image_model)

    def detect_in_video(self, frames_base64: list):
        frames = [Image.open(BytesIO(base64.b64decode(f))) for f in frames_base64]
        return self.model.detect_in_video(frames)
