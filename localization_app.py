import gradio as gr # UI Library
from transformers import pipeline # Transformer Pipeline

# Initialize translation pipeline
translation_pipeline_ENJP = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ja")
# translation_pipeline_ENZH = pipeline("translation_en_to_zh")
# translation_pipeline_JPEN = pipeline("translation_jp_to_en")
# translation_pipeline_JPZH = pipeline("translation_jp_to_zh")
# translation_pipeline_ZHEN = pipeline("translation_zh_to_en")
# translation_pipeline_ZHJP = pipeline("translation_zh_to_jp")

# Pass through text
results = translation_pipeline_ENJP('I love programming!')
# results1 = translation_pipeline_ENZH('I love programming!')


# Extract result
results[0]['translation_text']

# Create Gradio Function and Interface
def translate_transformers(from_text):
    results = results.translation_pipeline(from_text) # store translated results
    return results[0]['translation_text'] # return extracted results

translate_transformers('I love ice cream')
print(translation_pipeline_ENJP("I love programming!")[0]['translation_text'])