import streamlit as st
from googletrans import Translator

# Function to map language names to Google Translate language codes
def get_language_code(language):
    language_codes = {
        "English": "en",
        "French": "fr",
        "German": "de",
        "Latin": "la",
        "Spanish": "es",
        "Hindi": "hi",
        "Tamil": "ta",
        "Telugu": "te",
        "Marathi": "mr"
    }
    return language_codes.get(language, "en")

# Function to translate text
def translate(input_lang, output_lang, text):
    translator = Translator()
    src_lang_code = get_language_code(input_lang)
    dest_lang_code = get_language_code(output_lang)
    result = translator.translate(text, src=src_lang_code, dest=dest_lang_code)
    return result.text

# Streamlit app configuration
st.set_page_config(
    page_title="Translator.AI",
    page_icon="🈶",
    layout="centered"
)

# App title
st.title("🈶 Translator App - GPT-4o")

col1, col2 = st.columns(2)

# Input language selection
with col1:
    input_languages_list = ["English", "French", "German", "Latin", "Spanish", "Hindi", "Tamil", "Telugu", "Marathi"]
    input_language = st.selectbox(label="Input Language", options=input_languages_list)

# Output language selection
with col2:
    output_languages_list = [x for x in input_languages_list if x != input_language]
    output_language = st.selectbox(label="Output Language", options=output_languages_list)

# Text area for user input
input_text = st.text_area("Type the text to be translated")

# Translate button
if st.button("Translate"):
    if input_text.strip() == "":
        st.warning("Please enter some text to translate.")
    else:
        translated_text = translate(input_language, output_language, input_text)
        st.success(translated_text)
