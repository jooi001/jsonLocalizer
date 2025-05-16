# Translator App

## Overview
This project is a simple localization tool that uses a pre-trained translation model from the `transformers` library and a user interface built with `Gradio`. It translates English text into Japanese using the `Helsinki-NLP/opus-tatoeba-en-ja` model.

## Tools and Languages
- **Python**: The programming language used for the project.
- **Transformers**: A library by Hugging Face for natural language processing tasks.
- **Gradio**: A Python library for creating user interfaces.

## How to Run the Program

1. **Install Dependencies**
   Make sure you have Python installed on your system. Then, install the required libraries using pip:
   ```bash
   pip install gradio transformers
   ```

2. **Run the Application**
   Execute the Python script to start the Gradio interface:
   ```bash
   python localization_app.py
   ```

3. **Access the Interface**
   After running the script, a local URL will be displayed in the terminal. Open this URL in your web browser to access the translation interface.

## Usage
- Enter English text in the provided textbox.
- Click the "Submit" button to translate the text into Japanese.
- The translated text will appear below the textbox.

## Example
Input:
```
I love programming!
```
Output:
```
プログラミングが大好きです！
```
