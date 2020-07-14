import json

with open("users/{}.json".format("1"), 'r') as json_file:
    data = json.load(json_file)


for i in range(2, 50):
    with open('users/{}.json'.format(i), 'w') as outfile:
        json.dump(data, outfile)