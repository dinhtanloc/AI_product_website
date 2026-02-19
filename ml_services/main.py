
import sys
import os
import warnings
import logging
import json

# ====== DEBUG LOGGING ENABLED ======
# sys.stderr = open(os.devnull, "w")  # Để tắt log, bỏ comment dòng này

# Thiết lập logging chi tiết
logging.basicConfig(level=logging.DEBUG)

for name in [
    "torch",
    "transformers",
    "diffusers",
    "huggingface_hub",
    "urllib3",
]:
    logging.getLogger(name).setLevel(logging.DEBUG)

from fastapi.routing import APIRoute

from app.main import app

# ========= WARNINGS =========
warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", message="copying from a non-meta parameter")

# ========= ENV =========
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
os.environ["DIFFUSERS_VERBOSITY"] = "error"
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["TQDM_DISABLE"] = "1"

# ========= LOGGING =========
logging.basicConfig(level=logging.CRITICAL)

for name in [
    "torch",
    "transformers",
    "diffusers",
    "huggingface_hub",
    "urllib3",
]:
    logging.getLogger(name).setLevel(logging.CRITICAL)


def print_routes():
    print("\n=== API ROUTES ===")
    for route in app.routes:
        if isinstance(route, APIRoute):
            methods = ",".join(route.methods)
            print(f"{methods:8} {route.path}")

print_routes()
# This file is the entrypoint for uvicorn
# Usage: uvicorn main:app --reload --host 0.0.0.0 --port 8001
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
    "main:app",
    host="0.0.0.0",
    port=8001,
    reload=True,
    log_level="error",   
    access_log=False     
    )
