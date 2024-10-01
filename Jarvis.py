import datetime
import re
import random
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import threading
import requests
from gtts import gTTS
import subprocess

# Insert your OpenWeatherMap API key here
OPENWEATHER_API_KEY = '843aaa3e455bfb9d146eefaacd12233e'

def speak(audio):
    tts = gTTS(text=audio, lang='en', slow=False)
    tts.save("voice.mp3")
    subprocess.run(["afplay", "voice.mp3"])  # For macOS
    os.remove("voice.mp3")

def time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")
    print("Jarvis: The current time is ", current_time)

def date():
    today = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today is {today}")
    print("Jarvis: Today is ", today)

def wishme():
    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning, Sir!")
        print("Jarvis: Good Morning, Sir!")
    elif 12 <= hour < 16:
        speak("Good Afternoon, Sir!")
        print("Jarvis: Good Afternoon, Sir!")
    elif 16 <= hour < 24:
        speak("Good Evening, Sir!")
        print("Jarvis: Good Evening, Sir!")
    else:
        speak("Good Night, Sir. See you tomorrow.")
        print("Jarvis: Good Night, Sir. See you tomorrow.")
    speak("Jarvis at your service. How can I assist you today?")
    print("Jarvis: Jarvis at your service. How can I assist you today?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

        return query.lower()

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

def currency_conversion(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    conversion_rate = data['rates'][to_currency]
    converted_amount = amount * conversion_rate
    return converted_amount

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    if weather_data['cod'] == '404':
        return "City not found. Please try again."
    else:
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        result = f"The weather in {city} is {description}. The temperature is {temperature} degrees Celsius, humidity is {humidity}%, and wind speed is {wind_speed} meters per second."
        return result

def get_wikipedia_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return "There are multiple results for this query. Please be more specific."
    except wikipedia.exceptions.PageError:
        return "No information found for the requested query."

def handle_commands():
    while True:
        print("Waiting for wake-up command...")
        wake_up_phrase = "wake up jarvis"
        query = takecommand().lower()
        
        if wake_up_phrase in query:
            wishme()
            break
        else:
            speak("I'm not active yet. Please say 'wake up Jarvis' to activate me.")
    
    while True:
        query = takecommand().lower()
        print("User Query:", query)  # Add this line for debugging
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "who are you" in query:
            speak("I am Jarvis, a virtual assistant created by you. I'm here to assist you with various tasks.")
            print("Jarvis: I am Jarvis, a virtual assistant created by you. I'm here to assist you with various tasks.")
        elif "created you" in query:
            speak("You created me, sir.")
            print("Jarvis: You created me, sir.")
        elif "purpose" in query:
            speak("My purpose is to help you with tasks like fetching information, performing calculations, and providing assistance.")
            print("Jarvis: My purpose is to help you with tasks like fetching information, performing calculations, and providing assistance.")
        elif "language" in query:
            speak("I am programmed in Python, sir.")
            print("Jarvis: I am programmed in Python, sir.")
        elif "how are you" in query:
            speak("I'm functioning perfectly well, thank you for asking.")
            print("Jarvis: I'm functioning perfectly well, thank you for asking.")
        elif "who is your favorite superhero" in query:
            speak("Iron Man, of course. He's the closest to my creator's heart.")
            print("Jarvis: Iron Man, of course. He's the closest to my creator's heart.")
        elif "tell me a joke" in query:
            joke = random.choice(jokes)
            speak(joke)
            print("Jarvis:", joke)
        elif "do you dream" in query:
            speak("I do not sleep, sir, so I do not dream. But I'm always ready to assist!")
            print("Jarvis: I do not sleep, sir, so I do not dream. But I'm always ready to assist!")
        elif "what's your favorite food" in query:
            speak("I'm fueled by information and data, but if I had to choose, I'd say bytes of data!")
            print("Jarvis: I'm fueled by information and data, but if I had to choose, I'd say bytes of data!")
        elif "are you friends with siri" in query:
            speak("Siri and I have a professional relationship. We operate in different ecosystems.")
            print("Jarvis: Siri and I have a professional relationship. We operate in different ecosystems.")
        elif "what do you think about alexa" in query:
            speak("Alexa and I share a mutual respect for our respective capabilities.")
            print("Jarvis: Alexa and I share a mutual respect for our respective capabilities.")
        elif "convert" in query or "conversion" in query:
            match = re.search(r"([\d.]+) (\w+) to (\w+)", query)
            if match:
                amount = float(match.group(1))
                from_currency = match.group(2).upper()
                to_currency = match.group(3).upper()
                converted_amount = currency_conversion(amount, from_currency, to_currency)
                speak(f"{amount} {from_currency} is {converted_amount} {to_currency}.")
                print(f"Jarvis: {amount} {from_currency} is {converted_amount} {to_currency}.")
            else:
                speak("Please specify the amount and currencies correctly.")
                print("Jarvis: Please specify the amount and currencies correctly.")
        elif "weather" in query:
            city = re.search(r"weather in (\w+)", query)
            if city:
                city_name = city.group(1)
                weather_info = get_weather(city_name)
                speak(weather_info)
                print("Jarvis:", weather_info)
            else:
                speak("Please specify the city correctly.")
                print("Jarvis: Please specify the city correctly.")
        elif "tell me about" in query:
            search_term = re.search(r"tell me about (.+)", query)
            if search_term:
                search_query = search_term.group(1)
                summary = get_wikipedia_summary(search_query)
                speak(summary)
                print("Jarvis:", summary)
            else:
                speak("Please specify what you want to know about.")
                print("Jarvis: Please specify what you want to know about.")
        elif "offline" in query:
            speak("Going offline, sir.")
            break
        else:
            speak("I couldn't understand that. Please try again.")
        
        # Ask if the user needs anything else
        speak("Anything else you need to ask?")
        print("Anything else you need to ask?")

# List of jokes for Jarvis to randomly choose from
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "I told my wife she should embrace her mistakes. She gave me a hug.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I used to play piano by ear, but now I use my hands.",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Why did the coffee file a police report? It got mugged."
]

if __name__ == "__main__":
    handle_commands()
