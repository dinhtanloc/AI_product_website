from transformers import pipeline

class ImageSyntheticModel:
    def __init__(self, model_name: str = "CompVis/ldm-text2im-large-256"):
        self.pipe = pipeline("text-to-image", model=model_name)

    def synthesize(self, prompt, **kwargs):
        return self.pipe(prompt, **kwargs)
