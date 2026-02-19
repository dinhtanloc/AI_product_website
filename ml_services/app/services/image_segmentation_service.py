from app.models.image_segmentation import ImageSegmentationModel
from PIL import Image
import base64
from io import BytesIO

class ImageSegmentationService:
    def __init__(self, model_name: str = "facebook/detr-resnet-50-panoptic"):
        self.model = ImageSegmentationModel(model_name)

    def segment(self, image_base64: str):
        image = Image.open(BytesIO(base64.b64decode(image_base64)))
        return self.model.segment(image)
