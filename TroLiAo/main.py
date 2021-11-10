import speech_recognition as sr
from Noi import *
from Nao import *
from temp import *
from datetime import date, datetime
import os
from googlesearch import search

get_weather_data()
ear = sr.Recognizer()
bot_name = "Adam"
global run
run = False
while True:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    speech_rate = 200
    engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate", speech_rate)
    with sr.Microphone() as mic:
        ef()
        audio = ear.record(mic, duration=2.5)

    try:
        you = ear.recognize_google(audio)
    except:
        you = ""
    print("You:", you)
    # Ai Brain
    if you == "":
        brain = "I can't hear you, try again"
    elif "hello" in you:
        brain = "Hello!"
    elif "how are you" in you:
        brain = "I'm fine, almost"
    elif "what make you smile" in you or "what makes you smile" in you:
        brain = "Sadness, suffering and despair"
    elif "I will make you smile" in you:
        brain = "You will never understand me, stupid"
    elif "super Idol" in you:
        brain = "Playing Super Idol..."
        os.startfile("C:\TLA\idol.mp3")
        wait(15)
    elif "today" in you or 'today date' in you:
        today = date.today()
        brain = today.strftime("%B %d, %Y")
    elif 'time' in you or 'now' in you:
        now = datetime.now()
        brain = now.strftime("It's %H:%M")
    elif "start Google" in you or "stock Google" in you or "stop Google" in you:
        brain = "Starting Google..."
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
    elif "bye" in you or "stop" in you or "quit" in you:
        brain = "Bye"
        talk(brain)
        break
    elif "thank you" in you:
        brain = "No problem"
    elif "tell me a joke" in you:
        brain = "Why do bicycle fall over. Because they are two tired."
    elif "song" in you:
        brain = "Playing Good Stuff"
        os.startfile("C:\TLA\good stuff.mp3")
    elif "idle" in you or "idol" in you:
        wait(15)
    elif 'Wiki' in you:
        wiki_search = you.replace('Wiki', '')
        wiki(wiki_search)
        wait(15)
    elif "search" in you:
        gg_search = you.replace('search', '')
        for i in search(gg_search, tld="co.in", num=3, stop=3, pause=2):
            print(i)
        brain = "You can press these URL"
    elif "say" in you:
        say = you.replace("say", '')
        brain = say
    elif "white" in you:
        wait_sec = you.replace("white", "")
        brain = int(wait_sec)
        wait(int(wait_sec))
    elif "weather" in you:
        weather()
        brain = "These are the result"
    else:
        brain = "I can't answer your question because I am too stupid"
    print(bot_name,":", brain)
    talk(brain)

