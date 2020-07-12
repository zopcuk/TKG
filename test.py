import json
from os import walk
import cv2
users = []
for (dirpath, dirnames, filenames) in walk("users"):
    users.extend(filenames)
    break

with open("users/{}".format(users[3]), 'r') as json_file:
    data = json.load(json_file)

for p in data['user']:
    id = p['id']
    template1 = p['fp6']
    template2 = p['fp5']
print(id)
k=0
l=0
m=0
for j in range(1536):
    for i in range(8):
        if (m+i+1) >1535:
            break
        k = template1[m+i] - template1[m+i+1]
        if k < 0 :
            k = k*(-1)
        l = l + k
    m = m+1
print(l)
k=0
l=0
m=0
for j in range(1536):
    for i in range(8):
        if (m+i+1) >1535:
            break
        k = template2[m+i] - template2[m+i+1]
        if k < 0 :
            k = k*(-1)
        l = l + k
    m = m+1
print(l)