import os
import json



with open("/Users/aiman/Desktop/Veyle/database/fe3/b1.json", 'r', encoding="utf-8") as f:
    main = json.load(f)

with open("/Users/aiman/Downloads/csvjson.json", 'r', encoding="utf-8") as f:
    updated = json.load(f)

keys = updated.keys()
for i in keys:
  key = i.lower()
  stats = updated[i].keys()
  for j in stats:
    main[key]['base'][j] = updated[i][j]

with open('/Users/aiman/Desktop/Veyle/database/fe3/b1.json', 'w', encoding="utf-8") as fp:
        json.dump(main, fp, indent=2)
    
  