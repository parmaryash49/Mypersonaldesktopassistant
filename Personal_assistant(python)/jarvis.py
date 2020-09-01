import smtplib
import pyttsx3 
import os
import datetime
import random
import speech_recognition as sr
import wikipedia
import webbrowser
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour==0 and hour<12:
        speak('good morning')
    elif hour >=12 and hour <18:
        speak('good afternoon')
    else:
        speak("good evening")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1.5
        r.energy_threshold = 400
        audio=r.listen(source)
    
    try:
        print("Recoginze...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    
    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query

def  sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    speak("hello yash")
    wishme()
    # while True:
    if 1:
        query=takecommand().lower()

        #my logic for tasks...
        if "wikipedia" in query:
            speak("searching wikipedia.....")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=4)
            speak("According to wikipedia")
            print(result)
            speak(result)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open game' in query:
            print("hello data....")
            music='F:\\DATA STRUCTURE'
            songs=os.listdir(music)
            # print(songs)
            ran_num=random.randint(0,15)
            print("songs \n")
            os.startfile(os.path.join(music,songs[ran_num]))
        
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"sir,the time is {strtime}")

        elif 'open visual studio' in query:
            path="C:\\Users\\Administrator\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'email to yash' in query:
            try:
                speak("what should  i say")
                content=takecommand()
                to="yashparamar124@gmail.com"
                sendEmail(to,contact)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry i'm not able to send you email..")