import time
import os
import winsound
import images
import random
import datetime
import pyttsx3
import pymini
from datetime import date
from colorama import init, Fore, Back, Style
i = 1
# * This is an operating system with a few apps!
# TODO make the autoclicker!
# ! made 1
today = date.today()
currentDT = datetime.datetime.now()
password = "3219"
points = -1000


try:
    print(Fore.MAGENTA + "\n")
    print("%d" % currentDT.hour,":%d" % currentDT.minute,":%d" % currentDT.second)
    day = today.strftime("%B %d, %Y")
    print("d2 =", day)
    print(images.password)
    password = input()
    print(Fore.RESET)

    # ! Wrong password
    if password != "3219":
        print(Fore.RED+images.wrongpassword)
        ta = input()


        if ta == "no":
            print("Ok successfully left")
        if ta == 'yes':
            second = input("enter your password ")
            if second != '3219':
                print("You locked the phone wait 20 seconds")
                while i <= 20:
                    time.sleep(1)
                    print(i)
                    i = i + 1
                trird = input("Type your password ")
                if trird != "3219":
                    print("Your phone is locked you dont have an other try!")
                else:
                    print("Ok plese enter it the first time!")
            else:
                    print("Right password plese enter it at the start" + Fore.RESET)
        else:
            print("Can't understand")
            from bug1 import PasswordGlitch
            print('good luck getting out of here!')
            



        #?Password right
    if (password == password or 
    second == password or 
    trird == password):
        while True:
            print(Fore.MAGENTA)
            print(images.home)
            print("%d" % currentDT.hour,":%d" % currentDT.minute,":%d" % currentDT.second,)
            main = input()

            # * The notes app!
            if main.lower() == 'notes':
                while True:
                    notes = []
                    print("Press leave to leave notes")
                    print(images.notes)
                    note_w = input(">  ")
                    if note_w != 'leave':
                        notes.append(note_w)
                        print(notes)
                    if note_w.lower() == 'leave':
                        print("You left!"+Fore.RESET)
                        break
                    if note_w.lower() == "i love pymini":
                        sum_of_digits = 500
                        print(sum_of_digits)
                        for digit in str(points):
                        # turn to string to iterate through
                            sum_of_digits += int(points)
                        # OUTPUT
                        print("500- points for you my best friend you are at", points)
                    

            
            # * The proggram app
            if main == 'program':
                print(images.proggram)
                print('type here')
                print('type here')
                print('type here')

            
            # * The calculator app
            if main == 'calculator':
                for i in range(5):
                    time.sleep(1)
                    print(Fore.GREEN+images.calculator)
                    print('type 12345678910 or 1234.003 if you want to leave the calculator please enter it on the first number (you have to pass every number thought!)')
                    num = float(input("Your number "))
                    num2 = float(input("Your second number "))
                    # num3 = input("Your third number ")
                    num4 = input('do you want "+ - * multiply or / for devide" ')
                    if num4 == '+':
                        print('the result of', num, '+', num2, 'is', (num) + (num2))
                    if num4 == '-':
                        print('The result is', (num) - (num2))
                    if num4 == '*':
                        print("the result is", (num) * (num2))
                    if num4 == '/':
                        print('the result is', (num) / (num2))
                    if num == '12345678910' or num == "1234":
                        print('You have seccesfully left '+Fore.RESET)
                        import pymini
                        break
                    else:
                        print('Invalaid input')
                    
            if main.lower() == 'image':
                from PIL import Image
                folder = input("what folder (if none type none), (if a folder is on a folder type folder\\\\folder2) : ")
                
                if folder == "none":
                    img = input("Ok what image do you want (the name with the .png) : ")
                
                    print("Here's what I found!")
                    #read the image
                    im = Image.open(f"C:\\Users\\water\\Desktop\\coding py\\pymini\\{img}")
                    #show image
                    im.show()
                
                img = input("Ok what image do you want (the name with the .png) : ")
            
                print("Here's what I found!")
                #read the image
                im = Image.open(f"C:\\Users\\water\\{folder}\\{img}")
                #show image
                im.show()

            if main == 'games':
            #*The games folder!
                time.sleep(1)
                print(Fore.LIGHTYELLOW_EX+'do you want to play (rock, paper scissors = 1/maths = 2/fast typing = 3/adventure_game = 4/gimbling_game = 5\n/mayse = 6)')
                game = input()

                # * The adventure_game game
                # ? Im using an other project for this game!
                if game.lower() == 'adventure_game' or game.lower() == '4':
                    print('ok starting')
                    import adventure_game
                

                # * The gimbling_game
                # ! Im using an other project for this game!
                if game.lower() == 'gimbling_game' or game.lower() == '5':
                    print('ok starting')
                    import gimbling_game

                
                
                #? rock, paper, scissors
                if game.lower() == 'rock, paper, scissors' or game.lower() == '1':
                    while True:
                        print('what do you want rock, paper or scissors\nif you want to leave press o')
                        rps = input()
                        ROPESC = ['rock', 'paper', 'scissors']
                        RPS = random.choice(ROPESC)
                        print('the bot chose', RPS)
                        if rps == 'o': 
                            print('You left!')
                            break
                    

                if game == 'maths' or game == '2':
                    Maths = ['4', '79', '89', '57', '8', '7.8', '-2', '69']
                    Maths2 = ['45', ' +3','76', '8.09', '53', '21']
                    Symbols = ['+', '-', '*', '/']

                    symbols = random.choice(Symbols)
                    maths = random.choice(Maths)
                    maths2 = random.choice(Maths2)
                    print('Starting in ')
                    time.sleep(1)
                    print(3)
                    time.sleep(1)
                    print(2)
                    time.sleep(1)
                    print(1)
                    time.sleep(1)
                    print('GO!')
                    start_time = time.time()
                    print('Your porblem is', maths, symbols, maths2, '=')
                    maths = input()
                    fin_time = time.time() - start_time
                    m10 = points - 10
                    print('It took you', fin_time, 'to figure it out + 10 points')
                if game == 'fast typing' or game == '3':
                    fastyping = ['cat', 'man', 'woman', 'python', 'VScode', 'easy', 'last']
                    time.sleep(1)
                    print(3)
                    time.sleep(1)
                    print(2)
                    time.sleep(1)
                    print(1)
                    time.sleep(1)
                    print("GO!")
                    fast = random.choice(fastyping)
                    ft = random.choice(fastyping)
                    fasttyping = random.choice(fastyping)
                    start_time = time.time()
                    time.sleep(3)
                    ft = input(fasttyping)
                    time.sleep(1)
                    ft2 = input(fast)
                    time.sleep(0.4)
                    ft3 = input(ft)
                    if ft != fasttyping and ft2 != fast and ft3 != ft:
                        print("You're wrong!")
                    else:
                        fin_time = time.time() - start_time
                        m5 = points - 5
                        print("+5 points You're right! It took you", fin_time, "to reach"+Fore.RESET)
            if main == 'camera':
                import cv2

                cap = cv2.VideoCapture(0)

                # Check if the webcam is opened correctly
                if not cap.isOpened():
                    raise IOError("Cannot open webcam")

                while True:
                    ret, frame = cap.read()
                    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
                    cv2.imshow('Pycamera', frame)

                    c = cv2.waitKey(1)
                    if c == 27:
                        break

                cap.release()
                cv2.destroyAllWindows()
            if main.lower() == 'google':
                print(Fore.RED)
                import google_assistant
                if google_assistant.ask.lower() == "leave":
                    break
                print(Fore.RESET)
            if main.lower() == 'repeat':    
                while True:
                    repeat = input(Fore.YELLOW+"<say something... >$ ")
                    Repeat = pyttsx3.init()
                    Repeat.say(repeat)
                    Repeat.runAndWait()
                    print(Fore.RESET)
            if main.lower() == 'motivation':
                                
                talk = pyttsx3.init()
                for i in range(10):
                    Motivation = ["You are the best proggramer ever", 'everyone loves you', "You're pretty"]
                    motivation = random.choice(Motivation)
                    talk.say(motivation)
                    talk.runAndWait()
                    print(motivation)
            if main.lower() == "demotivation":
                talk = pyttsx3.init()
                name = input("tell me your name : ")
                for i in range(10):
                    Demotivation = [
f"{name}, you look like a professional blind date.",
f"{name}, you're not the sharpest knife in the drawer.",
f"{name}, I could agree with you, but then we'd both be wrong.",
f"{name}, let me guess",
f"{name}, You really are an idiot", 
f"{name}, Why do you exist?",
f'{name}, I would insult you but you are just waste of breath',
f"{name}, Your mom was 9 months in pain so you exist"]
                    demotivation = random.choice(Demotivation)
                    talk.say(demotivation)
                    talk.runAndWait()
                    print(demotivation)
            if main.lower() == "vgmedia":
                import vgmedia

            if main.lower() == 'clock':
                while True:
                    time.sleep(1)
                    currentDT = datetime.datetime.now()
                    print("%d" % currentDT.hour,":%d" % currentDT.minute,":%d" % currentDT.second)
            if main.lower() == "loop" or main.lower() == "turn off infinite feature":
                turn_off = input("Are you sure you want to turn off? (yes/no) : ")
                if turn_off == "no":
                    print("Ok not gonna turn off infinite feature!")
                if turn_off == "yes":
                    print("Successfully turned off!")
                    for i in range(1):
                        import pymini
                        break
                    break
            if main.lower() == "setting":
                import pysettings as pys
            if main.lower() == "pymini":
                m300 = points - 500
                print("-500 points :) you are at", m300)
            if main.lower() == "alarm" and points < -500:
                import alarm
            if main.lower() == "alarm" and points > -500:
                print("You dont have the points for premium pymini")
            if main.lower() == "spam bot":
                import pyautogui
                Type = input("What type of spambot do you want? (SpamBot) (TyperBot) (Autoclicker) (natural TypingBot) (KeyBot) : ")
                if Type == "SpamBot":
                    text = input(f"What text do you want : ")
                    Times = int(input("How many times do you wish to type it : "))
                    delayTime = int(input("How much time do you want to wait until it spams? (more than 1) :"))
                    if delayTime > "0":
                        print("Im really sorry but you can't do that its really dangerous for you computer")
                    else:
                        time.sleep(delayTime)
                        #Warning Do Not Use this with out a time.sleep()
                        for i in range(Times):
                            pyautogui.typewrite(text)
                if Type == "TyperBot":
                    text = input(f"What text do you want : ")
                    delayTime = int(input("How much time do you want to wait until it spams? (more than 1) :"))
                    if delayTime > "0":
                        print("Im really sorry but you can't do that its really dangerous for you computer")
                    else:
                        time.sleep(delayTime)
                        #Warning Do Not Use this with out a time.sleep()
                        pyautogui.typewrite(text)

                if Type == "Autoclicker":
                    print("You will have 50 seconds of an autoclicker!")
                    ac = input("(v) : ")
                    if ac == "v":
                        time.sleep(5)
                        for i in range(10):
                            pyautogui.click()
                            pyautogui.click()
                            pyautogui.click()
                            pyautogui.click()
                            pyautogui.click()
                            pyautogui.click()
                if Type == 'natural TypingBot':
                    Text = input("What text do you want to dysplay? : ")
                    Delay = int(input("how much time do you want to delay? : "))
                    time.sleep(Delay)
                    for char in Text:
                        pyautogui.typewrite(char)
                if Type.lower() == 'keybot':
                    Key = input("What key do you want to type : ")
                    Delay = int(input("How much delay : "))
                    Times = int(input("How many times : "))
                    time.sleep(Delay)
                    for i in range(Times):
                        pyautogui.press(Key)
                        import SpamBot

                    
            if main.lower() == "spambot" and points > -500:
                print("You dont have the points for premium pymini")
            if main.lower() == "stats":
                if points > 500:
                    print("points are" + points + "you are a normal guy")
                if points > 0:
                    print("points are" + points + "you are a good guy")
                if points > -500:
                    print("points are" + points + "You are the a REALLY GOOD GUY (you can get premium)")
                if points < 500:
                    print("points are" + points + "You are questionable?")                    
                if points < 1000:
                    print("points are" + points + "You are or a normal guy or a bad guy")                    
                    
            if main.lower() == "register":
                registarity == True
                def registarity() :
                    name = input("Your name : ")
                    password = input(f"Please enter your password {name} : ")
                    password = input(f"Enter you password again {name} : ")
                    confirm = input("do you confirm (y) : ")
                    if confirm != 'y':
                        registarity == False
                        print("Ok so you aren't a pymini registed member")



            if main.lower() == 'leave':
                break             
            else:
                print("Im really sorry but I can't understand")
            
except Exception:
    for i in range(0,2):
        # winsound.PlaySound(sound,flags)
        duration = 1000  # milliseconds
        freq = 440  # Hz
        winsound.Beep(freq, duration)
    talk = pyttsx3.init() 
    talk.say("Something went wrong")
    talk.runAndWait()
    import Error
    print(Fore.BLUE+images.Error+Fore.RESET)
    import load_bar
    import pymini

__version__ = "1.0.5"