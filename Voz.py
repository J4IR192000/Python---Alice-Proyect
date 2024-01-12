import speech_recognition as SR #pip install SpeechRecognition
import pyttsx3 #pip install pyttsx3
import pywhatkit #pip install pywhatkit 
import datetime #pip install datetime 
import wikipedia #pip install wikipedia
#pip install flask

name = 'alicia'
key= 'AIzaSyDdWRclKXleOrcmC1Kg4n5WMkLikCAQIk0'
listener = SR.Recognizer ()
engine = pyttsx3.init()

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def talk (text):
    engine.say (text)
    engine.runAndWait() 

def listen ():
    try:
         with SR.Microphone() as Source:
             print("Te Escucho!...")
             voice=listener.listen(Source)
             rec = listener.recognize_google(voice)
             rec = rec.lower()
             if name in rec:
                 rec = rec.replace(name,'')
                 print(rec)
    except:
        pass
    return rec

def run():
    rec = listen()
    if 'reproduce' in rec :
        musica = rec.replace('reproduce','')
        talk('reproduciendo ahora '+musica)
        pywhatkit.playonyt(musica)

    elif 'hora' in rec:
        hora= datetime.datetime.now().strftime('&H:%M')
        talk("son las "+hora)

    elif 'encuentro' in rec:
        order = rec.replace('encuentro','')
        info = wikipedia.summary(order,1)
        talk(info)
run()