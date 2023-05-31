import pyttsx3
engine = pyttsx3.init()
text = str(input('Entrez le text : '))
engine.say(text)
engine.runAndWait()