import pyttsx3
import datetime
import speech_recognition as sr 
import pyaudio
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    if hour>= 0 and hour <12:
        speak("Good Morning!")
    elif hour >=12 and hour <18:
        speak("Good Afternoon!")
    elif hour >=18 and hour <22:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak(" This is Jarvis Sir , Please tell me How may i help you ?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening .....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try: 
        print('Reconginzing....')
        query = r.recognize_google(audio, language = 'en-in')
        print(f'User said : {query}\n')

    except Exception as e:
        print(e)
        print('Say that again please......')
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query , sentences =2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        if 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        # elif 'open geekforgeeks' or 'open geek for geeks 'in query:
        #     webbrowser.open('geekforgeeks.com')
        
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'open instagram' in query:
            webbrowser.open('instagram.com')
         
        elif 'open whats app' in query:
            webbrowser.open('whatsapp.com')

        elif 'open gmail' in query:
            webbrowser.open('gmail.com')
        
        # elif 'open stackoverflow' or 'open stack overflow'in query:
        #     webbrowser.open('stackoverflow.com')


        elif 'play music' in query:
            music_dir = 'D:\\Music\\Music1'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H : %M : %S")
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            VScodePath ="C:\\Users\\himangshu Baruah\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(VScodePath)

        elif 'open code blocks' in query:
            codeblockPath ="C:\\Users\\himangshu Baruah\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\CodeBlocks"
            os.startfile(codeblockPath)


        
