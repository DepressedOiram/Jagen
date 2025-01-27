import requests
from bs4 import BeautifulSoup
import json


def scrape_page(page_name):
    # Follow the same steps for feheroes.fandom
    fandom = requests.get(f'https://fireemblem.fandom.com/wiki/List_of_Skills_in_Fire_Emblem_Engage')
    soup = BeautifulSoup(fandom.text, 'html.parser')

    # The information we want on the page is stored under '<div role="document" class="page">
    document = soup.find(class_="mw-parser-output")

    # Create a list that will hold all the info we want to export to the Excel file
    unit_info = []

    # get the name and title of the unit and append both to the unit_info
    wiki_info = document.find_all(class_="wikitable")

    #print(wiki_info)

    for table1 in wiki_info:
        table1 = table1.find_all('tr')
        #print(table1)
        for i in range(1, len(table1)):
            cols = list(table1[i].stripped_strings)
            #print(table1[i])
            atags = table1[i].find_all(class_="image")
            for j in atags:
                print(j)
                url = j['href']
                # if '.png' not in url:
                #    continue
                name = 'skills/fe17_' + cols[0].replace('/', '') + '.png'
              
                # name = 'skills/' + url[57:-34]
                name = name.replace(' ', '')
                name = name.lower()
                #print(name)
                data = requests.get(url).content
                f = open(name, 'wb', )
                f.write(data)
                f.close()

    # This statement requests the resource at
    # the given link, extracts its contents
    # and saves it in a variable

    # Opening a new file named img with extension .jpg
    # This file would store the data of the image file

    # Storing the image data inside the data variable to the file

    # print(wiki_info)

    return unit_info


print(scrape_page('/wiki/Lucina:_Future_Witness'))
