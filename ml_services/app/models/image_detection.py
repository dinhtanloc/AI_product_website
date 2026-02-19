from transformers import pipeline

class ImageDetectionModel:
    def __init__(self, model_name: str = "hustvl/yolos-tiny"):
        self.pipe = pipeline("object-detection", model=model_name)

    def detect(self, image):
        return self.pipe(image)
