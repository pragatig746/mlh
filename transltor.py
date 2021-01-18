pip install googletrans

from googletrans import Translator

sentence = str(input("say......."))

import googletrans
print(googletrans.LANGUAGES)

translator = Translator()
translation = translator.translate(sentence, dest='bn',src='en')
print(translation.text)
translator.translate(sentence, dest='ja')
