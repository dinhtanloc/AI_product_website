import requests
from PIL import Image
from io import BytesIO
import base64
import matplotlib.pyplot as plt

# Thay đổi URL endpoint cho phù hợp với server của bạn
ENDPOINTS = [
    "http://0.0.0.0:8001/generate-image/",
    "http://0.0.0.0:8001/synthesize-image/"
]

# Ví dụ payload cho endpoint tạo ảnh
payload = {
    "prompt": "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
}

def show_image_from_base64(b64_str, title=None):
    image = Image.open(BytesIO(base64.b64decode(b64_str)))
    plt.imshow(image)
    plt.axis('off')
    if title:
        plt.title(title)
    plt.show()

def test_image_endpoints():
    for url in ENDPOINTS:
        print(f"Requesting: {url}")
        try:
            resp = requests.post(url, json=payload, timeout=120)
            resp.raise_for_status()
            data = resp.json()
            # API trả về key 'image_base64'
            b64_img = data.get('image_base64')
            if b64_img:
                show_image_from_base64(b64_img, title=url)
            else:
                print(f"No image found in response from {url}")
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(f"Error with {url}: {e}")

if __name__ == "__main__":
    test_image_endpoints()
