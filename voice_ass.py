import speech_recognition
import pyttsx3
import datetime
import webbrowser

recognizer = speech_recognition.Recognizer()


def speak(text):
    print(f"Assistant: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


with speech_recognition.Microphone() as mic:
    recognizer.adjust_for_ambient_noise(mic, duration=0.2)

    speak("Hello! Welcome to Jisan's personal Voice Assistant. How can I help you today...")

    while True:
        try:
            print("\nI am listening...")

            audio = recognizer.listen(mic, timeout=15)
            text = recognizer.recognize_google(audio)
            text = text.lower().strip()

            print(f"Recognized: {text}")

            if text == "what is the time":
                current_time = datetime.datetime.now()
                response = "The time is " + current_time.strftime("%I:%M:%S %p")

            elif text == "what is the date":
                today = datetime.datetime.now()
                response = "Today's date is " + today.strftime("%d-%m-%Y")

            elif text == "hello":
                response = "Hello! Welcome to Jisan's personal Voice Assistant...\nHow can I help you today.."

            elif text == "open google":
                webbrowser.open("https://www.google.com")
                response = "Opening Google"

            elif text == "open youtube":
                webbrowser.open("https://www.youtube.com")
                response = "Opening YouTube"

            elif text.startswith("search for"):
                search_query = text.replace("search for", "").strip()

                if search_query:
                    url = "https://www.google.com/search?q=" + search_query
                    webbrowser.open(url)
                    response = "Searching for " + search_query
                else:
                    response = "What would you like me to search for?"

            elif text == "stop":
                speak("GoodBye !! See you again...")
                break

            else:
                response = "You said: " + text

            speak(response)

        except speech_recognition.WaitTimeoutError:
            speak("No response. Goodbye!")
            break

        except speech_recognition.UnknownValueError:
            speak("I could not understand what you said. Please say it again.")

        except speech_recognition.RequestError:
            speak("There is a problem with the speech recognition service.")