from dotenv import load_dotenv
load_dotenv()  # Load all environment variables

import streamlit as st
import torch
from transformers import AutoProcessor, AutoModelForCausalLM, BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os

# Load Mistral 7B model (make sure to have enough resources)
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16, device_map="auto")
processor = AutoProcessor.from_pretrained(MODEL_NAME)

# Load BLIP-2 model for image captioning
BLIP_MODEL = "Salesforce/blip-image-captioning-base"
blip_processor = BlipProcessor.from_pretrained(BLIP_MODEL)
blip_model = BlipForConditionalGeneration.from_pretrained(BLIP_MODEL, torch_dtype=torch.float16, device_map="auto")

def get_mistral_response(input_text):
    inputs = processor(input_text, return_tensors="pt").to("cuda")
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=300)
    return processor.decode(output[0], skip_special_tokens=True)

def generate_image_caption(image):
    inputs = blip_processor(images=image, return_tensors="pt").to("cuda")
    with torch.no_grad():
        caption = blip_model.generate(**inputs)
    return blip_processor.decode(caption[0], skip_special_tokens=True)

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        return image
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit app initialization
st.set_page_config(page_title="Calorie Count App")
st.header("Calorie Count App")

input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
image_caption = ""

if uploaded_file is not None:
    image = input_image_setup(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    image_caption = generate_image_caption(image)
    st.write("Image Description:", image_caption)

submit = st.button("Tell me the total calories")

input_prompt = """
You are an expert nutritionist. Analyze the food items from the image and calculate the total calories.
Provide the details of every food item with calorie intake in the following format:

1. Item 1 - no of calories
2. Item 2 - no of calories
----
----
"""

if submit:
    full_prompt = input_prompt + "\n" + image_caption + "\n" + input_text
    response_text = get_mistral_response(full_prompt)
    st.subheader("The Response is")
    st.write(response_text)
