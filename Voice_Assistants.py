import speech_recognition as sr
import win32com.client
import webbrowser
import openai
import os

speaker = win32com.client.Dispatch("SAPI.SpVoice")

# while 1:
#     print("Enter the word you want you speak it out by computer ")
#     s= input()
def say(text):
    speaker.Speak(f"say{text}")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language ="en-in")
            print(f"User said:{query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry form Jarvis"
        
        
        
            
if __name__ == '__main__':
    print('Assistanst')
    say("Hello I am Jarvis A.I")  
    while True: 
        print("Listening....")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],
                 [ "google","https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir....")
                webbrowser.open(site[1])
            if "open music" in query:
                music_player_path = r"C:/Users/Lenovo/Downloads/perfect-beauty-191271.mp3" # Adjust the path as needed
                os.system(f"{music_player_path}")
        # say(query)
        