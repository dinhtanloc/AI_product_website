from transformers import pipeline

class ImageSegmentationModel:
    def __init__(self, model_name: str = "facebook/detr-resnet-50-panoptic"):
        self.pipe = pipeline("image-segmentation", model=model_name)

    def segment(self, image):
        return self.pipe(image)
