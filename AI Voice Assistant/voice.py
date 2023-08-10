#pip install pyttsx3
#pip install speechrecognition
#pip install pyaudio
import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audiovoice):
    #engine.say('Hello Dear')
    print(audiovoice)
    engine.say(audiovoice)
    engine.runAndWait()

def greet():
    hour=int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour<11:
        speak('Good Morning Sir')
    elif hour>=11 and hour<15:
        speak('Good Afternoon Sir')
    elif hour>=15 and hour<24:
        speak('Good Evening Sir')
    speak('I am Your AI Assistant')

def askname():
    speak('Can I know your good Name Sir?')
    name=takevoicecommand()
    speak('Welcome '+name)
    speak('How Can I help You Sir')

def takevoicecommand():
    r=sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        try:
            audio=r.listen(source,timeout=30,phrase_time_limit=10)
            print("Compiling your voice please wait..")
            text=r.recognize_google(audio,language='en-in')
            print(text)
        except Exception as e:
            speak('Unable to recognize your voice , Can u repeat once')
        return text
    
#speak('my audio voice')

if __name__=='__main__':
    greet()
    askname()
    while True:
        work=takevoicecommand().lower()
        if 'how are you' in work:
            speak('I am fine. Thank You')
            speak('How are You Sir?')
        elif 'fine' in work or 'good' in work:
            speak('It is good to know that you are fine')

        elif 'Yes' in work or 'Yea' in work:
            speak('Wow great job sir and All the best')

        elif 'My faculty' in work or 'Subject faculty' in work:
            speak('Your Subject Faculty is PC Karthik')

        elif 'project' in work:
            path="C:\\Kalyan Reddy ( All Photos )\\AI Project"
            os.startfile(path)

        elif 'my folder' in work:
            path="C:\\Kalyan Reddy ( All Photos )"
            os.startfile(path)    

        elif 'open chrome' in work:
            url="techsrijan.com"
            chrome_path='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
        elif 'close chrome' in work:
            os.system("TASKKILL /F /IM chrome.exe")

        elif 'bye' in work:
            speak('bye Sir..Have a good day')
            exit()
        else:
            speak('I cant understand Please repeat again')