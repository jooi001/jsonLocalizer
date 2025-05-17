import json # Import JSON
from transformers import pipeline # Transformer Pipeline
import os

# Initialize translation pipeline (cache first to avoid reloading)
translation_pipeline_ENJP = None

def get_translation_pipeline():
    global translation_pipeline_ENJP
    if translation_pipeline_ENJP is None:
        translation_pipeline_ENJP = pipeline("translation", model="Helsinki-NLP/opus-tatoeba-en-ja")
    return translation_pipeline_ENJP

# Translate string from JSON file helper function
def translate_strings(json_data):
    strings_list = []
    for key, value in json_data.items():
        if isinstance(value, str):
            result = get_translation_pipeline()(value)
            json_data[key] = result[0]['translation_text']
        elif isinstance(value, dict):
            translate_strings(value)

# Load source file in read mode
def translate_source_file():
    with open('./source/en.json', 'r', encoding='utf-8') as infile:
        data = json.load(infile)
        translate_strings(data)

# Write to JSON file
    with open('./source/translations.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)