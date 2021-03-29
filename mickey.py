import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import os

BOSS = "KingsMan"
print("Initialising Mickey...")

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate', 125 )
    engine.setProperty('volume',1.0)
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning" + BOSS) 
    elif hour>=12 and hour<18:
        speak("Good Afternoon" + BOSS)    
    else:
        speak("Good Evening" + BOSS)  
    speak("I am Mickey. How can I help you ?")      

def listenCommand():
    command=0
    hear = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = hear.listen(source)

    try:
        print("Recognizing...")
        command = hear.recognize_google(audio, language='en-in')
        print(f'{BOSS} : {command}\n')

    except:
            pass

    return command


speak("Initialising Mickey..........")
wishMe()

def main():
    command = listenCommand()
    command=str(command).lower()

    if ('who is' in command) or ('what is' in command):
        speak('Searching Wikipedia...')
        command = command.replace("who is","")
        command = command.replace("what is","")
        results = wikipedia.summary(command, sentences = 1)
        print("Mickey:",results)
        return speak(results)

    elif 'play' in command:
        speak('Playing...')
        command = command.replace('play','')
        print(command)
        return pywhatkit.playonyt(command)

    elif 'google' in command:
        speak("Googling...")
        command = command.replace('google','')
        print(command)
        return pywhatkit.search(command)
       
    elif 'open visual studio' in command: 
        speak("Opening...")
        return os.system("code")
    
    elif 'stop mickey' in command:
        speak("Suiciding...")
        return exit()
        
    else:
        return 0

while True:
    main()
    
    