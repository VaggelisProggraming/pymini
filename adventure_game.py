try:
    
    from time import time, sleep
    from pyautogui import countdown
    import keyboard
    from colorama import init, Fore, Back, Style
    
    start = input("Do you want to play not or later (n) (l) : ")

    if start.lower() == 'n':
        print("Ok so your time is going to be recorded to know your time")
        sleep(1)
        countdown(3)
        start_time = time()
        x = input("Ok so you found a street where do you go (left, right, straight) : ")
        if x == 'left':
            y = input("Ok so you found a lake waht do you do (swim) (go around) <---(*It's really big) (boat)  <---(*you found it in a near by harbur*) : ")
            if y.lower() == 'swim':
                print("This is going to take a while")
                sleep(10)
                print("You made it across")
                z = input("Ok there's a really big climb what do you do (climb it) (back) <--(go back to the street senario) : ")
                if z.lower() == 'climb it':
                    print("Good choice but I think the other thing was a right move")
                    sleep(1)
                    KeyboardInterrupt
                if z.lower() == 'back':
                    X = input("Ok so you found a street where do you go (left, right, straight) : ")
                    if X == 'left':
                        print("You really are an idiot")
                    if X == 'right':
                        # print("hello world")
                        print("You're smart!", end=' ')
                        sleep(1)
                        print("see I said Good choice but I think the other thing "+Fore.BLACK+Back.YELLOW+"was a right move"+Back.RESET, Fore.RESET)
                        print("Ok let's continue")
                        sleep(1)
                        print("YOU WON")
            if y.lower() == 'boat':
                print("ok so you found the boat let's go to the other side aaaaaaa", end='')
                sleep(5)
                print("nd")
                sleep(0.1)
                print("wait...")
                sleep(5)
                print("i don't know how to drive a boat")
                sleep(1)
                KeyboardInterrupt
            if y.lower() == 'go around':
                print("This is going to take a while")
                sleep(5)
                KeyboardInterrupt

    if start.lower() == 'l':
        print("Ok gonna wait press s to start the game")
        while 1:
                if keyboard.is_pressed("s"):
                    break

except Exception:
    Exception()