import speech_recognition as sr
import pyttsx3 as txt

listener = sr.Recognizer()
engine = txt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


engine.say('I am HSBC Chat bot')
engine.say('How can i help you?')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


try:
    with sr.Microphone() as source:
        print('listning...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
        command = command.lower()
        if 'hsbc' in command:
            engine.say('mai pagal hu! hahahahahahahahah')
            talk(command)
except:
    pass