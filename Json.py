import json


dic = {}
ls = {}
for i in range(1, 10):
    dic[i] = i % 2 == 0
dic[12] = False
k = open('json.json', 'w')
json.dump(dic, k)
k.close()
f = open('json.json', 'r')
x = json.load(f)
for i in x:
    print(i)
