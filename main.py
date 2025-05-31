from googletrans import Translator
import asyncio

def translate_tagalog(text):
    async def do_translate():
        translator = Translator()
        translated = await translator.translate(text, dest='en')
        return translated.text
    
    return asyncio.run(do_translate())