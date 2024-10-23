from googletrans import Translator
import ssl
import requests

requests.packages.urllib3.disable_warnings()    

def translator(text):

    translator = Translator()
    context = ssl._create_unverified_context()
    translated = translator.translate(text, dest='en')

    return translated.text # Output: "Example title"
