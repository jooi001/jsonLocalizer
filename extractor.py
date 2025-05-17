import json # Import JSON
from transformers import pipeline # Transformer Pipeline

# Initialize translation pipeline
translation_pipeline_ENJP = (pipeline("translation", model="Helsinki-NLP/opus-tatoeba-en-ja"))

# Translate string from JSON file helper function
def translate_strings(json_data):
    strings_list = []
    for key, value in json_data.items():
        if isinstance(value, str):
            result = translation_pipeline_ENJP(value)
            json_data[key] = result[0]['translation_text']
        elif isinstance(value, dict):
            translate_strings(value)

# Load source file in read mode
with open('./source/en.json', 'r', encoding='utf-8') as infile:
    data = json.load(infile)
    translate_strings(data)

# Write to JSON file
with open('./source/translations.json', 'w', encoding='utf-8') as outfile:
    writer = json.dump(data, outfile, ensure_ascii=False, indent=2)