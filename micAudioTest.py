import pyautogui
import time
import speech_recognition as sr
from threading import Thread

scrolling = False  # Flag to control scrolling

# Function to continuously scroll
def auto_scroll():
    global scrolling
    while True:
        if scrolling:
            pyautogui.scroll(-40)  # Scroll down
            time.sleep(0.2)  # Adjust scroll speed

# Function to recognize voice commands
def listen_for_commands():
    global scrolling
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)  # Calibrate the recognizer

    while True:
        with mic as source:
            print("Listening for commands...")
            audio = recognizer.listen(source)
            print("Recognizing...")

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"Command recognized: {command}")

            if "scroll" in command:
                scrolling = True
                print("Scrolling started...")

            elif "stop" in command:
                scrolling = False
                print("Scrolling stopped...")

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            print(f"Error with the recognition service: {e}")

# Start scrolling in a separate thread
scroll_thread = Thread(target=auto_scroll)
scroll_thread.daemon = True
scroll_thread.start()

# Start listening for voice commands
listen_for_commands()