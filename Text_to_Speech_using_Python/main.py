from gtts import gTTS
import os

mytext = input("Enter your text that you want to hear: ")

language = 'en'

output = gTTS(text=mytext,lang=language,slow=False)

output.save("speech.mp3")
os.system("start speech.mp3")