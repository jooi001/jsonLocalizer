import gradio as gr # UI Library
from transformers import pipeline # Transformer Pipeline

# Initialize translation pipeline
translation_pipeline_ENJP = (pipeline("translation", model="Helsinki-NLP/opus-tatoeba-en-ja"))

# Pass through text
results = translation_pipeline_ENJP('I love programming!')

# Extract result
results[0]['translation_text']

# Create Gradio Function and Interface
def translate_transformers(from_text):
    results = translation_pipeline_ENJP(from_text) # store translated results
    return results[0]['translation_text'] # return extracted results

translate_transformers('I love ice cream')
print(translation_pipeline_ENJP("I love programming!")[0]['translation_text'])

interface = gr.Interface(fn=translate_transformers,
    inputs=gr.Textbox(lines=2, placeholder='Text to translate'),
    outputs='text')

interface.launch()