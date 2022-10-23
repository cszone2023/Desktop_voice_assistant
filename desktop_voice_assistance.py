import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('lahane493@gmail.com', 'rhtcnmozzbaknamq')
    server.sendmail('lahane493@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            webbrowser.open("https://www.wikipedia.org/")
                                                                                        # speak('Searching Wikipedia...')
                                                                                        # results = wikipedia.summary(query, sentences=2)
                                                                                        # speak("According to Wikipedia")
                                                                                        # print(results)
                                                                                        # speak(results)

        elif 'youtube' in query:
            webbrowser.open("http://www.youtube.com")

        elif 'google' in query:
            webbrowser.open("http://www.google.com")

        elif 'stackoverflow' in query:
            webbrowser.open("http://www.stackoverflow.com")   

        elif 'gfg' in query:
            webbrowser.open_new_tab("https://www.geeksforgeeks.org/")

        elif 'movie' in query:
            music_dir = 'F:\movies'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "G:"
            os.startfile(codePath)

        elif 'send email to shubham' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "lahane493@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend shubham. I am not able to send this email")    
        