from app.models.image_detection import ImageDetectionModel
from PIL import Image
import base64
from io import BytesIO

class ImageDetectionService:
    def __init__(self, model_name: str = "hustvl/yolos-tiny"):
        self.model = ImageDetectionModel(model_name)

    def detect(self, image_base64: str):
        image = Image.open(BytesIO(base64.b64decode(image_base64)))
        return self.model.detect(image)
