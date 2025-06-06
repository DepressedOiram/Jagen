import Webscraper

import weapon
import json
import skill_scrape
import utility

obj = {}

file =  './sk.json'

skills = [
"Squad Ace BU",
"Squad Ace BV",
"Squad Ace BW",
"Squad Ace BX",
"Squad Ace BY",
"Squad Ace BZ",
"Squad Ace CA",
"Squad Ace CB",
"Squad Ace CC",
"Squad Ace CD",
"Squad Ace CE",
"Squad Ace CF"

]

#print(obj['spddeftempo'])
for i in range(0, len(skills)):
    key = utility.compress(skills[i])
    obj[key]= skill_scrape.scrape_passive_skill(skills[i])


json_file = open(file, 'w')
json.dump(obj, json_file)
json_file.close()

#with open() as fp:
    #json.dump(obj, fp)
    





#for i in range(0, len(units)):
    #Webscraper.scrape_page(f"/wiki/{units[i]}")






    
  


 