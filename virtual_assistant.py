import speech_recognition as speechRecognition
import pyttsx3
import pywhatkit 
import datetime
import wikipedia
#from dotenv import load_dotenv
import os
import pyautogui
import time
import subprocess


#load_dotenv()

#client_id = os.getenv("CLIENT_ID")
#client_secret = os.getenv("CLIENT_SECRET")

listener = speechRecognition.Recognizer()


machine = pyttsx3.init()


def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    try:
        talk("listening")
        with speechRecognition.Microphone() as origin:
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction=instruction.lower()
    except:
        pass
    return instruction

def play_sam():
    global instruction
    instruction=''
    #talk("listening")
    while(instruction != 'goodbye'):
        instruction = input_instruction()
        print(instruction)
        if "sam" in instruction or "sem" in instruction:
            instruction = instruction.replace('sam','')
            instruction = instruction.replace('sem','')
            #talk("listening")
            
            print(instruction)
            if "play" in instruction and 'you tube' in instruction:
                song = instruction.replace('play','')
                print('Playing' + song)
                talk("playing" + song)
                pywhatkit.playonyt(song)
                
            elif 'time' in instruction:
                Currenttime = datetime.datetime.now().strftime('%I:%M%p')
                print(Currenttime)
                talk('Current time '+ Currenttime)
                
            elif 'date' in instruction:
                date = datetime.datetime.now().strftime('%d /%m /%Y')
                print(date)
                talk("Today's date is " + date)
                
            elif 'who is' in instruction:
                human = instruction.replace('who is','')
                info = wikipedia.summary(human, 1)
                print(info)
                
                talk(info)
            
            elif 'text' in instruction:
                print('In text condition')
                subprocess.Popen(["cmd", "/C", "start whatsapp://send?phone=+923318110015"], shell=True)
                time.sleep(1)
                for x in range(9):
                    pyautogui.press('tab')
                talk('Say what you want me to send.')
                with speechRecognition.Microphone() as origin:
                    speech = listener.listen(origin)
                    text = listener.recognize_google(speech)
                    text = text.lower()
                pyautogui.write(text)
                pyautogui.press('enter')
            
            elif 'play' in instruction and 'liked songs' in instruction and 'spotify' in instruction:
                os.system('spotify')
                time.sleep(5)
                pyautogui.hotkey('alt','shift','s')
                time.sleep(1)
                for x in range(2):
                    pyautogui.press('tab')
                pyautogui.press('enter')
            
            elif 'toggle' in instruction and 'shuffle' in instruction:
                os.system('spotify')
                time.sleep(5)
                pyautogui.hotkey('ctrl','s')
                
            elif 'goodbye' in instruction or 'good boy' in instruction:
                talk('Goodbye')
                break
                    
            else:
                talk("Please repeat")
    
play_sam()