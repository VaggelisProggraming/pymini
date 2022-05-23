import re
import subprocess
from importlib.resources import path
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from xml.dom.expatbuilder import theDOMImplementation
import idlelib.colorizer as ic
import idlelib.percolator as ip

x=range(10)
compiler = Tk()
compiler.title('pymini IDE')
compiler.geometry('1500x1000')
file_path = ''


#This is the html tutorial its really long but
def HtmlTutorial() :
    root = Tk()
    root.title('HTMLTutorial')
    from Tutorial import HTMLtitle
    titleLabel = Label(root, text=HTMLtitle)
    from Tutorial import BaseOfHTML
    BaseOfHTML = Label(root, text=BaseOfHTML, font='Helvetica 7 bold')
    titleLabel.pack()
    BaseOfHTML.pack()
def PythonTutorial() :
    from Tutorial import PythonTitle
    root = Tk()
    root.title('python')
    label = Text(root, text=PythonTitle, font='Helvetica 10 bold')
    label.pack()
    root.mainloop()

def OpenGetStarted() :
    root = Tk()
    root.title('Get started with proggraming')
    root.config(bg="blue")
    Title = Label(root, text="You NEED to start proggraming", font='Helvetica 50 bold')
    textForStarting = Label(root, text="""proggraming is really easy to learn
    start with html or Python then step up to Java, C, C++ or C#
    but starting with python means when you are a bigginer its really good but when you become good at python its good for a lot of things one of them isn't video games
    """, font='Helvetica 15 bold')
    HTMLButton = Button(root, text="Start with HTML", command=HtmlTutorial)
    PythonButton = Button(root, text="Start with Python", command=PythonTutorial)
    Title.config(bg="blue", fg="white")
    textForStarting.config(bg="blue", fg="white")
    HTMLButton.config(bg="RED", fg="white")
    PythonButton.config(bg="GREEN", fg="white")
    Title.pack()
    textForStarting.pack()
    HTMLButton.pack()
    PythonButton.pack()


def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)

def RunS(e):
    run()

def light():
    editor.config(bg='white', fg='black', insertbackground='blue')
def dark():
    editor.config(bg='black', fg='red', insertbackground='blue')
def magenta():
    editor.config(bg='magenta', fg='yellow', insertbackground='blue')
def HackerMan():
    editor.config(bg='black', fg='green', insertbackground='blue')
def yellow():
    editor.config(bg='yellow', fg='green', insertbackground='blue')
def darkPython():
    editor.config(bg='gray', fg='#ADD8E6', insertbackground='white')
def lightHTML():
    editor.config(bg='white', fg='orange', insertbackground='#ADD8E6')
def lightHTML():
    editor.config(bg='gray', fg='orange', insertbackground='#ADD8E6')
def cAndCpp():
    editor.config(bg="gray", fg="magenta", insertbackground="black", font=('Helvetica', 15, 'bold'))

def OpenMyThemesShortcut(e):
    #This will make an other window
    root = Tk()
    root.title("IDE settings")
    w = Label(root, text='Here are all the themes')
    w.pack
    v = IntVar()
    #the choices
    Radiobutton(root, text='light', command=light, variable=v, value=1).pack(anchor=W)
    Radiobutton(root, text='dark', command=dark, variable=v, value=2).pack(anchor=W)
    Radiobutton(root, text='magenta', command=magenta, variable=v, value=3).pack(anchor=W)
    Radiobutton(root, text='hacker theme', command=HackerMan, variable=v, value=4).pack(anchor=W)
    Radiobutton(root, text='yellow', command=yellow, variable=v, value=5).pack(anchor=W)
    Radiobutton(root, text='Dark + Python', command=darkPython, variable=v, value=6).pack(anchor=W)
    Radiobutton(root, text='light + html', command=lightHTML, variable=v, value=7).pack(anchor=W)
    Radiobutton(root, text='dark + html', command=lightHTML, variable=v, value=7).pack(anchor=W)
    Radiobutton(root, text='dark + C/C++', command=cAndCpp, variable=v, value=8).pack(anchor=W)
    mainloop()    

def OpenMyThemes():
    #This will make an other window
    root = Tk()
    root.title("IDE settings")
    w = Label(root, text='Here are all the themes')
    w.pack
    v = IntVar()
    #the choices
    Radiobutton(root, text='light', command=light, variable=v, value=1).pack(anchor=W)
    Radiobutton(root, text='dark', command=dark, variable=v, value=2).pack(anchor=W)
    Radiobutton(root, text='magenta', command=magenta, variable=v, value=3).pack(anchor=W)
    Radiobutton(root, text='hacker theme', command=HackerMan, variable=v, value=4).pack(anchor=W)
    Radiobutton(root, text='yellow', command=yellow, variable=v, value=5).pack(anchor=W)
    Radiobutton(root, text='Dark + Python', command=darkPython, variable=v, value=6).pack(anchor=W)
    Radiobutton(root, text='light + html', command=lightHTML, variable=v, value=7).pack(anchor=W)
    Radiobutton(root, text='dark + html', command=lightHTML, variable=v, value=7).pack(anchor=W)
    Radiobutton(root, text='dark + C/C++', command=cAndCpp, variable=v, value=8).pack(anchor=W)
    mainloop()    

#this is the max size on text
#Its for a shrotcut the e on the () can be only for shortcuts
def thirdteenS(e):
    editor.config(width=1000, height=500,  font=('Georgia 40'))
    code_output.config(width=1000, height=500,  font=('Georgia 40'))


#This is for the gui
def thirdteenM():
    editor.config(width=1000, height=500,  font=('Georgia 40'))
    code_output.config(width=1000, height=500,  font=('Georgia 40'))


#20 for shortcut
def twentyS(e):
    editor.config(width=1000, height=500,  font=('Georgia 20'))
    code_output.config(width=1000, height=500,  font=('Georgia 20'))


#20 for gui
def twenty():
    editor.config(width=1000, height=500,  font=('Georgia 20'))
    code_output.config(width=1000, height=500,  font=('Georgia 20'))


#15 for shortcut
def fifteenS(e):
    editor.config(width=1000, height=500, font=('Georgia 15'))
    code_output.config(width=1000, height=500, font=('Georgia 15'))


#15 for gui
def fifteen():
    editor.config(width=1000, height=500, font=('Georgia 15'))
    code_output.config(width=1000, height=500, font=('Georgia 15'))


#14 for gui
#Shortcuts are on 30, 20, 15, 10 and 1
def fourteen():
    editor.config(width=1000, height=500, font=('Georgia 14'))
    code_output.config(width=1000, height=500, font=('Georgia 14'))

#13 for gui
def thirdteen():
    editor.config(width=1000, height=500, font=('Georgia 13'))
    code_output.config(width=1000, height=500, font=('Georgia 13'))

# 12 for gui
def twelve():
    editor.config(width=1000, height=500, font=('Georgia 12'))
    code_output.config(width=1000, height=500, font=('Georgia 12'))

# 11 for gui
def eleven():
    editor.config(width=1000, height=450, font=('Georgia 11'))
    code_output.config(width=1000, height=450, font=('Georgia 11'))

# 10 for shortcut
def tenS(e):
    editor.config(width=1000, height=500, font=('Georgia 10'))
    code_output.config(width=1000, height=450, font=('Georgia 10'))


# 10 for gui
def ten():
    editor.config(width=1000, height=500, font=('Georgia 10'))
    code_output.config(width=1000, height=450, font=('Georgia 10'))


# 5 for gui
def five():
    editor.config(width=1000, height=500, font=('Georgia 5'))
    code_output.config(width=1000, height=400, font=('Georgia 5'))


#The smallest text size is the 1
#1 for shortcut
def oneS(e):
    editor.config(width=100, height=500, font=('georgia 1'))
    code_output.config(width=100, height=400, font=('georgia 1'))


#1 for gui
def one():
    editor.config(width=100, height=500, font=('georgia 1'))
    code_output.config(width=100, height=300, font=('georgia 1'))


#This is the gui
def MyTextSize():
    root = Tk()
    root.title("IDE text size")   
    v = IntVar() 
    #These all make the options for every thing you'll need for text size
    Radiobutton(root, text='40(mega)', command=thirdteenM, variable=v, value=1).pack(anchor=W)

    Radiobutton(root, text='20', command=twenty, variable=v, value=2).pack(anchor=W)

    Radiobutton(root, text='15', command=fifteen, variable=v, value=3).pack(anchor=W)

    Radiobutton(root, text='14', command=fourteen, variable=v, value=4).pack(anchor=W)

    Radiobutton(root, text='13', command=thirdteen, variable=v, value=5).pack(anchor=W)

    Radiobutton(root, text='12', command=twelve, variable=v, value=6).pack(anchor=W)

    Radiobutton(root, text='11', command=eleven, variable=v, value=7).pack(anchor=W)

    Radiobutton(root, text='10', command=ten, variable=v, value=8).pack(anchor=W)

    Radiobutton(root, text='5', command=five, variable=v, value=9).pack(anchor=W)

    Radiobutton(root, text='1', command=one, variable=v, value=10).pack(anchor=W)

    root.bind('<Control-p>', twentyS)
    root.bind('<Control-m>', tenS)
    root.mainloop()

#The explaning to compiler.bind('<a shortcut>', command)
# compiler is the name of the tab in proggraming .bind is if the user pressed
# this shortcut then exicute the command
#The shorcuts
#This the shortcut for opening the themes gui
compiler.bind("<Control-h>", OpenMyThemes)
#This the shortcut for opening the text size gui
compiler.bind("<Control-s>", MyTextSize)
#The biggest text size the shortcut is Crtl and +
compiler.bind("<Control-+>", twentyS)
#The normal text size the shortcut is Crtl and n
compiler.bind("<Control-n>", fifteenS)
#The no so big the shortcut is Crtl and l
compiler.bind("<Control-l>", tenS)
#The least big text size the shortcut is Crtl and m
compiler.bind("<Control-m>", oneS)

compiler.bind("<F5>", RunS)




menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run f5', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

getStarted = Menu(menu_bar, tearoff=0)
getStarted.add_command(label='get started with a proggraming language', command=OpenGetStarted)
getStarted.add_command(label='shortcuts', command=OpenGetStarted)
menu_bar.add_cascade(label='GetStarted', menu=getStarted)

theme = Menu(menu_bar, tearoff=0)
theme.add_command(label='size', command=MyTextSize)
theme.add_command(label='themes', command=OpenMyThemes)
menu_bar.add_cascade(label='veiw', menu=theme)

compiler.config(menu=menu_bar)

#This is were you type all your text
#TODO:this is for easy acces to line 314
editor = Text(width=1500)
darkMode=editor.config(bg='#302f2f', fg='red', insertbackground='blue')
editor.pack()
cdg = ic.ColorDelegator()
cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat(), re.S)
cdg.idprog = re.compile(r'\s+(\w+)', re.S)

cdg.prog = re.compile(r'\b(?P<ImportColor>import)\b|' + ic.make_pat(), re.S)
cdg.idprog = re.compile(r'\s+(\w+)', re.S)

cdg.prog = re.compile(r'\b(?P<Classes>class)\b|' + ic.make_pat(), re.S)
cdg.idprog = re.compile(r'\s+(\w+)', re.S)

cdg.tagdefs['MYGROUP'] = {'foreground': '#7F7F7F', 'background': darkMode}
cdg.tagdefs['ImportColor'] = {'foreground': '#AA336A', 'background': darkMode}
cdg.tagdefs['Classes'] = {'foreground': '#0e0ef0', 'background': darkMode}

# These five lines are optional. If omitted, default colours are used.
cdg.tagdefs['COMMENT'] = {'foreground': 'dark green', 'background': darkMode}
#This is for while class def try and more...
cdg.tagdefs['KEYWORD'] = {'foreground': '#ad007f', 'background': darkMode}
cdg.tagdefs['BUILTIN'] = {'foreground': '#00c0ff', 'background': darkMode}
cdg.tagdefs['STRING'] = {'foreground': '#e88725', 'background': darkMode}
cdg.tagdefs['DEFINITION'] = {'foreground': '#1eff00', 'background': darkMode}

ip.Percolator(editor).insertfilter(cdg)



#The code output
code_output = Text(height=20, width=1500)
code_output.config(bg='#1c1c1c', fg='red', foreground='blue')
code_output.pack()

compiler.mainloop()