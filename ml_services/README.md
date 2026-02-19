# ML Services for Image Generation

This FastAPI service provides endpoints for generating images using Hugging Face models (e.g., Stable Diffusion).

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the service:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8001
   ```

## Endpoints

- `POST /generate-image/`  
  Generate an image from a text prompt. Returns a base64-encoded PNG image.
  
  **Request body:**
  ```json
  {
    "prompt": "A fantasy landscape, trending on artstation",
    "negative_prompt": "low quality, blurry",
    "num_inference_steps": 25,
    "guidance_scale": 7.5,
    "width": 512,
    "height": 512
  }
  ```

- `GET /`  
  Health check endpoint.

## Notes
- The default model is `stabilityai/stable-diffusion-2-1`. You can change it in `main.py`.
- The service returns images as base64-encoded PNGs for easy integration with web frontends.
