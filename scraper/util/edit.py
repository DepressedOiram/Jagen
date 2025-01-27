
import json

with open('./job.json', 'r', encoding="utf-8") as f:
    file = json.load(f)

keys = file.keys()

for i in keys:
    obj = file[i]
    print(obj)
    #del obj['rank']
    del obj['major']
    del obj['minor']
    del obj['weapon']
    #del obj['ALT_NAME']
    del obj['rank']
    file[i] = obj

with open('./job2.json', 'w') as fp:
    json.dump(file, fp, indent=2)
