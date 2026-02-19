import sys
from app.main import app

# This file is the entrypoint for uvicorn
# Usage: uvicorn main:app --reload --host 0.0.0.0 --port 8001
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
