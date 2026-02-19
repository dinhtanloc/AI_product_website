from app.models.image_synthetic import ImageSyntheticModel

class ImageSyntheticService:
    def __init__(self, model_name: str = "CompVis/ldm-text2im-large-256"):
        self.model = ImageSyntheticModel(model_name)

    def synthesize(self, prompt: str, **kwargs):
        return self.model.synthesize(prompt, **kwargs)
