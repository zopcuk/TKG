import tkinter as tk
from tkinter import ttk

'''////////////////////////////////////////'''


def exit(event):
    root.destroy()
'''////////////////////////////////////////'''


def root_tk():

    def exit(event):
        root.destroy()

    def limitSizeDay(*args):
        value1 = password1.get()
        if len(value1) > 3: password1.set(value1[:4])

    root = tk.Toplevel()
    w = 425
    h = root.winfo_screenheight()-100
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.overrideredirect(True)
    root.wm_attributes('-topmost', 'true')
    root.grab_set()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    '''///////////////////////////////////////'''
    rootColor = "#189ad3"
    buttoncolor = "#107dac"
    cancelColor = "#f09609"
    font = "Helvetica 36"
    textFont = "Helvetica 20"

    password1 = tk.StringVar()  # Password variable
    password1.trace('w', limitSizeDay)
    '''//////////////////////////////////////'''
    content = ttk.Frame(root)
    content.grid(column=0, row=0, sticky="nsew")
    content.columnconfigure(0, weight=1)
    content.rowconfigure(0, weight=2)
    content.rowconfigure(1, weight=5)
    content.rowconfigure(2, weight=1)
    '''/////////////////////////////////////////'''
    okey = tk.PhotoImage(file=r"checked.png")
    okey = okey.subsample(7, 7)

    delete = tk.PhotoImage(file=r"backspace.png")
    delete = delete.subsample(6, 6)
    '''////////////////////////////////////////'''
    passwordlabel1 = tk.Label(content, bg=rootColor)
    passwordlabel1.grid(column=0, row=0, sticky="ewsn")
    passwordlabel1.columnconfigure(0, weight=2)
    passwordlabel1.columnconfigure(1, weight=3)
    passwordlabel1.rowconfigure(0, weight=1)
    textLabel1 = tk.Label(passwordlabel1, text="Kullanıcı Yetkisi :", bg=rootColor, font=textFont)
    textLabel1.grid(column=0, row=0, sticky="e")
    entry1 = tk.Entry(passwordlabel1, textvariable=password1, highlightthickness=0, width=10, show="", font=textFont,
                      border=0, disabledbackground=buttoncolor)
    entry1.grid(column=1, row=0, sticky="w")
    '''///////////////////////////////////////////////'''
    numbersLabel = tk.Label(content, bg=buttoncolor)
    numbersLabel.grid(column=0, row=1, sticky="ewsn")
    numbersLabel.columnconfigure(0, weight=2)
    numbersLabel.columnconfigure(1, weight=2)
    numbersLabel.columnconfigure(2, weight=2)
    numbersLabel.columnconfigure(3, weight=2)
    numbersLabel.columnconfigure(4, weight=2)
    numbersLabel.rowconfigure(0, weight=2)
    numbersLabel.rowconfigure(1, weight=2)
    numbersLabel.rowconfigure(2, weight=2)
    numbersLabel.rowconfigure(3, weight=2)

    def deleteNumber():
        entry1.delete(len(entry1.get()) - 1, tk.END)

    def cancel():
        root.destroy()

    def get_rank():
        if entry1.get() != "":
            print(entry1.get())
            root.destroy()
        else:
            pass
    b1 = tk.Button(numbersLabel, text="1", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font=font, command=lambda: entry1.insert(tk.END, "1"))
    b1.grid(column=1, row=0)

    b2 = tk.Button(numbersLabel, text="2",bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font=font, command=lambda: entry1.insert(tk.END, "2"))
    b2.grid(column=2, row=0)

    b3 = tk.Button(numbersLabel, text="3", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font=font, command=lambda: entry1.insert(tk.END, "3"))
    b3.grid(column=3, row=0)

    b4 = tk.Button(numbersLabel, text="4", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font=font, command=lambda: entry1.insert(tk.END, "4"))
    b4.grid(column=1, row=1)

    b5 = tk.Button(numbersLabel, text="5", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font=font, command=lambda: entry1.insert(tk.END, "5"))
    b5.grid(column=2, row=1)

    b6 = tk.Button(numbersLabel, text="6", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font=font, command=lambda: entry1.insert(tk.END, "6"))
    b6.grid(column=3, row=1)

    b7 = tk.Button(numbersLabel, text="7", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font=font, command=lambda: entry1.insert(tk.END, "7"))
    b7.grid(column=1, row=2)

    b8 = tk.Button(numbersLabel, text="8", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font=font, command=lambda: entry1.insert(tk.END, "8"))
    b8.grid(column=2, row=2)

    b9 = tk.Button(numbersLabel, text="9", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font=font, command=lambda: entry1.insert(tk.END, "9"))
    b9.grid(column=3, row=2)

    bok = tk.Button(numbersLabel, image=okey, bg=buttoncolor, width=7, border=0, highlightthickness=0,
                    activebackground=buttoncolor, command=get_rank)
    bok.grid(column=1, row=3, sticky="ewns")

    b0 = tk.Button(numbersLabel, text="0", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font=font, command=lambda: entry1.insert(tk.END, "0"))
    b0.grid(column=2, row=3)

    bdel = tk.Button(numbersLabel, image=delete, bg=buttoncolor, width=7, border=0, highlightthickness=0,
                     activebackground=buttoncolor, command=deleteNumber)
    bdel.grid(column=3, row=3, sticky="ewns")
    '''///////////////////////////////////////////'''
    cancelLabel = tk.Label(content, bg=cancelColor)
    cancelLabel.grid(column=0, row=2, sticky="ewsn")
    cancelLabel.columnconfigure(0, weight=1)
    cancelLabel.rowconfigure(0, weight=1)
    cancelButton = tk.Button(cancelLabel, text="CANCEL", width=20, font="Helvetica 20 bold", bg=cancelColor, border=0,
                             highlightthickness=0, activebackground=cancelColor, command=cancel)
    cancelButton.grid(column=0, row=0, sticky="nsew")

    root.bind("<Escape>", exit)
    root.mainloop()
'''////////////////////////////////////////'''


def resetButton():
    global textLabel

    def cancel():
        win.destroy()
    winColor = "#106181"
    cancelColor = "#f09609"
    win = tk.Toplevel(background=winColor)
    win.wm_title("Home Position")
    w = 425
    h = 275
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    win.geometry('%dx%d+%d+%d' % (w, h, x, y))
    win.overrideredirect(True)
    win.wm_attributes('-topmost', 'true')
    win.grab_set()
    win.columnconfigure(0, weight=1)
    win.rowconfigure(0, weight=1)
    '''//////////////////////////////////'''
    s = ttk.Style()
    s.configure('new.TFrame', background=winColor, highlightcolor=winColor, highlightthickness=3, bd=3)
    winFrame = ttk.Frame(win, style='new.TFrame')
    winFrame.grid(column=0, row=0, sticky="nsew")
    winFrame.columnconfigure(0, weight=1)
    winFrame.rowconfigure(0, weight=2)
    winFrame.rowconfigure(1, weight=2)
    winFrame.rowconfigure(2, weight=1)
    winFrame.rowconfigure(3, weight=2)
    '''//////////////////////////////////'''

    headLabel = tk.Label(winFrame, text="KAYIT", bg=winColor, font="Courier 18",
                         border=0, highlightthickness=0)
    headLabel.grid(row=0, column=0, sticky="ewsn")

    textLabel = tk.Label(winFrame, text="Tekrar aynı\nparmağınızı okutunuz", bg=winColor, font="Courier 16",
                         border=0, highlightthickness=0)
    textLabel.grid(row=1, column=0, sticky="ewsn")

    spacer = tk.Label(winFrame, bg=winColor, border=0, highlightthickness=0)
    spacer.grid(row=2, column=0, sticky="ewsn")

    cancelLabel = tk.Label(winFrame, bg=cancelColor)
    cancelLabel.grid(column=0, row=3, sticky="ewsn")
    cancelLabel.columnconfigure(0, weight=1)
    cancelLabel.rowconfigure(0, weight=1)
    cancelButton = tk.Button(cancelLabel, text="CANCEL", font="Courier 16", bg=cancelColor, border=0,
                             highlightthickness=0, activebackground=cancelColor, command=cancel)
    cancelButton.grid(column=0, row=0, sticky="nsew")
    win.bind("<Escape>", exit)

    win.mainloop()
    '''////////////////////////////////////////////////////////////////'''



'''////////////////////////////////////////'''
root = tk.Tk()
root.title("INFO")
root.wm_attributes('-fullscreen', 'true')
root.wm_attributes('-topmost', 'true')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
'''///////////////////////////////////////'''
reg_color= "#7c9a92"
del_color = "#7c9a92"
sync_color = "#7c9a92"
side_color = "#314448"
activecolor="#6ea023"
font = "Helvetica 40"

'''//////////////////////////////////////'''
content = ttk.Frame(root)
content.grid(column=0, row=0, sticky="nsew")
content.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=4)
content.columnconfigure(2, weight=1)
'''//////////////////////////////////////'''
sidelabel1 = tk.Label(content, bg=side_color)
sidelabel1.grid(column=0, row=0, sticky="ewns")
sidelabel2 = tk.Label(content, bg=side_color)
sidelabel2.grid(column=2, row=0, sticky="ewns")
'''//////////////////////////////////////'''
menulabel = tk.Label(content, text="Kartı okutunuz", border=0, bg="#e0dab8")
menulabel.grid(column=1, row=0, sticky="ewsn")
menulabel.columnconfigure(0, weight=1)
menulabel.rowconfigure(0, weight=1)
menulabel.rowconfigure(1, weight=1)
menulabel.rowconfigure(2, weight=1)
'''//////////////////////////////////////'''
kayit = tk.Button(menulabel, text="Kullanıcı Ekle", bg=reg_color, border=1, highlightthickness=0, font=font,
                         activebackground=activecolor, command=root_tk)
kayit.grid(column=0, row=0)

'''//////////////////////////////////////'''
sync_icon = tk.PhotoImage(file=r"cloud-server.png")
sync_icon = sync_icon.subsample(5, 5)
sync_button = tk.Button(menulabel, image=sync_icon, bg=sync_color, border=1, highlightthickness=0, font=font,
                        activebackground=activecolor)
sync_button.grid(column=0, row=1, ipadx=120,ipady=5)
'''//////////////////////////////////////'''
delete = tk.Button(menulabel, text=" Kullanıcı Sil ", bg=del_color, border=1, highlightthickness=0, font=font,
                         activebackground=activecolor, command=resetButton)
delete.grid(column=0, row=2)
'''//////////////////////////////////////'''
root.bind("<Escape>", exit)
#
# root.config(cursor='none')
root.mainloop()