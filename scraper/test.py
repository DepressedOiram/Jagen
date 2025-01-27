import Webscraper

import weapon
import json
import skill_scrape

obj = {}

file =  './sk.json'


#skill_scrape.upgrade_sp('Brutal Shell+')
#skill_scrape.upgrade_passive('Worldbreaker+')

with open(file, 'w') as fp:
    json.dump(obj, fp)
    


units = [
"Lilina: Brilliant Flame",
"Zeiss: Ebon Bolt",
"Bors: Ostia's Bastion",
"Elffin: Truth Beholden",
"Þjazi: Ruthless Jötun",
"Ogier: Ostia's New Blade"

]



#bj = {}

for i in range(0, len(units)):
    Webscraper.scrape_page(f"/wiki/{units[i]}")
    

#with open(file, 'w') as fp:
    #json.dump(obj, fp)





    
  


 