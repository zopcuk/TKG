from time import sleep
from os import walk
import serial
import json
import threading
from pyModbusTCP.client import ModbusClient
import fingerprintlib

SERVER_HOST = "192.168.1.5"
SERVER_PORT = 502
c = ModbusClient()
c.host(SERVER_HOST)
c.port(SERVER_PORT)
hid = {4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 14: 'k', 15: 'l', 16: 'm', 17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 24: 'u', 25: 'v', 26: 'w', 27: 'x', 28: 'y', 29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7', 37: '8', 38: '9', 39: '0', 44: ' ', 45: '-', 46: '=', 47: '[', 48: ']', 49: '\\', 51: ';' , 52: '\'', 53: '~', 54: ',', 55: '.', 56: '/'}
hid2 = {4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K', 15: 'L', 16: 'M', 17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V', 26: 'W', 27: 'X', 28: 'Y', 29: 'Z', 30: '!', 31: '@', 32: '#', 33: '$', 34: '%', 35: '^', 36: '&', 37: '*', 38: '(', 39: ')', 44: ' ', 45: '_', 46: '+', 47: '{', 48: '}', 49: '|', 51: ':' , 52: '"', 53: '~', 54: '<', 55: '>', 56: '?'}
fp = open('/dev/hidraw0', 'rb')
uart = serial.Serial("/dev/ttyS0", baudrate=57600, timeout=1)
finger = fingerprintlib.Adafruit_Fingerprint(uart)


def card_reader():
    while True:
        id_number_temp = ""
        sleep(.1)
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

        users = []
        for (dirpath, dirnames, filenames) in walk("users"):
            users.extend(filenames)
            break
        if "{}.json".format(id_number_temp) in users:
            print("Kart numarası eşleşti.")
            try:
                ret = user_send(id_number_temp, False)
            except:
                pass
        else:
            print("Kart Tanımsız !")
            print("Kart veya Parmak izi bilgisi bekleniyor...")

def fingerprint_scanner():
    while True:
        while finger.get_image() != fingerprintlib.OK:
            pass
        print("Parmak izi okutuldu.")
        print("İşleniyor...")
        if finger.image_2_tz(1) != fingerprintlib.OK:
            return False
        print("Parmak izi aranıyor...")

        users = []
        for (dirpath, dirnames, filenames) in walk("users"):
            users.extend(filenames)
            break

        id_number_temp = ""
        rank_temp = ""
        check = False
        for i in users:

            with open("users/{}".format(i), 'r') as json_file:
                data = json.load(json_file)

            for j in range(6):
                j = j+1
                template = []
                for p in data['user']:
                    template = p['fp{}'.format(j)]
                    id_number_temp = p['id']
                    rank_temp = p['rank']
                finger.send_fpdata(template, "char", 2)

                i = finger.create_model()
                if i == fingerprintlib.OK:
                    print("Parmak izi bulundu.")
                    check = True
                    break
                else:
                    pass
            if check:
                break
        if check:
            try:
                ret = user_send(id_number_temp, rank_temp)
            except:
                pass
        elif not check:
            print("Parmak izi bulunamadı.")
            sleep(.5)
            print("Kart veya Parmak izi bilgisi bekleniyor...")

def user_send(id_number, rank):

    if not rank:
        with open("users/{}.json".format(id_number), 'r') as json_file:
            data = json.load(json_file)
        for p in data['user']:
            rank = p['rank']
    print("Kart ID : {}".format(id_number))
    print("Yetki seviyesi : {}".format(rank))
    print("Bilgiler PlC'ye gönderiliyor")

    if not c.is_open():
            if not c.open():
                print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))
                sleep(1)
                print("PLC'ye bağlanılamadı.")

    if c.is_open():
        sleep(.1)
        toggle = 200
        c.write_single_register(10100, toggle)
        print("send")
        sleep(1)
        toggle = 2000
        c.write_single_register(10100, toggle)
        print("send")
        sleep(1)
        print("Bilgiler PlC'ye gönderildi")

    print("Kart veya Parmak izi bilgisi bekleniyor...")
    return True


print("Kart veya Parmak izi bilgisi bekleniyor...")
APP = threading.Thread(target=fingerprint_scanner)
APP2 = threading.Thread(target=card_reader)
APP.start()
APP2.start()