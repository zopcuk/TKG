import tkinter as tk
from tkinter import ttk
from time import sleep
import os
import serial
import json
import pika
import threading
import fingerprintlib
'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

hid = {4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 14: 'k', 15: 'l', 16: 'm',
       17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 24: 'u', 25: 'v', 26: 'w', 27: 'x', 28: 'y',
       29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7', 37: '8', 38: '9', 39: '0', 44: ' ',
       45: '-', 46: '=', 47: '[', 48: ']', 49: '\\', 51: ';', 52: '\'', 53: '~', 54: ',', 55: '.', 56: '/'}
hid2 = {4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K', 15: 'L', 16: 'M',
        17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V', 26: 'W', 27: 'X', 28: 'Y',
        29: 'Z', 30: '!', 31: '@', 32: '#', 33: '$', 34: '%', 35: '^', 36: '&', 37: '*', 38: '(', 39: ')', 44: ' ',
        45: '_', 46: '+', 47: '{', 48: '}', 49: '|', 51: ':', 52: '"', 53: '~', 54: '<', 55: '>', 56: '?'}

get_id = False
get_rank = False
get_fp = False
id_number = ""
id_number_temp = ""
fp1 = []
fp2 = []
fp3 = []
fp4 = []
fp5 = []
fp6 = []
users = []
loc_max = 0
stop_event = threading.Event()
text_time = 0.25
c = ""

def loc_find():
    global loc_max
    users = []
    for (dirpath, dirnames, filenames) in os.walk("users"):
        users.extend(filenames)
        break
    if len(users) == 0:
        loc_max = 0
    else:
        for i in users:
            with open("users/{}".format(i), 'r') as json_file:
                data = json.load(json_file)
            loc_temp = []
            for p in data['user']:
                loc_temp = p['loc']

            if loc_max < loc_temp[2]:
                loc_max = loc_temp[2]
        loc_max = loc_max + 1


def id_card_read():
    global id_number_temp, get_id
    try:
        while True:
            sleep(1)
            fp = open('/dev/hidraw0', 'rb')
            get_id = False
            shift = False
            done = False

            while not done:
                sleep(.05)
                buffer = fp.read(8)
                for c in buffer:
                    if c > 0:
                        if int(c) == 40:
                            done = True
                            break
                        if shift:
                            if int(c) == 2:
                                shift = True
                            else:
                                id_number_temp += hid2[int(c)]
                                shift = False
                        else:
                            if int(c) == 2:
                                shift = True
                            else:
                                id_number_temp += hid[int(c)]
            fp.close()
            get_id = True
    except:
        pass


def finger_get(location):
    uart = serial.Serial("/dev/ttyS0", baudrate=57600, timeout=1)
    finger = fingerprintlib.Adafruit_Fingerprint(uart)
    for fingerimg in range(1, 3):
        if fingerimg == 1 and not stop_event.is_set():
            # print("Parmağınızı sensöre yerleştirin...", end="", flush=True)
            textLabel2.configure(text="Parmağınızı sensöre yerleştirin...")
            sleep(text_time)
        elif not stop_event.is_set():
            # print("Aynı parmağı tekrar yerleştirin...", end="", flush=True)
            textLabel2.configure(text="Aynı parmağı tekrar yerleştirin...")
            sleep(text_time)
        while not stop_event.is_set() and not stop_event.is_set():
            i = finger.get_image()
            if i == fingerprintlib.OK and not stop_event.is_set():
                # print("Parmak izi alındı")
                textLabel2.configure(text="Parmak izi alındı")
                sleep(text_time)
                break
            if i == fingerprintlib.NOFINGER and not stop_event.is_set():
                # print(".", end="", flush=True)
                # textLabel.configure(text="Bekleniyor")
                pass
            elif i == fingerprintlib.IMAGEFAIL and not stop_event.is_set():
                #print("Görüntü hatası")
                textLabel2.configure(text="Görüntü hatası")
                sleep(text_time)
                return False
            elif not stop_event.is_set():
                #print("Diğer hatalar.")
                textLabel2.configure(text="Diğer hatalar.")
                sleep(text_time)
                return False

        #print("İşleniyor...", end="", flush=True)
        if not stop_event.is_set():
            textLabel2.configure(text="İşleniyor...")
            sleep(text_time)
        i = finger.image_2_tz(fingerimg)
        if i == fingerprintlib.OK and not stop_event.is_set():
            # print("Parmak izi işlendi")
            textLabel2.configure(text="Parmak izi işlendi")
            sleep(text_time)
        else:
            if i == fingerprintlib.IMAGEMESS and not stop_event.is_set():
                # print("Parmak izi çok bulanık")
                textLabel2.configure(text="Parmak izi çok bulanık")
                sleep(text_time)
            elif i == fingerprintlib.FEATUREFAIL and not stop_event.is_set():
                # print("Parmak izi özellikleri tanımlanamadı.")
                textLabel2.configure(text="Parmak izi özellikleri tanımlanamadı.")
                sleep(text_time)
            elif i == fingerprintlib.INVALIDIMAGE and not stop_event.is_set():
                # print("Parmak izi geçersiz.")
                textLabel2.configure(text="Parmak izi geçersiz.")
                sleep(text_time)
            elif not stop_event.is_set():
                # print("Diğer hatalar.")
                textLabel2.configure(text="Diğer hatalar.")
                sleep(text_time)
            return False

        if not stop_event.is_set():
            #print("Parmağınızı kaldırın !!")
            textLabel2.configure(text="Parmağınızı kaldırın !!")
            sleep(text_time)
            sleep(1)
            while i != fingerprintlib.NOFINGER and not stop_event.is_set():
                i = finger.get_image()

    # print("Parmak izleri eşleştiriliyor...", end="", flush=True)
    textLabel2.configure(text="Parmak izleri eşleştiriliyor...")
    sleep(text_time)
    fp_buffer1 = finger.get_fpdata("char", 1)
    fp_buffer2 = finger.get_fpdata("char", 2)
    i = finger.create_model()
    if i == fingerprintlib.OK and not stop_event.is_set():
        # print("Parmak izleri eşleşdi")
        textLabel2.configure(text="Parmak izleri eşleşdi")
        sleep(text_time)
    else:
        if i == fingerprintlib.ENROLLMISMATCH and not stop_event.is_set():
            # print("Parmak izleri eşleşmedi")
            textLabel2.configure(text="Parmak izleri eşleşmedi", foreground="red")
            sleep(text_time + text_time)
            textLabel2.configure(text="", foreground="black")

        elif not stop_event.is_set():
            # print("Diğer hatalar")
            textLabel2.configure(text="Diğer hatalar.")
            sleep(text_time)
        return False, False

    # print("Model no #%d..." % location)
    i = finger.store_model(location)
    if i == fingerprintlib.OK and not stop_event.is_set():
        # print("Stored")

        return fp_buffer1, fp_buffer2
    else:
        if i == fingerprintlib.BADLOCATION and not stop_event.is_set():
            # print("Bad storage location")
            textLabel2.configure(text="Konum hatası.")
            sleep(text_time)
        elif i == fingerprintlib.FLASHERR and not stop_event.is_set():
            # print("Flash storage error")
            textLabel2.configure(text="Hafıza hatası.")
            sleep(text_time)
        elif not stop_event.is_set():
            # print("Other error")
            textLabel2.configure(text="Diğer hatalar.")
            sleep(text_time)
        return False


def user_save():
    global fp1, fp2, fp3, fp4, fp5, fp6, id_number, rank, loc_max
    # print("Bilgiler kaydediliyor lütfen bekleyin...")
    textLabel2.configure(text="Bilgiler kaydediliyor lütfen bekleyin...")
    sleep(text_time)
    data = {}
    data['user'] = []
    data['user'].append({
        'loc': [loc_max, (loc_max + 1), (loc_max + 2)],
        'id': id_number,
        'rank': rank,
        'fp1': fp1,
        'fp2': fp2,
        'fp3': fp3,
        'fp4': fp4,
        'fp5': fp5,
        'fp6': fp6
    })

    with open('users/{}.json'.format(id_number), 'w') as outfile:
        json.dump(data, outfile)
    # print("Kullanıcı bilgileri kaydedildi")
    textLabel2.configure(text="Kullanıcı bilgileri kaydedildi")
    sleep(text_time)

    try:
        credentials = pika.PlainCredentials(username='test', password='test')
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', credentials=credentials))
        channel = connection.channel()
        channel.exchange_declare(exchange='logs', exchange_type='fanout')
        message = json.dumps(data)
        channel.basic_publish(exchange='logs', routing_key='', body=message)
        connection.close()
        # print("Kullanıcı bilgileri dağıtıldı.")
    except:
        pass
    win.destroy()


def register():
    global fp1, fp2, fp3, fp4, fp5, fp6, id_number, id_number_temp, rank, loc_max, get_id, get_rank
    id_number = ""
    id_number_temp = ""
    # print("Yeni Kayıt için : r || Kişi silmek için d tuşuna basınız. ")
    textLabel.configure(text="Kartı okutunuz")
    textLabel2.configure(text="Bekleniyor...")
    while not stop_event.is_set() and not get_id:
        sleep(.1)
    id_number = id_number_temp
    textLabel2.configure(text="Kart okundu")
    users = []
    for (dirpath, dirnames, filenames) in os.walk("users"):
        users.extend(filenames)
        break
    if c == "d":
        if "{}.json".format(id_number) in users:
            textLabel2.configure(text="Kullanıcı siliniyor.")
            sleep(text_time)
            os.remove("users/{}.json".format(id_number))
            textLabel2.configure(text="Kullanıcı silindi.")
            sleep(text_time*2)
        else:
            textLabel2.configure(text="Tanımsız Kart !")
            sleep(text_time * 2)
        win.destroy()
    if c == "r":
        if "{}.json".format(id_number) in users:
            textLabel.configure(text="Bu kart tanımlıdır !!")
            textLabel2.configure(text="Lütfen önce kayıtı siliniz.")
            sleep(text_time*6)
            win.destroy()
        # id_number = input("> ")
        '''textLabel.configure(text="Kullanıcının yetkisini giriniz")
        root_tk()
        while not stop_event.is_set() and not get_rank:
            sleep(.1)'''

        loc_find()
        i = 0
        parmak = ""
        while not stop_event.is_set():
            if i == 0:
                parmak = "BAŞ"
            if i == 1:
                parmak = "İŞARET"
            if i == 2:
                parmak = "ORTA"
            # print("{} PARMAK İZİ İÇİN!!".format(parmak))
            textLabel.configure(text="{} PARMAK İZİ İÇİN!!".format(parmak))
            fp_buffer1, fp_buffer2 = finger_get(loc_max + i)
            if fp_buffer2 != False:
                if i == 0:
                    fp1 = fp_buffer1
                    fp2 = fp_buffer2
                elif i == 1:
                    fp3 = fp_buffer1
                    fp4 = fp_buffer2
                elif i == 2:
                    fp5 = fp_buffer1
                    fp6 = fp_buffer2

            if fp_buffer2 != False:
                i += 1

            if i == 3 or stop_event.is_set():
                break

        if i == 3 and not stop_event.is_set():
            user_save()

'''////////////////////////////////////////'''


def exit(event):
    root.destroy()


def root_tk():

    def exit(event):
        root.destroy()

    def limitSizeDay(*args):
        value1 = password1.get()
        if len(value1) > 3: password1.set(value1[:4])

    root = tk.Toplevel()
    w = 375
    h = root.winfo_screenheight()
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
    rootColor = "#7c9a92"
    buttoncolor = "#314448"
    cancelColor = "#b22222"
    font = "Helvetica 36"
    textFont = "Courier 16"

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
    entry1 = tk.Entry(passwordlabel1, textvariable=password1, highlightthickness=0, width=8, show="", font=textFont,
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
        global get_rank
        get_rank = False
        root.destroy()

    def get_entry():
        global get_rank, rank
        if entry1.get() != "":
            rank = entry1.get()
            get_rank = True
            root.destroy()
            resetButton()
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
                    activebackground=buttoncolor, command=get_entry)
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
    cancelButton = tk.Button(cancelLabel, text="CANCEL", width=20, font="Courier 16", bg=cancelColor, border=0,
                             highlightthickness=0, activebackground=cancelColor, command=cancel)
    cancelButton.grid(column=0, row=0, sticky="nsew")
    root.config(cursor='none')
    root.bind("<Escape>", exit)
    root.mainloop()
'''////////////////////////////////////////'''


def resetButton():
    global textLabel, textLabel2, win, c

    def cancel():
        stop_event.set()
        win.destroy()
    winColor = "#314448"
    cancelColor = "#b22222"
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
    winFrame.rowconfigure(0, weight=1)
    winFrame.rowconfigure(1, weight=2)
    winFrame.rowconfigure(2, weight=2)
    winFrame.rowconfigure(3, weight=1)
    '''//////////////////////////////////'''
    if c == "r":
        headLabel = tk.Label(winFrame, text="YENİ KAYIT", bg=winColor, font="Courier 18",
                             border=0, highlightthickness=0)
    else:
        headLabel = tk.Label(winFrame, text="KAYIT SİLME", bg=winColor, font="Courier 18",
                             border=0, highlightthickness=0)
    headLabel.grid(row=0, column=0, sticky="ewsn")

    textLabel = tk.Label(winFrame, text="", bg=winColor, font="Courier 16",
                         border=0, highlightthickness=0)
    textLabel.grid(row=1, column=0, sticky="ewsn")

    textLabel2 = tk.Label(winFrame, text="", bg=winColor, border=0, highlightthickness=0, font="Courier 14")
    textLabel2.grid(row=2, column=0, sticky="ewsn")

    cancelLabel = tk.Label(winFrame, bg=cancelColor)
    cancelLabel.grid(column=0, row=3, sticky="ewsn")
    cancelLabel.columnconfigure(0, weight=1)
    cancelLabel.rowconfigure(0, weight=1)
    cancelButton = tk.Button(cancelLabel, text="CANCEL", font="Courier 16", bg=cancelColor, border=0,
                             highlightthickness=0, activebackground=cancelColor, command=cancel)
    cancelButton.grid(column=0, row=0, sticky="nsew")
    win.bind("<Escape>", exit)

    APP = threading.Thread(target=register)
    APP.daemon = True
    APP.start()
    win.config(cursor='none')
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
back_color = "#e0dab8"
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
menulabel = tk.Label(content, border=0, bg="#e0dab8")
menulabel.grid(column=1, row=0, sticky="ewsn")
menulabel.columnconfigure(0, weight=1)
menulabel.rowconfigure(0, weight=1)
menulabel.rowconfigure(1, weight=1)
menulabel.rowconfigure(2, weight=1)
'''//////////////////////////////////////'''
kayit_button = tk.Button(menulabel, text="Kullanıcı Ekle", bg=reg_color, border=1, highlightthickness=0, font=font,
                         activebackground=reg_color)
kayit_button.grid(column=0, row=0)


def kayit_press(event):
    kayit_button.configure(bg=activecolor, activebackground=activecolor)


def kayit_release(event):
    global c
    c = "r"
    kayit_button.configure(bg=reg_color, activebackground=reg_color)
    stop_event.clear()
    root_tk()


kayit_button.bind("<ButtonPress>", kayit_press)
kayit_button.bind("<ButtonRelease>", kayit_release)
'''//////////////////////////////////////'''
sync_icon = tk.PhotoImage(file=r"cloud-server.png")
sync_icon = sync_icon.subsample(5, 5)
sync_button = tk.Button(menulabel, image=sync_icon, bg=sync_color, border=1, highlightthickness=0, font=font,
                        activebackground=sync_color)
sync_button.grid(column=0, row=1, ipadx=120, ipady=5)


def sync_press(event):
    sync_button.configure(bg=activecolor, activebackground=activecolor)


def sync_release(event):
    sync_button.configure(bg=sync_color, activebackground=sync_color)


sync_button.bind("<ButtonPress>", sync_press)
sync_button.bind("<ButtonRelease>", sync_release)
'''//////////////////////////////////////'''
delete_button = tk.Button(menulabel, text=" Kullanıcı Sil ", bg=del_color, border=1, highlightthickness=0, font=font,
                          activebackground=del_color)
delete_button.grid(column=0, row=2)


def delete_press(event):
    delete_button.configure(bg=activecolor, activebackground=activecolor)


def delete_release(event):
    global c
    c = "d"
    delete_button.configure(bg=del_color, activebackground=del_color)
    stop_event.clear()
    resetButton()

delete_button.bind("<ButtonPress>", delete_press)
delete_button.bind("<ButtonRelease>", delete_release)
'''//////////////////////////////////////'''
root.bind("<Escape>", exit)
APP2 = threading.Thread(target=id_card_read)
APP2.daemon = True
APP2.start()
root.config(cursor='none')
root.mainloop()