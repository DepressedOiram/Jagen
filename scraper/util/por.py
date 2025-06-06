import os
import json



with open("/Users/aiman/Desktop/Veyle/database/fe17/ring.json", 'r', encoding="utf-8") as f:
    rings = json.load(f)

keys = rings.keys()
for i in keys:
    print(rings[i]['portrait'])
    if rings[i]['portrait'] == None:
        rings[i]['portrait'] = 'bond/' + i + '.png'
 

with open('/Users/aiman/Desktop/Veyle/database/fe17/ring.json', 'w', encoding="utf-8") as fp:
        json.dump(rings, fp, indent=4)
    
  