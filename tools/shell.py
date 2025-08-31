import speech_recognition as sr
import pyttsx3
import os
import operator
import pyautogui
import webbrowser
import time
from langchain_community.tools import ShellTool
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ================= INIT =================
parser = StrOutputParser()
load_dotenv()
model = ChatOpenAI()
shell = ShellTool()

prompt = PromptTemplate(
    template=(
        "You are Jarvis, my friendly AI assistant. "
        "Respond like we are having a natural conversation. "
        "Keep it short, casual, and warm. "
        "Always end with a follow-up question.\n\n"
        "User: {ques}\nJarvis:"
    ),
    input_variables=['ques']
)

# ================= SPEAK =================
def speak(text):
    print(f"🗣️ Jarvis: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# ================= CALCULATION =================
def calculate_expression(expr: str):
    ops = {
        "plus": operator.add,
        "add": operator.add,
        "minus": operator.sub,
        "subtract": operator.sub,
        "times": operator.mul,
        "multiply": operator.mul,
        "divided": operator.truediv,
        "divide": operator.truediv
    }
    expr = expr.lower().replace("by", "")
    tokens = expr.split()
    numbers = [int(s) for s in tokens if s.isdigit()]
    for word in tokens:
        if word in ops:
            op = ops[word]
            if len(numbers) >= 2:
                return op(numbers[0], numbers[1])
    return None

# ================= WINDOWS CONTROL =================
def take_screenshot():
    filename = "screenshot.png"
    pyautogui.screenshot(filename)
    speak("Screenshot taken and saved as screenshot.png")

def adjust_brightness(increase=True):
    # Brightness can’t be controlled natively with Python on all PCs → using shortcut keys
    if increase:
        for _ in range(5):  # increase 5 steps
            pyautogui.press("brightnessup")
        speak("Brightness increased.")
    else:
        for _ in range(5):  # decrease 5 steps
            pyautogui.press("brightnessdown")
        speak("Brightness decreased.")

def adjust_volume(up=True):
    if up:
        for _ in range(5):
            pyautogui.press("volumeup")
        speak("Volume increased.")
    else:
        for _ in range(5):
            pyautogui.press("volumedown")
        speak("Volume decreased.")

# ================= BROWSER AUTOMATION =================
def search_browser(query):
    speak(f"Searching for {query} in your browser.")
    webbrowser.open(f"https://www.google.com/search?q={query}")
    time.sleep(3)

def open_youtube_and_play(song):
    speak(f"Playing {song} on YouTube.")
    webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
    time.sleep(5)
    pyautogui.moveTo(1500, 1500)  # approximate first video position
    pyautogui.click()
    time.sleep(2)

# ================= MAIN LOOP =================
print("🤖 Jarvis is online. Say 'stop jarvis' to quit.\n")
speak("Jarvis at your service, sir.")

while True:
    try:
        with sr.Microphone() as source:
            print("🎙️ Listening...")
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=8)

        command = recognizer.recognize_google(audio)  # type: ignore
        print(f"👉 You said: {command}")
        cmd = command.lower()

        # -------- SYSTEM COMMANDS --------
        if "open cv" in cmd:
            speak("Opening your CV, sir.")
            shell.invoke('''start "" "C:/Users/divya/OneDrive/Documents/anushka_cv_new.pdf"''')

        elif "open notepad" in cmd:
            speak("Opening Notepad.")
            shell.invoke("notepad.exe")

        elif "close notepad" in cmd:
            speak("Closing Notepad.")
            shell.invoke("taskkill /im notepad.exe /f")

        elif "open calculator" in cmd:
            speak("Opening Calculator.")
            shell.invoke("calc.exe")

        elif "close calculator" in cmd:
            speak("Closing Calculator.")
            shell.invoke("taskkill /im Calculator.exe /f")

        elif "open camera" in cmd:
            speak("Opening Camera.")
            shell.invoke("start microsoft.windows.camera:")

        elif "close camera" in cmd:
            speak("Closing Camera.")
            shell.invoke("taskkill /im WindowsCamera.exe /f")

        elif "open browser" in cmd:
            speak("Opening Microsoft Edge.")
            shell.invoke("start msedge")

        elif "close browser" in cmd:
            speak("Closing Browser.")
            shell.invoke("taskkill /im msedge.exe /f")

        elif "open command prompt" in cmd or "open terminal" in cmd:
            speak("Opening Command Prompt.")
            shell.invoke("start cmd")

        elif "screenshot" in cmd or "screen shot" in cmd:
            take_screenshot()

        elif "increase brightness" in cmd:
            adjust_brightness(increase=True)

        elif "decrease brightness" in cmd:
            adjust_brightness(increase=False)

        elif "increase volume" in cmd:
            adjust_volume(up=True)

        elif "decrease volume" in cmd:
            adjust_volume(up=False)

        elif "shutdown" in cmd:
            speak("Shutting down your system.")
            shell.invoke("shutdown /s /t 1")

        elif "stop" in cmd:
            speak("Goodbye sir, shutting down.")
            break

        # -------- CALCULATIONS --------
        elif any(x in cmd for x in ["plus", "minus", "times", "multiply", "divide"]):
            result = calculate_expression(command)
            if result is not None:
                speak(f"The result is {result}")
                print(f"🧮 Result: {result}")
            else:
                speak("Sorry, I couldn't calculate that.")

        # -------- BROWSER TASKS --------
        elif "search" in cmd and "browser" in cmd:
            query = cmd.replace("search", "").replace("in browser", "").strip()
            search_browser(query)

        elif "search youtube" in cmd:
            query = cmd.replace("search youtube for", "").replace("search youtube", "").strip()
            open_youtube_and_play(query)

        elif "play" in cmd and "youtube" in cmd:
            song = cmd.replace("play", "").replace("on youtube", "").strip()
            open_youtube_and_play(song)

        # -------- CHAT FALLBACK --------
        else:
            chain = prompt | model | parser
            result = chain.invoke({'ques': command})
            print(result)
            speak(result)

    except sr.WaitTimeoutError:
        speak("No input detected for 10 seconds. Goodbye.")
        break
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
    except Exception as e:
        print(f"⚠️ Error: {e}")
        speak("Something went wrong.")
