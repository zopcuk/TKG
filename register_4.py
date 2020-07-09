from time import sleep
import os
import serial
import json
import pika
import fingerprintlib

hid = {4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 14: 'k', 15: 'l', 16: 'm', 17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 24: 'u', 25: 'v', 26: 'w', 27: 'x', 28: 'y', 29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7', 37: '8', 38: '9', 39: '0', 44: ' ', 45: '-', 46: '=', 47: '[', 48: ']', 49: '\\', 51: ';' , 52: '\'', 53: '~', 54: ',', 55: '.', 56: '/'}
hid2 = {4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K', 15: 'L', 16: 'M', 17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V', 26: 'W', 27: 'X', 28: 'Y', 29: 'Z', 30: '!', 31: '@', 32: '#', 33: '$', 34: '%', 35: '^', 36: '&', 37: '*', 38: '(', 39: ')', 44: ' ', 45: '_', 46: '+', 47: '{', 48: '}', 49: '|', 51: ':' , 52: '"', 53: '~', 54: '<', 55: '>', 56: '?'}
uart = serial.Serial("/dev/ttyS0", baudrate=57600, timeout=1)
finger = fingerprintlib.Adafruit_Fingerprint(uart)

id_number = ""
fp1 = []
fp2 = []
fp3 = []
fp4 = []
fp5 = []
fp6 = []

def id_card_read():
    fp = open('/dev/hidraw0', 'rb')
    global id_number
    while True:
        sleep(.05)
        shift = False
        done = False
        print("Kartı okutunuz !!")
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
                            id_number += hid2[int(c)]
                            shift = False
                    else:
                        if int(c) == 2:
                            shift = True
                        else:
                            id_number += hid[int(c)]
        fp.close()
        break

def finger_get():
    for fingerimg in range(1, 3):
        if fingerimg == 1:
            print("Parmağınızı sensöre yerleştirin...", end="", flush=True)
        else:
            print("Aynı parmağı tekrar yerleştirin...", end="", flush=True)

        while True:
            i = finger.get_image()
            if i == fingerprintlib.OK:
                print("Parmak izi alındı")
                break
            if i == fingerprintlib.NOFINGER:
                print(".", end="", flush=True)
            elif i == fingerprintlib.IMAGEFAIL:
                print("Görüntü hatası")
                return False
            else:
                print("Diğer hatalar.")
                return False

        print("İşleniyor...", end="", flush=True)
        i = finger.image_2_tz(fingerimg)
        if i == fingerprintlib.OK:
            print("Parmak izi işlendi")
        else:
            if i == fingerprintlib.IMAGEMESS:
                print("Parmak izi çok bulanık")
            elif i == fingerprintlib.FEATUREFAIL:
                print("Parmak izi özellikleri tanımlanamadı.")
            elif i == fingerprintlib.INVALIDIMAGE:
                print("Parmak izi geçersiz.")
            else:
                print("Diğer hatalar.")
            return False

        if fingerimg == 1:
            print("Parmağınızı kaldırın !!")
            sleep(1)
            while i != fingerprintlib.NOFINGER:
                i = finger.get_image()

    print("Parmak izleri eşleştiriliyor...", end="", flush=True)
    i = finger.create_model()
    if i == fingerprintlib.OK:
        print("Parmak izleri eşleşdi")
        fp_buffer1 = finger.get_fpdata("char", 1)
        fp_buffer2 = finger.get_fpdata("char", 2)
        return fp_buffer1, fp_buffer2
    else:
        if i == fingerprintlib.ENROLLMISMATCH:
            print("Parmak izleri eşleşmedi")
        else:
            print("Diğer hatalar")
        return False, False
def user_save():
    global fp1, fp2, fp3, fp4, fp5, fp6, id_number, rank
    print("Bilgiler kaydediliyor lütfen bekleyin...")
    data = {}
    data['user'] = []
    data['user'].append({
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
    print("Kullanıcı bilgileri kaydedildi")
    try:
        credentials = pika.PlainCredentials(username='test', password='test')
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', credentials=credentials))
        channel = connection.channel()
        channel.exchange_declare(exchange='logs', exchange_type='fanout')
        message = json.dumps(data)
        channel.basic_publish(exchange='logs', routing_key='', body=message)
        connection.close()
        print("Kullanıcı bilgileri dağıtıldı.")
    except:
        pass
while True:
    id_number = ""
    print("Yeni Kayıt için : r || Kişi silmek için d tuşuna basınız. ")
    c = input("> ")
    if c == "d":
        #id_card_read()
        print("Kartı okutunuz !!")
        id_number = input("> ")
        users = []
        for (dirpath, dirnames, filenames) in os.walk("users"):
            users.extend(filenames)
            break
        if "{}.json".format(id_number) in users:
            print("Kullanıcı bulundu.")
            print("Kullanıcı siliniyor.")
            sleep(1)
            os.remove("users/{}.json".format(id_number))
            print("Kullanıcı silindi.")
        else:
            print("Kart Tanımsız !")

    if c == "r":
        #id_card_read()
        print("Kartı okutunuz !!")
        id_number = input("> ")
        while True:
            print("Kullanıcının yetkisini giriniz !!")
            rank = input("> ")
            try:
                if 0<=int(rank)<=9:
                    print("Gecerli yetki !")
                    break
                else:
                    print("Gecersiz yetki !")
            except:
                print("Gecersiz yetki !")
                pass
        i = 0
        parmak = ""
        while True:
            if i == 0:
                parmak = "BAŞ"
            if i == 1:
                parmak = "İŞARET"
            if i == 2:
                parmak = "ORTA"
            print("{} PARMAK İZİ İÇİN!!".format(parmak))
            fp_buffer1, fp_buffer2 = finger_get()
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
            if i==2:
                break
            i += 1
        if i == 2:
            user_save()