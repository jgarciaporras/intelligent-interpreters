# This module includes function for integrating Google's Translator API

from googletrans import Translator


def get_source_language(source_language):
     
    Dict = {'de-DE':'de',
            'en-US':'en',
            'es-ES':'es'
         }
    
    return (Dict[source_language])


def translate(source_text, source_lang, lang):
	translator = Translator(service_urls=['translate.googleapis.com'])
	result = translator.translate(source_text, src = source_lang, dest = lang)
	return result
