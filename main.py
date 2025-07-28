import speech_recognition as sr
import os
import webbrowser
import openai
import datetime


def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language="en-in" )
            print(f"User said:{query}")
            return query
        except Exception as e :
            return "Some error occured. Sorry from Jarvis"

if __name__ == '__main__':
    print('Pycharm')
    say("Hello I am Jarivs A.I")
    while True:
        print("Listening.......")
        query = takeCommand()
        sites = [["youtube","https://www.youtube.com"],["Wikipedia","https://www.wikipidea.com"],["Google","https://www.google.com"],["anime","https://hianime.to/watch/dandadan-19319?ep=130592"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir  ......")
                webbrowser.open(site[1])

        if "play music" in query :
            musicPath = "/Users/abhijithmr/Downloads/Old Money AP Dhillon.mp3"
            import subprocess , sys

            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener,musicPath])

        if "the time" in query :
            musicPath = "/Users/abhijithmr/Downloads/Old Money AP Dhillon.mp3"
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strfTime}")

        if "open camera".lower()  in query :
            os.system(f"open /System/Applications/FaceTime.app")

        say(query)
        #if(query =='stop'):
          #  break

