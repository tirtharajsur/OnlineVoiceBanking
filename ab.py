import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening")
    audio = r.listen(source)

    text = r.recognize_google(audio)
    print(text)
