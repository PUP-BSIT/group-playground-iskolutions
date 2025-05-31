from googletrans import Translator

def translate_tagalog(text):
        translator = Translator()
        translated = translator.translate(text, dest='en')
        return translated.text

tagalog_text = input("Enter text: ")

english_text = translate_tagalog(tagalog_text)

print(f"Translated text: {english_text}")