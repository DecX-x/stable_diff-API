import argparse
import requests
import base64
from io import BytesIO
from PIL import Image

# Initialize argument parser
parser = argparse.ArgumentParser(description="Generate images from prompts using LitServe")

# Add an argument for an optional prompt with a default value
parser.add_argument("--prompt", type=str, default="An astronaut riding a horse on Mars.",
                    help="Text prompt for the image generation")

# Parse the command-line arguments
args = parser.parse_args()

# Use the provided prompt, or fall back to the default prompt
prompt_text = args.prompt

# Prepare the request data with your prompt
data = {
    "prompt": prompt_text
}

# Send a request to your LitServe server
response = requests.post("http://localhost:8000/predict", json=data)

# Get the Base64-encoded image string from the response
img_str = response.json().get("image")

if img_str:
    # Decode the Base64 string to bytes
    img_bytes = base64.b64decode(img_str)

    # Convert bytes data to PIL Image
    img = Image.open(BytesIO(img_bytes))

    # Save the image
    img.save("generated_image.png")
    print("Image saved successfully.")
else:
    print("No image data found.")