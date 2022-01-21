import pyttsx3
import datetime
import keyboard
import pyautogui
import pywhatkit as pywhatkit
import speech_recognition
import wikipedia
import webbrowser
import os
import Links
from pynput import mouse
from pynput.mouse import Button , Controller
import smtplib
import random
mouse = Controller()

email_contacts = {'cafe' : "mparikhya@gmail.com", 'kushan': 'carchana813@gmail.com', 'khushi': 'shubhi6482@gmail.com', "papa": 'ranvijay4517@gmail.com','kushan gaming' : 'kushan7752@gmail.com'}
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    wish_list = ['16 gb ram rtx 3050 gpu with the power of fire, how may I help you', 'I am Jarvis, How may I help you!','The supreme Jarvis is in your service!, how may i serve you ', 'jarvis here, may i ask you , why you remembered me?']
    speak(wish_list[random.randint(0,3)])


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('classeskushan@gmail.com', 'llbkmgnopvzwolky')
    server.sendmail('classeskushan@gmail.com', to, content)
    server.close()
def Activate():
    speak("Activating home automation for light bulb.")
    wipro = "C:\\Users\\Hp\\Desktop\\WiproNextSmartHome.lnk"
    os.startfile(wipro)
def hackOS():
    speak("Opening Kali Linux.")
    keyboard.press_and_release("windows + m")
    kali= "D:\kali-linux-2021.3-vmware-amd64.vmwarevm\Kali-Linux-2021.3-vmware-amd64.vmx"
    os.startfile(kali)
    pyautogui.sleep(4)
    keyboard.press_and_release('windows + up')
    mouse.position = (56, 179)
    pyautogui.sleep(3)
    mouse.click(Button.left)
    exit()





if __name__ =="__main__":
    wishme()
    while True:
      query = takeCommand().lower()



      if 'wikipedia' in query:
          speak('Searching Wikipedia...')
          query=query.replace("wikipedia", "")
          results = wikipedia.summary(query, sentences=2)
          speak("According to wikipedia")
          print(results)
          speak(results)
    #Normal use
      #Wish back
      elif 'good morning' in query:
         speak( 'Good Morning! sir')
      elif 'good evening' in query:
          speak("Good evening! sir")
      elif "good afternoon" in query:
          speak("Good Afternoon! sir")
      ##############################
      elif 'light' in query:
          Activate()
      ##############################
      elif 'in chemistry' in query:
          speak("joining chemistry class sir!")
          Link = Links.Chemistry()
          webbrowser.open(Link)
          pyautogui.sleep(4)
          keyboard.press_and_release("ctrl + d")
          pyautogui.sleep(1)
          keyboard.press_and_release("ctrl + e")
          pyautogui.sleep(1)
          pyautogui.click(x=1298, y=609)
          speak("Chemistry class joined sir!")
          exit()
      elif "in physics" in query:
          speak("joining physics class sir!")
          Link = Links.Physics()
          webbrowser.open(Link)
          pyautogui.sleep(4)
          keyboard.press_and_release("ctrl + d")
          pyautogui.sleep(1)
          keyboard.press_and_release("ctrl + e")
          pyautogui.sleep(1)
          pyautogui.click(x=1298, y=609)
          speak("Physics class joined sir!")
          exit()
      elif "in maths" in query:
          speak("joining maths class sir!")
          Link= Links.Maths()
          webbrowser.open(Link)
          pyautogui.sleep(4)
          keyboard.press_and_release("ctrl + d")
          pyautogui.sleep(1)
          keyboard.press_and_release("ctrl + e")
          pyautogui.sleep(1)
          pyautogui.click(x=1298, y=609)
          speak("Physics class joined sir!")
          exit()
      elif "in computer" in query:
          speak("joining computer class sir!")
          Link= Links.Computer()
          webbrowser.open(Link)
          pyautogui.sleep(4)
          keyboard.press_and_release("ctrl + d")
          pyautogui.sleep(1)
          keyboard.press_and_release("ctrl + e")
          pyautogui.sleep(1)
          pyautogui.click(x=1298, y=609)
          speak("Physics class joined sir!")
          exit()
          ##################################################
      elif 'open youtube' in query:
          webbrowser.open("youtube.com")
          exit()
      elif 'open google' in query:
          webbrowser.open("google.com")
          exit()
      elif 'play music' in query:
          webbrowser.open("music.amazon.com")
          exit()
      elif'open brave' in query:
          brave = "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
          os.startfile(brave)
          exit()
      elif 'open edge' in query:
          edge="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
          os.startfile(edge)
      elif "maths" in query:
          webbrowser.open('https://www.youtube.com/playlist?list=PLQPK0MrSEwKITpy1ZOlJXsdZEgumBSITM')
          exit()
      elif "physics" in query:
          webbrowser.open("https://www.youtube.com/playlist?list=PLQPK0MrSEwKKkTv4h_kWUBpEcT4UU9gBo")
          exit()
      elif "open whatsapp" in query:
          keyboard.press_and_release('windows + s')
          pyautogui.sleep(1)
          keyboard.write('whatsapp')
          pyautogui.sleep(1)
          keyboard.press('enter')
          exit()
      elif "open telegram" in query:
          keyboard.press_and_release('windows + s')
          pyautogui.sleep(1)
          keyboard.write('telegram')
          pyautogui.sleep(1)
          keyboard.press("enter")
      elif "google search" in query:
          import wikipedia as googleScrap
          query = query.replace("google search ","")
          query = query.replace("google","")
          speak("This is what I found on the web!")
          pywhatkit.search(query)
          try:
              result = googleScrap.summary(query, 2)
              print(result)
              speak(result)
          except:
              speak("Can you please say that again, sir!")

    #Date and time
      elif 'the time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          print(strTime)
          speak(f"Sir, the time is {strTime}")
      elif 'the date' in query:
          strdate = datetime.datetime.today().strftime("%D")
          print(strdate)
          speak(f"Sir, the date is {strdate}")
    #Games
      elif 'open cyberpunk' in query:
          cyberpath = "C:\Cyberpunk.2077.v1.31\Cyberpunk.2077.v1.31\bin\x64\Cyberpunk2077.exe"
          os.startfile(cyberpath)
      elif 'open gta' in query:
          gamepath = "D:\Grand.Theft.Auto.V.v1.0.2189.0\Grand Theft Auto V\GTA5.exe"
          os.startfile(gamepath)
    #Special use
      elif 'kali linux' in query:
          hackOS()
      elif 'tor' in query:
          speak("By whonix vm or by tor browser? Sir..")
          if 'vm' in query:
              whopath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Oracle VM VirtualBox\Oracle VM VirtualBox.lnk"
              os.startfile(whopath)
              speak("Happy Whonix, sir!")
              exit()
          elif 'tor browser' in query:
              torpath = "C:\\Users\\Hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Start Tor Browser.lnk"
              os.startfile(torpath)
              speak("Do you want to use vpn sir?")
              if "yes" in query:
                  vpnpath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\ProtonVPN\ProtonVPN.lnk"
                  os.startfile(vpnpath)
                  speak("It is good to use a vpn while using tor, sir")
                  speak("Happy browsing sir!")
                  exit()




      elif 'open code' in query:
          pypath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm Community Edition 2021.3.1.lnk"
          os.startfile(pypath)
      elif 'send email' in query:

          try:
              speak("What should I say?")
              content = takeCommand()
              speak("Whom should I send?")
              to = email_contacts[takeCommand().lower()]
              sendEmail(to, content)
              speak("Email has been sent!")
          except Exception as e:
              print(e)
              speak("Sorry sir. I am not able to send this email.")


      elif 'exit' or 'quit' or 'stop' in query:
          speak("Thanks for using JARVIS sir, have a good day.")
          exit()