# Calorie Count App

## Overview
The **Calorie Count App** is a Streamlit-based application that utilizes AI models to analyze food images and estimate their total calorie content. It leverages:
- **BLIP-2** for image captioning (extracting food item details from images)
- **Mistral 7B** for natural language processing (interpreting image descriptions and estimating calorie content)

## Features
- Upload an image containing food items.
- AI extracts a textual description of the food items.
- AI estimates the total calorie content of the food.
- Displays detailed calorie breakdown per item.

## Technologies Used
- **Python**
- **Streamlit** (for UI)
- **Transformers (Hugging Face)** (for AI model inference)
- **BLIP-2** (for image captioning)
- **Mistral 7B** (for NLP-based calorie estimation)
- **Torch** (for model execution)
- **PIL (Pillow)** (for image processing)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/calorie-count-app.git
   cd calorie-count-app
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the project directory.
   - Add API keys (if needed) and configurations.

4. Run the application:
   ```sh
   streamlit run app.py
   ```

## Usage
1. Upload an image containing food items.
2. The AI model processes the image and generates a description.
3. The calorie estimation model provides a breakdown of the total calories.
4. View the results displayed on the Streamlit interface.

## Requirements
Ensure you have the following dependencies installed (also in `requirements.txt`):
```
torch
transformers
streamlit
dotenv
Pillow
```

## Future Enhancements
- Improve food recognition accuracy using specialized food datasets.
- Integrate a database for storing food calorie information.
- Add a meal planning feature based on calorie intake.

## License
This project is licensed under the MIT License.

---

### Authors & Acknowledgements
- **Developed by:** [Your Name]
- Special thanks to Hugging Face for providing pre-trained models.
