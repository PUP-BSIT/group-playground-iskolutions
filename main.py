# Jakim D. Lopez 
# Date: 2025-05-31
# Laboratory Execise 12: Tagalog to English Translator
# Best compatible python version to use: 3.12 below

from googletrans import Translator

def translate_tagalog(text):
    translator = Translator()
    translation = translator.translate(text, dest='en')

    return translation.text

text = input("Enter text in Tagalog: ")
print(f"Translated text: {translate_tagalog(text)}")