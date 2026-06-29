import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty("rate", 170)


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():

    recognizer = sr.Recognizer()

    fs = 44100
    duration = 5

    filename = "voice_input.wav"

    try:
        print("Listening for 5 seconds...")
        speak("Listening")

        recording = sd.rec(
            int(duration * fs),
            samplerate=fs,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        write(filename, fs, recording)

        with sr.AudioFile(filename) as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)

        print("You:", text)

        os.remove(filename)

        return text.lower()

    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand.")
        return ""

    except sr.RequestError:
        speak("Internet connection required.")
        return ""

    except Exception as e:
        print(e)
        speak("Voice recognition failed.")
        return ""

    finally:
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except:
                pass