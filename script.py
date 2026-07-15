import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

# Initialize voice engine
engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Male voice


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def wish_me():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Hi there, Good Morning Jayram Sir. What can I help you?")
    elif 12 <= hour < 16:
        speak("Hi there, Good Afternoon Jayram Sir. What can I help you?")
    else:
        speak("Hi there, Good Evening Jayram Sir. What can I help you?")


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""

    except sr.RequestError:
        speak("Internet connection is required.")
        return ""


def take_command(message):

    if "hello" in message or "hey" in message:
        speak("Hello Sir, what can I help you?")

    elif "who are you" in message:
        speak("I am a virtual assistant created by Jayram Sir.")

    elif "open youtube" in message:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open google" in message:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open facebook" in message:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif "open instagram" in message:
        speak("Opening Instagram")
        webbrowser.open("https://instagram.com")

    elif "open whatsapp" in message:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")

    elif "open calculator" in message:
        speak("Opening Calculator")
        os.system("calc")   # Windows only

    elif "time" in message:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "date" in message:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}")

    elif "exit" in message or "stop" in message:
        speak("Goodbye Sir.")
        exit()

    else:
        query = message.replace("maya", "")
        speak(f"This is what I found on the internet regarding {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")


# Main Program
wish_me()

while True:
    command = listen()

    if command:
        take_command(command)
