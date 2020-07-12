from tkinter import ttk
import tkinter as tk
import configparser
from time import sleep
config = configparser.ConfigParser()
config.read('config.ini')

def root_tk():
    def exit(event):
        root.destroy()
    def limitSizeDay(*args):
        value1 = password1.get()
        if len(value1) > 3: password1.set(value1[:4])
        value2 = password2.get()
        if len(value2) > 3: password2.set(value2[:4])
        value3 = password3.get()
        if len(value3) > 3: password3.set(value3[:4])

    root = tk.Toplevel()
    #root.wm_attributes('-fullscreen', 'true')
    #root.wm_attributes('-topmost', 'true')
    w = 475
    h = 600
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
    cancelColor = "#f09609" #"#ff5722"
    activeColor = "#f09609"
    font = "Helvetica 36 bold"
    textFont = "Helvetica 20 bold"
    entryFont = "Helvetica 20 bold"

    password1 = tk.StringVar()  # Password variable
    password1.trace('w', limitSizeDay)

    password2 = tk.StringVar()  # Password variable
    password2.trace('w', limitSizeDay)

    password3 = tk.StringVar()  # Password variable
    password3.trace('w', limitSizeDay)

    config.read('config.ini')
    parola = config.get('section_a', 'parola')
    admin_parola = config.get('section_a', 'admin_parola')

    '''//////////////////////////////////////'''
    content = ttk.Frame(root)
    content.grid(column=0, row=0, sticky="nsew")
    content.columnconfigure(0, weight=1)
    content.rowconfigure(0, weight=1)
    content.rowconfigure(1, weight=2)
    content.rowconfigure(2, weight=2)
    content.rowconfigure(3, weight=2)
    content.rowconfigure(4, weight=5)
    content.rowconfigure(5, weight=1)
    '''/////////////////////////////////////////'''
    okey = tk.PhotoImage(file=r"checkbox.png")
    okey = okey.subsample(7, 7)

    delete = tk.PhotoImage(file=r"delete.png")
    delete = delete.subsample(6, 6)
    '''////////////////////////////////////////'''
    headlabel = tk.Label(content, text="YENİ KAYIT", bg=rootColor, font="Helvetica 30 bold")
    headlabel.grid(column=0, row=0, sticky="ewsn")
    '''/////////////////////////////////////////'''
    headlabel2 = tk.Label(content, text="Kartı okutunuz", bg=rootColor, font="Helvetica 20 bold",
                          foreground=activeColor)
    headlabel2.grid(column=0, row=1, sticky="ewsn")
    '''/////////////////////////////////////////'''
    '''passwordlabel1 = tk.Label(content, bg=activeColor)
    passwordlabel1.grid(column=0, row=1, sticky="ewsn")
    passwordlabel1.columnconfigure(0, weight=2)
    passwordlabel1.columnconfigure(1, weight=3)
    passwordlabel1.rowconfigure(0, weight=1)
    textLabel1 = tk.Label(passwordlabel1, text="    Enter Password :", bg=activeColor, font=textFont)
    textLabel1.grid(column=0, row=0, sticky="e")
    entry1 = tk.Entry(passwordlabel1, textvariable=password1, highlightthickness=0, width=15, show="*", font=entryFont,
                      border=0, disabledbackground=buttoncolor)
    entry1.grid(column=1, row=0, sticky="w")'''
    '''///////////////////////////////////////'''
    passwordlabel2 = tk.Label(content, bg=rootColor)
    passwordlabel2.grid(column=0, row=2, sticky="ewsn")
    passwordlabel2.columnconfigure(0, weight=2)
    passwordlabel2.columnconfigure(1, weight=3)
    passwordlabel2.rowconfigure(0, weight=1)
    '''textLabel2 = tk.Label(passwordlabel2, text="      New Password :", bg=rootColor,font=textFont)
    textLabel2.grid(column=0, row=0, sticky="e")
    entry2 = tk.Entry(passwordlabel2, textvariable=password2, highlightthickness=0, state=tk.DISABLED, width=15,
                      show="*", font=entryFont, border=0, disabledbackground=buttoncolor)
    entry2.grid(column=1, row=0, sticky="w")'''
    '''/////////////////////////////////////////'''
    passwordlabel3 = tk.Label(content, bg=rootColor)
    passwordlabel3.grid(column=0, row=3, sticky="ewsn")
    passwordlabel3.columnconfigure(0, weight=2)
    passwordlabel3.columnconfigure(1, weight=3)
    passwordlabel3.rowconfigure(0, weight=1)
    textLabel3 = tk.Label(passwordlabel3, text="Kullanıcı Yetkisi :", bg=rootColor, font=textFont)
    textLabel3.grid(column=0, row=0, sticky="e")
    entry3 = tk.Entry(passwordlabel3, textvariable=password3, highlightthickness=0, state=tk.DISABLED, width=15,
                      show="*", font=entryFont, border=0, disabledbackground=buttoncolor)
    entry3.grid(column=1, row=0, sticky="w")
    '''///////////////////////////////////////////////'''
    numbersLabel = tk.Label(content, bg=buttoncolor)
    numbersLabel.grid(column=0, row=4, sticky="ewsn")
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
        entry2.delete(len(entry2.get()) - 1, tk.END)
        entry3.delete(len(entry3.get()) - 1, tk.END)
    def cancel():
        root.destroy()
    def activateEntry2():
        passwordlabel1.configure(bg=rootColor)
        textLabel1.configure(bg=rootColor)
        passwordlabel2.configure(bg=activeColor)
        textLabel2.configure(bg=activeColor)
        passwordlabel3.configure(bg=rootColor)
        textLabel3.configure(bg=rootColor)
        entry1.configure(state=tk.DISABLED)
        entry2.configure(state=tk.NORMAL)
        entry3.configure(state=tk.DISABLED)
        b0.configure(command=lambda: entry2.insert(tk.END, "0"))
        b1.configure(command=lambda: entry2.insert(tk.END, "1"))
        b2.configure(command=lambda: entry2.insert(tk.END, "2"))
        b3.configure(command=lambda: entry2.insert(tk.END, "3"))
        b4.configure(command=lambda: entry2.insert(tk.END, "4"))
        b5.configure(command=lambda: entry2.insert(tk.END, "5"))
        b6.configure(command=lambda: entry2.insert(tk.END, "6"))
        b7.configure(command=lambda: entry2.insert(tk.END, "7"))
        b8.configure(command=lambda: entry2.insert(tk.END, "8"))
        b9.configure(command=lambda: entry2.insert(tk.END, "9"))
    def activateEntry3():
        passwordlabel1.configure(bg=rootColor)
        textLabel1.configure(bg=rootColor)
        passwordlabel2.configure(bg=rootColor)
        textLabel2.configure(bg=rootColor)
        passwordlabel3.configure(bg=activeColor)
        textLabel3.configure(bg=activeColor)
        entry1.configure(state=tk.DISABLED)
        entry2.configure(state=tk.DISABLED)
        entry3.configure(state=tk.NORMAL)
        b0.configure(command=lambda: entry3.insert(tk.END, "0"))
        b1.configure(command=lambda: entry3.insert(tk.END, "1"))
        b2.configure(command=lambda: entry3.insert(tk.END, "2"))
        b3.configure(command=lambda: entry3.insert(tk.END, "3"))
        b4.configure(command=lambda: entry3.insert(tk.END, "4"))
        b5.configure(command=lambda: entry3.insert(tk.END, "5"))
        b6.configure(command=lambda: entry3.insert(tk.END, "6"))
        b7.configure(command=lambda: entry3.insert(tk.END, "7"))
        b8.configure(command=lambda: entry3.insert(tk.END, "8"))
        b9.configure(command=lambda: entry3.insert(tk.END, "9"))
    def changePassword():
        sleep(2)
        config.set("section_a", "parola", entry3.get())
        with open("config.ini", 'w') as configfile:
            config.write(configfile)
        root.destroy()
    def com():
        if entry1.get() == parola and len(entry2.get())==0 and len(entry3.get())==0 or entry1.get() == admin_parola and len(entry2.get())==0 and len(entry3.get())==0:
            activateEntry2()
        else:
            entry1.delete(0, tk.END)
        if len(entry2.get())==4 and len(entry3.get())==0:
            activateEntry3()
        else:
            entry2.delete(0, tk.END)
        if len(entry2.get())==4 and len(entry3.get())==4 and entry3.get()==entry2.get():
            headlabel.configure(text="PASSWORD CHANGED",bg="#639a67")
            root.update()
            changePassword()
        elif len(entry2.get())==4 and entry3.get()!=entry2.get() and len(entry3.get())>0:
            entry3.delete(0, tk.END)
            activateEntry2()
            entry2.delete(0, tk.END)
    b1 = tk.Button(numbersLabel, text="1", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   font=font, command=lambda: entry1.insert(tk.END, "1"))
    b1.grid(column=1, row=0)

    b2 = tk.Button(numbersLabel, text="2",bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   font=font, command=lambda: entry1.insert(tk.END, "2"))
    b2.grid(column=2, row=0)

    b3 = tk.Button(numbersLabel, text="3", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   font=font, command=lambda: entry1.insert(tk.END, "3"))
    b3.grid(column=3, row=0)

    b4 = tk.Button(numbersLabel, text="4", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   font=font, command=lambda: entry1.insert(tk.END, "4"))
    b4.grid(column=1, row=1)

    b5 = tk.Button(numbersLabel, text="5", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   font=font, command=lambda: entry1.insert(tk.END, "5"))
    b5.grid(column=2, row=1)

    b6 = tk.Button(numbersLabel, text="6", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   font=font, command=lambda: entry1.insert(tk.END, "6"))
    b6.grid(column=3, row=1)

    b7 = tk.Button(numbersLabel, text="7", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   font=font, command=lambda: entry1.insert(tk.END, "7"))
    b7.grid(column=1, row=2)

    b8 = tk.Button(numbersLabel, text="8", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   font=font, command=lambda: entry1.insert(tk.END, "8"))
    b8.grid(column=2, row=2)

    b9 = tk.Button(numbersLabel, text="9", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   font=font, command=lambda: entry1.insert(tk.END, "9"))
    b9.grid(column=3, row=2)

    bok = tk.Button(numbersLabel, image=okey, bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   command=com)
    bok.grid(column=1, row=3, sticky="ewns")

    b0 = tk.Button(numbersLabel, text="0", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                      font=font, command=lambda: entry1.insert(tk.END, "0"))
    b0.grid(column=2, row=3)

    bdel = tk.Button(numbersLabel, image=delete, bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                      command=deleteNumber)
    bdel.grid(column=3, row=3, sticky="ewns")
    '''///////////////////////////////////////////'''
    cancelLabel = tk.Label(content, bg=cancelColor)
    cancelLabel.grid(column=0, row=5, sticky="ewsn")
    cancelLabel.columnconfigure(0, weight=1)
    cancelLabel.rowconfigure(0, weight=1)
    cancelButton = tk.Button(cancelLabel, text="CANCEL", width=20, font="Helvetica 20 bold", bg=cancelColor, border=0,
                             highlightthickness=0, activebackground=cancelColor, command=cancel)
    cancelButton.grid(column=0, row=0, sticky="nsew")

    root.bind("<Escape>", exit)
    root.config(cursor='none')
    root.mainloop()

