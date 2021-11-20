import speech_recognition as sr

r = sr.Recognizer()


def record_audio():
    with sr.Microphone() as source:
        print(' Say Something')
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print('Sorry, I did not get that')
        except sr.RequestError:
            print(' Sorry, my speech service is down ')
        return voice_data


def respond(voice_data):
    if 'What is your name' in voice_data:
        print(' My Name is HSBC Technology')


print('how can i help you? ')
voice_data = record_audio()
respond(voice_data)