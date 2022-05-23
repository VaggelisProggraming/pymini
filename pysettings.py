#these are really important to make it work
x = input("do you want display or users? (user/display/leave)")
if x.lower() == 'user':
    #These are the users
    print("What user are you?\n")
    print("proggraming")
    print("kids mode")
    print("Student")
    user = input("$ ")
    if user.lower() == "proggraming":
        print("Ok turning on proggraming mode!")
        import pygram
    if user.lower() == "kids mode":
        print("Ok its your time to user pymini kids :)")  
    if user.lower() == "student":
        import studentpymini 
    if x.lower() == "display":
        #This is actuallythe settings
        print("What setting do you want?\n")
        print("wallpaper")
        print("talking")
        print("infinite feature off")
    else:
        print("Im really sorry but i can't understand")

        