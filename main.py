# Jakim D. Lopez 
# Date: 2025-05-31
# Laboratory Execise 12: Tagalog to English Translator
# Best compatible python version to use: 3.12 below

from googletrans import Translator

translator = Translator()

input_user = input("Enter text: ")

translation = translator.translate(input_user, src='tl', dest='en')

print(f"Translated text: {translation.text}")