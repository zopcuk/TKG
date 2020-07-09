import tkinter as tk
from tkinter import ttk

def exit(event):
    info.destroy()
def resetButton():
    winColor = "#106181"
    bottomColor = "#106181"
    yesColor = "#51719c"
    noColor = "#51719c"
    win = tk.Toplevel(background=winColor)
    win.wm_title("Home Position")
    w = 475
    h = 225
    ws = info.winfo_screenwidth()
    hs = info.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    win.geometry('%dx%d+%d+%d' % (w, h, x, y))
    win.overrideredirect(True)
    win.wm_attributes('-topmost', 'true')
    win.grab_set()
    s = ttk.Style()
    s.configure('new.TFrame', background=winColor, highlightcolor=winColor, highlightthickness=3, bd=3)
    winFrame = ttk.Frame(win, style='new.TFrame')
    '''//////////////////////////////////'''
    def yesButton():
        global dutyCycle
        textLabel.configure(text="Please wait..!", foreground=timeLabelColor)
        win.update()
        win.destroy()

    headLabel = tk.Label(winFrame, text="Reset Positions", bg=winColor, font="Courier 18")
    textLabel = tk.Label(winFrame, text="Are you sure?", bg=winColor, font="Courier 16")

    yesLabel = tk.Label(winFrame, bg=bottomColor)
    yesLabel.grid(row=2, column=0, sticky='ewns', columnspan=1)
    b_yes = tk.Button(winFrame, text="OK", bg=bottomColor, border=0, highlightthickness=0,
                      activebackground=bottomColor, command=yesButton)

    noLabel = tk.Label(winFrame, bg=bottomColor)
    noLabel.grid(row=2, column=4, sticky='ewns', columnspan=1)
    b_no = tk.Button(winFrame, text="cancel", bg=bottomColor, border=0, highlightthickness=0,
                     activebackground=bottomColor, command=win.destroy)

    area1 = tk.Label(winFrame, bg=bottomColor)
    area1.grid(row=2, column=1, sticky='ewns', columnspan=1)
    area2 = tk.Label(winFrame, bg=bottomColor)
    area2.grid(row=2, column=2, sticky='ewns', columnspan=1)
    area3 = tk.Label(winFrame, bg=bottomColor)
    area3.grid(row=2, column=3, sticky='ewns', columnspan=1)
    '''////////////////////////////////////////////////////////////////'''

    winFrame.grid(column=0, row=0, sticky="nsew")
    headLabel.grid(row=0, column=2)
    textLabel.grid(row=1, column=2)
    b_yes.grid(row=2, column=0)
    b_no.grid(row=2, column=4)

    win.columnconfigure(0, weight=1)
    win.rowconfigure(0, weight=1)
    winFrame.columnconfigure(0, weight=2)
    winFrame.columnconfigure(1, weight=0)
    winFrame.columnconfigure(2, weight=2)
    winFrame.columnconfigure(3, weight=0)
    winFrame.columnconfigure(4, weight=2)
    winFrame.rowconfigure(0, weight=2)
    winFrame.rowconfigure(1, weight=2)
    winFrame.rowconfigure(2, weight=2)
    win.bind("<Escape>", exit)

info = tk.Tk()

info.title("INFO")
info.wm_attributes('-fullscreen', 'true')
#info.wm_attributes('-topmost', 'true')
info.columnconfigure(0, weight=1)
info.rowconfigure(0, weight=1)
'''///////////////////////////////////////'''
rootColor = "#107dac" #51719c
buttoncolor = "#106181"
cancelColor = rootColor #ff5722
activeColor = "#f09609"
font = "Helvetica 22 bold"
textFont = "Helvetica 26 bold"
valueFont = "Helvetica 20 bold"
stepLabelColor = "#189ad3"
distanceLabelColor = "#1ebbd7"
speedLabelColor = "#1ebbd7"
timeLabelColor = "#189ad3"



'''//////////////////////////////////////'''
content = ttk.Frame(info)
content.grid(column=0, row=0, sticky="nsew")
content.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=1)
content.columnconfigure(2, weight=1)
'''//////////////////////////////////////'''
kayit = tk.Button(content, text="Yeni Kullanıcı", bg=speedLabelColor, border=2, highlightthickness=0, font=textFont,
                         activebackground=timeLabelColor, command=resetButton)
kayit.grid(column=0, row=0, ipadx=50, ipady=50)

'''//////////////////////////////////////'''
delete = tk.Button(content, text="Kullanıcı Sil", bg=speedLabelColor, border=2, highlightthickness=0, font=textFont,
                         activebackground=timeLabelColor)
delete.grid(column=2, row=0, ipadx=50, ipady=50)
'''//////////////////////////////////////'''

info.bind("<Escape>", exit)


info.mainloop()