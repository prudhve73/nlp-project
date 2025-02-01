import speech_recognition as sr
import os
import time
from gtts import gTTS
import pygame

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Could not request results, please check your internet connection.")
            return None

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    filename = "response.mp3"
    tts.save(filename)
    time.sleep(1)  # Ensure file is saved properly before playing
    
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Wait until playback finishes
        time.sleep(0.5)
    
    pygame.mixer.quit()
    try:
        os.remove(filename)
    except PermissionError:
        print("Error: Unable to delete the file. It might still be in use.")

def main():
    print("Chat-to-Voice AI is running. Say 'exit' to stop.")
    while True:
        user_input = recognize_speech()
        if user_input:
            if user_input.lower() == "exit":
                print("Exiting...")
                break
            text_to_speech(user_input)

if __name__ == "__main__":
    main()
