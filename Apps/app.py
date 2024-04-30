import streamlit as st
import requests
import json
import base64
from PIL import Image
from io import BytesIO

# Define a function to generate an image
def generate_image(prompt):
    # Prepare the request data with your prompt
    data = {
        "prompt": prompt
    }

    # Send a request to your LitServe server
    response = requests.post("https://8000-01hwnarbqtt992v1wpjg6cteac.cloudspaces.litng.ai/predict", json=data)

    # Get the Base64-encoded image string from the response
    img_str = response.content.decode("utf-8")
    if img_str:
        img_data = json.loads(img_str)
        img_bytes = base64.b64decode(img_data.get("image"))
        img = Image.open(BytesIO(img_bytes))
        return img
    else:
        return None

# Streamlit app
st.title('Image Generator')

# User input for the prompt
prompt = st.text_input('Enter a prompt:', 'Mafia spongebob with green suit jumping off a plane')

# Button to generate the image
if st.button('Generate Image'):
    image = generate_image(prompt)
    if image is not None:
        st.image(image)
    else:
        st.write('No image data found.')