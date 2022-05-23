import os
import time
import uuid
import webbrowser
import images
import random
import datetime
import pyttsx3
from datetime import date
import pyautogui as gui
from colorama import init, Fore, Back, Style
today = date.today() #from libraries
currentDT = datetime.datetime.now()
id = uuid.uuid4()
password = "3219" # strings
Gmail = 'spyridoni164@gmail.com'
PymKeys = 0 # intigers
i = 1



try:
    while True:
        print(Fore.MAGENTA)
        print(images.home)
        print("%d" % currentDT.hour,":%d" % currentDT.minute,":%d" % currentDT.second)
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
                symbols = ['+', '-', '*', '/']
                nums = num, num2
                if num4 != symbols or nums != int:
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
            print(Fore.LIGHTYELLOW_EX+'do you want to play (rock, paper scissors = 1/maths = 2/fast typing = 3/not readt to launch(adventure_game = 4)/gimbling_game = 5\n/mayse = 6)')
            game = input()

            # * The adventure_game game
            # ? Im using an other project for this game!
            if game.lower() == 'adventure_game' or game.lower() == '4':
                print("We're really sorry but we're working on the adventure game")
            

            # * The gimbling_game
            # ! Im using an other project for this game!
            if game.lower() == 'gambling game' or game.lower() == '5':
                from pyautogui import countdown
                print('ok starting')
                # import gimbling_game
                countdown(3)
                firstChocie = random.randint(0, 100)
                SecondChoice = random.randint(0, 100)
                ThirdChocie = random.randint(0, 100)
                print(firstChocie, "|", end=' ')
                time.sleep(1)
                print(SecondChoice, ' |', end=' ')
                time.sleep(1)
                print(ThirdChocie)
                time.sleep(1)
                Total = firstChocie + SecondChoice + ThirdChocie
                print(f"Your total Pymkey money is {Total}")
                if(Total>500):
                    time.sleep(1)
                    int(Total = Total + 50)
                    print("Ok so theres a rule if you have more than 700PymKeys so you get 50 more so...", Total + 50)
                    PymKeys = PymKeys + Total
                elif(Total<499):
                    int(Total = Total - 100)
                    print("Ok so there's a rule if you have less than 700PymKeys so you get 100 less so...", Total - 100)
                    PymKeys = PymKeys + Total

            
            
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
                print('It took you', fin_time, 'to figure it out + 10 points')
            if game == 'fast typing' or game == '3':
                fastyping = ['cat', 'man', 'woman', 'python', 'VScode', 'easy', 'last']
                gui.countdown(3)
                print("GO!")
                fast = random.choice(fastyping)
                ft = random.choice(fastyping)
                fasttyping = random.choice(fastyping)
                start_time = time.time()
                Times = range(10)
                times = random.choice(Times)
                time.sleep(times)
                ft = input(fasttyping)
                time.sleep(times)
                ft2 = input(fast)
                time.sleep(times)
                ft3 = input(ft)
                if ft != fasttyping and ft2 != fast and ft3 != ft:
                    print("You're wrong!")
                else:
                    fin_time = time.time() - start_time
                    print("+5 points You're right! It took you", fin_time, "to reach the finish line"+Fore.RESET)
                    PymKeys = PymKeys + 5
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
        if main.lower() == "vgmedia":
            print("You need to be more than 13years old")
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
                    import pyminiInf
        if main.lower() == "setting":
            import pysettings as pys
        if main.lower() == "alarm":
            import alarm
        if main.lower() == "alarm":
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
                    
                
        if main.lower() == "register":
            # registarity == True
            def registarity() :
                name = input("Your name : ")
                password = input(f"Please enter your password {name} : ")
                password = input(f"Enter you password again {name} : ")
                confirm = input("do you confirm (y) : ")
                import rPymini
                if confirm != 'y':
                    print("Ok so you aren't a pymini registed member")
                    registarity == False
            registarity()
        if main == 'personal info': 
            print("Please Enter your password")
            pas = input("Enter your password : ")
            if(pas!=password):
                print("Wrong Password")
                time.sleep(1)
            if(pas==password and '@gmail.com' not in Gmail): 
                print(f"ID : {id}")
                Email=input("add a Email : (no) (email)")
                if(Email=='no'):
                    print("Ok")
                if("@gmail.com"in Email):
                    print("Ok so")
                    print(f"Email : {Email}")
            if(pas==password and '@gmail.com' in Gmail):
                print(f'ID : {id}')
                print(f'Email : {Gmail}')
                print(f"money {PymKeys}")

        if main.lower() == "youtube":
            webbrowser.open("www.youtube.com")
        if  main.lower() == "wikipedia":
            webbrowser.open("www.wikipedia.com")
        if main.lower() == 'notepad':
            os.system("notepad")
        if main.lower() == 'discord':
            webbrowser.open("www.discord.com")
        if main.lower() == 'amazon':
            webbrowser.open("www.amazon.com")
        if main.lower() == 'speedrun':
            webbrowser.open("www.speedrun.com")

        if main.lower() == 'proggram':
            print("Ok gonna open pyminiIDE")
            import pyminiIDE



        if main.lower() == 'leave':
            KeyboardInterrupt
            
except KeyboardInterrupt:
    print("Keyboard interupt")
except Exception:
    print(Fore.BLUE+images.Error+Fore.RESET)
    import load_bar
    import PyminiWithNoPassword

__version__ = "1.0.5"