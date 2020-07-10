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
for i in range(8):
    k = template1[i] - template1[i+1]
    if k < 0 :
        k = k*(-1)
    l = l + k
print(l/2)
k=0
l=0
for i in range(8):
    k = template2[i] - template2[i+1]
    if k < 0 :
        k = k*(-1)
    l = l + k
print(l/2)