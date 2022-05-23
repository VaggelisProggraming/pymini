import pyautogui  
import win32api, win32con, time, keyboard
import time
while 1:
    try:
        def Autoclicker() :
            time.sleep(3)
            for i in range(50):
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)            
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)                  
                pyautogui.click()
                pyautogui.click()
                pyautogui.click()
                pyautogui.click()
                pyautogui.click()
                pyautogui.click()
        def SpamBotTyper() :
            time.sleep(5)
            for i in range(40):
                #This will make it more humanble
                for char in " ":
                    pyautogui.typewrite(char)
        def SpamBot():
            #Warning Do Not Use this with out a time.sleep()
            for i in range(5):
                pyautogui.typewrite("The quick brown fox jumps over the lazy dog")
        def KeyPress() :
            #This will press a key
            time.sleep(5)
            for i in range(40):
                pyautogui.press("Space")
                pyautogui.press("Space")
                pyautogui.press("Space")
                pyautogui.press("Space")
                pyautogui.press("Space")
                pyautogui.press("Space")
                pyautogui.press("Space")
                pyautogui.press("Space")
        def Coundown():
            pyautogui.countdown(seconds=5)
        def screenShot() :
            pyautogui.screenshot('screenshot.png')
        SpamBots = """
        """
    except KeyboardInterrupt:
            print("Keyboard Interrupt")
            break