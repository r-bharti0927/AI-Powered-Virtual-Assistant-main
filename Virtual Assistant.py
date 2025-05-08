import speech_recognition as sr
import pyttsx3
import pywhatkit 
import datetime
import wikipedia

listener = sr.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    instruction = ""
    try:
        with sr.Microphone() as origin:
            print("Listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace("jarvis", "").strip()
                print("Instruction:", instruction)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Could not request results. Please check your internet connection.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return instruction

def play_jarvis():
    instruction = input_instruction()
    print("Heard:", instruction)

    if "play" in instruction:
        song = instruction.replace("play", "").strip()
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif "time" in instruction:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk("Current time is " + current_time)

    elif "date" in instruction:
        current_date = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Today's date is " + current_date)

    elif "how are you" in instruction:
        talk("I am fine, how about you?")

    elif "what is your name" in instruction:
        talk("I am Jarvis. What can I do for you?")

    elif "who is" in instruction:
        human = instruction.replace("who is", "").strip()
        try:
            info = wikipedia.summary(human, 1)
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError:
            talk("That is too ambiguous. Can you be more specific?")
        except wikipedia.exceptions.PageError:
            talk("I couldn't find any information on that.")
        except Exception as e:
            talk("Sorry, I encountered a problem.")
            print(f"Wikipedia error: {e}")

    else:
        talk("Please repeat your instruction.")

# Start the assistant
play_jarvis()
