import pyttsx3 
import speech_recognition as sr
import webbrowser
import time
import datetime
import os
from pydub import AudioSegment
from pydub.playback import play
wel = pyttsx3.init()
voices = wel.getProperty('voices')
wel.setProperty('voices',voices[0].id)
rate = wel.getProperty("rate")
wel.setProperty("rate",135)
print(rate)
def spake(audio):
    wel.say(audio)
    wel.runAndWait()

def commas():
    commas = sr.Recognizer()
    with sr.Microphone() as mic :
        print('say commands sir...')
        commas.pause_threshold =1
        audio = commas.listen(mic)
        print('Recording...')
    query = commas.recognize_google(audio, language='en')

spake('Hello sir sif , say your commands ')
while True:
    query = commas()
    if 'no commands' in query:
        spake('I exit')
    if 'open firefox' in query:
        spake('ok sif and open firefox')
        FR="C:\Program Files\Firefox Nightly\firefox.exe"
        os.startfile(FR)
    if 'open photo shop'in query:
        spake('ok sif and open adobe photo shop')
        FA="F:\ps\Adobe\Adobe Photoshop 2023\Photoshop.exe"
        os.startfile(FA)
    if 'open game loop'in query:
        spake('ok sif, open game loop')
        FC="F:\TxGameAssistant\AppMarket\AppMarket.exe"
        os.startfile(FC)
    if 'open epic games'in query:
        spake('DONE')
        DL="D:\epic games\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"
        os.startfile(DL)
    if "internet download manager"in query:
        spake('DONE')
        LD="C:\Program Files (x86)\Internet Download Manager\IDMan.exe"
        os.startfile(LD)
    if 'turboVPN' in query:
        spake('DONE')
        OK="C:\Program Files (x86)\TurboVPN\TurboVPNLauncher.exe"
        os.startfile(OK)
    if 'open microsoft edge'in query:
        spake('ok and open edge')
        LP="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        os.startfile(LP)
    if 'open HTTP' in query:
        spake('OK')
        PT="C:\Program Files (x86)\HTTPDebuggerPro\HTTPDebuggerUI.exe"
        os.startfile(PT)
    if 'Driver booster' in query:
        spake('OK')
        MS="C:\Program Files (x86)\IObit\Driver Booster\10.2.0\DriverBooster.exe"
        os.startfile(MS)
    if 'which are your'in query:
        spake('im ben')
    if 'Which are you from' in query:
        spake('im Algeria in Djelfa in Idrisiyah')
    if 'Who made you' in query:
        spake('he sif')
    if 'Solve the problem pc'in query:
        spake('No problem')
    if 'gg ben' in query:
        spake('gg sif')
    if 'who is big' in query:
        spake('he Tusk')   
    if 'who is crazy' in query:
        spake('he Ashraf') 
    if 'What do you think of Hamida' in query:
        spake('he king')
    if 'sif' in query:
        spake('it.s sir')      
    if 'Hello' in query:
        spake('Hello sir sif')
    if 'how are your age' in query:
        spake('17')
    if 'open google' in query:
        spake('OK SIF')
        time.sleep(3)
        webbrowser.open_new_tab('https://www.google.com')
    if 'open facebook' in query:
        spake('OK SIF , Im open facebook')
        time.sleep(3)
        webbrowser.open_new_tab('https://www.facebook.com')
    if 'open instagram' in query:
        spake('OK SIF and open instagram')
        time.sleep(3)
        webbrowser.open_new_tab('https://www.instagram.com')
    if 'open tiktok' in query:
        spake('Ok sif')
        time.sleep(3)
        webbrowser.open_new_tab('https://www.tiktok.com')
    if 'open github' in query:
        spake('ok sif ,open github') 
        time.sleep(3)
        webbrowser.open_new_tab('https://www.github.com')
    if 'open YouTube' in query:
        spake('ok sif, open youtube')
        time.sleep(3)
        webbrowser.open_new_tab('https://www.youtube.com')
    if 'open speed test' in query:
        spake('ok sif and open speed test')
        time.sleep(1)
        webbrowser.open_new_tab('https://www.speedtest.net/')
    if 'ben' in query:
        spake('hello , what do you want')
    if 'hello ben' in query:
        spake('Im good')
    if 'shut down' in query:
        spake('ok sif and shut down PC')
        os.system("shutdown /s /t 2")
    if 'restart' in query:
        spake('ok sif and restart PC')
        input(os.system("restart /s /t 2"))
    if 'sleep' in query:
        spake('ok sif and sleep PC')
        os.system("sleep /s /t 2")
#   if 'open Visual Studio' in query:
#      spake('ok sif,open visual studio')
#      f11= "C:\Users\PC\AppData\Local\Programs\Microsoft VS Code\Code.exe"
#     os.startfile(f11)
    if 'open browser google chrome' in query:
        spake('ok sif,open google chrome')
        f2= "C:\Program Files\Google\Chrome\Application\chrome.exe"
        os.startfile(f2)
    if 'open valorant' in query:
        spake('ok sif,open riot client')
        f3="E:\Riot Games\Riot Client\RiotClientServices.exe"
        os.startfile(f3)
    if 'opne kali linux' in query:
        spake('ok sif,open kali')
        f4="F:\kali-linux-2022-W48-vmware-amd64\kali-linux-2022-W48-vmware-amd64.vmwarevm\kali-linux-2022-W48-vmware-amd64.vmx"
        os.startfile(f4)
    if 'school' in query:
        time=input('enter the time: ')
        b=AudioSegment.from_mp3('so/alarm.mp3')
        play(b)
        while True:
            Timo=datetime.datetime.now()
            now=Timo.strftime("%H:%M:%S")
            if now == time:
                b=AudioSegment.from_mp3('so/doaa.mp3')
                play(b)
                if now > time:
                    break
