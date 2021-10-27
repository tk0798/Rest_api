import json
x = {}
x = json.dumps(x)
for i in range(2):

    json1 = {'asd':1,'das':'aassdd'}

    y=json.dumps(json1)

    z = x+y
print(z)