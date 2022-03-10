# This module includes functions for integration with Google's translation API

from googletrans import Translator

def transcribe(source_text,source_lang,convert_to='en'):
	translator = Translator(service_urls=['translate.googleapis.com'])
	result = translator.translate(source_text, src = source_lang, dest = convert_to)
	return result


#output = transcribe('Mikä on nimesi','fi','en')
#print("Input text: Mikä on nimesi , Language: Finnish")
#print("Output text",output.text)