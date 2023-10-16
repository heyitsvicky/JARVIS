import requests
from online_fns import get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, find_my_ip
import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime
from random import choice
from responses import opening_text
from pprint import pprint


USERNAME = config('USER')
BOTNAME = config('BOTNAME')


engine = pyttsx3.init('nsss')

# Set Rate
engine.setProperty('rate', 230)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Male)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()


# Greet the user
def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")


# Takes Input from User
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen miss.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, miss?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen miss.")
            print(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, miss?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, miss?')
            query = take_user_input().lower()
            search_on_google(query)

        elif "send an email" in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject miss?")
            subject = take_user_input().capitalize()
            speak("What is the message miss?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email miss.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs miss.")

        elif 'joke' in query:
            speak(f"Hope you like this one miss")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen miss.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, miss")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen miss.")
            pprint(advice)

        elif "trending movies" in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen miss.")
            print(*get_trending_movies(), sep='\n')

        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, miss")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen miss.")
            print(*get_latest_news(), sep='\n')

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")