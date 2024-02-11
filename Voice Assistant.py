import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyjokes
import requests
import json

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("How can I assist you today?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't understand what you said. Can you please repeat?")
        return "None"
    return query

def main():
    wish_me()
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'weather' in query:
            api_key = "your_api_key"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("Which city's weather would you like to know?")
            city_name = take_command().lower()
            complete_url = f"{base_url}appid={api_key}&q={city_name}"
            response = requests.get(complete_url)
            data = response.json()
            if data["cod"] != "404":
                weather_description = data["weather"][0]["description"]
                temperature = round(data["main"]["temp"] - 273.15, 2)  # Converting Kelvin to Celsius
                speak(f"The weather in {city_name.title()} is {weather_description} with a temperature of {temperature} degrees Celsius.")
            else:
                speak("City not found. Please try again.")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'search' in query:
            speak("What would you like me to search for?")
            search_query = take_command().lower()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
