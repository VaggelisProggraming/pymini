import random
import time
import images
import vgmedia_librares as librares
name = ''
try:
    print("Welcome to vgmedia")
    time.sleep(1)
    scroll = input("<Enter (Down or press Enter), (help)>$ ")
    if scroll == 'down' or scroll == '':
        while True:
            account = random.choices(librares.Accounts)
            posts = random.choices(librares.Posts)
            year = random.choices(librares.years)
            follow = random.choices(librares.Followers)
            veiws = random.choices(librares.Veiws)
            likes = random.choices(librares.Likes)
            comments = random.choice(librares.comments)
            commenting = random.choice(librares.Commenting)
            if posts == "The boring company is doing good!":
                print(f"{year} created by Elon Musk {follow}\n\n\nThe boring company is doing good!\nlikes {likes}")
            if posts == "Im building a new spaceX rocket":
                print(f"{year} created by Elon Musk {follow}\n\n\nIm building a new SpaceX rocket\nlikes {likes}")
            print(f"{year} created by {account} {follow}\n\n\n{posts}\nlikes {likes}\nComments {comments}")
            scroll = input("$ ")
            if scroll == "comment":
                for i in range(5):
                    account = random.choices(librares.Accounts)
                    commenting = random.choice(librares.Commenting)
                    print(f"{account} : {commenting}")
                name = input("Enter you name : ")
                Comment = input(f"{name} type your comment here : ")
                if name == "leave":
                    print("Ok leaving")
                    break
            if scroll == "My name":
                print("Ok With a name you can comment")
                name = input("Enter you name : ")
            if scroll == "help":
                print("""
                ok so here are some thing you can type
                you can type these : (comment) (name) (leave)
                """)
            if scroll == "credits":
                print("""
                
                Thanks for asking


                """)
                from tkinter import *
                root = Tk()
                root.title('Credits')
                def emailMe() :
                    # import google_assistant
                    import webbrowser as wb
                    wb.open('https://mail.google.com/mail/u/0/#advanced-search/to=watervga%40gmail.com&query=in%3Asent&isrefinement=true&todisplay=VGA+vaggelis?compose=GTvVlcSKkVRkkZGJfrWQhMnRWDpTxNxzNmqZNjDsxRfsVtdbnzcfVVSLNDtLCmZpKVMGBtVxkPqCL')                  
                
                root = Tk()
                root.title('Credits')
                # specify size of window.
                root.geometry("250x170")
                
                # Create text widget and specify size.
                T = Text(root, height = 5, width = 52)
                
                # Create label
                l = Label(root, text="Made by vaggelis")
                L = Label(root, text = "Contact me at")
                L.config(font =("Courier", 18))
                l.config(font =("Courier", 14))
                
                Fact = """
                E-mail me on 


                watervga@gmail.com

                """

                Gmail = Button(root, text='\n\n\nEmail', command=emailMe)
                T.insert(END, Fact)

                l.pack()
                L.pack() 
                T.pack()
                Gmail.pack()

                
                root.mainloop()

            if scroll == 'leave':
                break
except Exception:
    print(images.Error)    