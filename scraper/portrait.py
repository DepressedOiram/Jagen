import requests
from bs4 import BeautifulSoup
import json
from PIL import Image
import time
import maps


with open('../database/feh/char.json', 'r', encoding="utf-8") as f:
    char = json.load(f)

path2 = '../database/feh/images/heroes/'



#130
def lordPortrait(unit, char, resp=False):

  img = Image.new('RGBA', (169, 169), (255, 0, 0, 0))

  if (resp == True):
    background = Image.open('editing/frames/colors/colorless_fill.png', 'r')
    frame = Image.open('editing/frames/colors/colorless_frame.png', 'r')
    img.paste(background, (1,1))
    try:
      img.paste(char, (5,5), char)
    except:
      img.paste(char, (5,5))
    img.paste(frame, (0, 0), frame)
    img = img.resize((130, 130))
    img.save('./' + unit['name'] + '_resp.png')
    return

  elif (unit['type'] == 'legendary' or unit['type'] == 'mythic'):
    element = Image.open('editing/icons/' + unit['blessing'].lower() + '.png', 'r')
    background = Image.open('editing/frames/lm_fill.png', 'r')
    frame = Image.open('editing/frames/lm_frame.png', 'r')
    img.paste(background, (1,1))
    try:
      img.paste(char, (5,5), char)
    except:
      img.paste(char, (5,5))
    img.paste(frame, (0, 0), frame)
    img.paste(element, (10, 164-(element.height+5)), element)
    img = img.resize((130, 130))
    img.save('./' +  unit['name'] + '_leg.png')
    return

  elif (unit['pool'] == 'seasonal'):
    background = Image.open('editing/frames/multi_fill.png', 'r')
    frame = Image.open('editing/frames/multi_frame.png', 'r')
    img.paste(background, (1,1))
    try:
      img.paste(char, (5,5), char)
    except:
      img.paste(char, (5,5))
    img.paste(frame, (0, 0), frame)
    if (unit['rarity'] == 4):
      icon = Image.open('editing/icons/4star.png', 'r')
      icon=icon.resize((55,55))
      img.paste(icon, (5, 164-(icon.height)), icon)
    if unit['duo']:
      icon = Image.open('editing/icons/duo.png', 'r')
      icon=icon.resize((icon.width-20,icon.height-20))
      img.paste(icon, (5, 164-(icon.height)), icon)

    if unit['harmonized']:
      icon = Image.open('editing/icons/harmonic.png', 'r')
      icon=icon.resize((icon.width-20,icon.height-20))
      img.paste(icon, (5, 164-(icon.height)), icon)
    img = img.resize((130, 130))
    img.save('./' +  unit['name'] + '_seasonal.png')


    return

  elif (unit['type'] == 'emblem'):
    background = Image.open('editing/frames/purple_fill.png', 'r')
    frame = Image.open('editing/frames/purple_frame.png', 'r')
    img.paste(background, (1,1))
    try:
      img.paste(char, (5,5), char)
    except:
      img.paste(char, (5,5))
    img.paste(frame, (0, 0), frame)
    img = img.resize((130, 130))
    img.save( unit['name'] + '_emblem.png')
    return

  elif (unit['type'] == 'rearmed'):
    background = Image.open('editing/frames/rarity/5_bg.png', 'r')
    frame = Image.open('editing/frames/rarity/5_frame.png', 'r')
    img.paste(background, (1,1))
    try:
      img.paste(char, (5,5), char)
    except:
      img.paste(char, (5,5))
    img.paste(frame, (0, 0), frame)
    icon = Image.open('editing/icons/rearm.png', 'r')
    icon=icon.resize((52,52))
    img.paste(icon, (5, 164-(icon.height)), icon)
    img = img.resize((130, 130))
    img.save( unit['name'] + '_rearmed.png')
    return

  elif (unit['type'] == 'ascended'):
    background = Image.open('editing/frames/rarity/5_bg.png', 'r')
    frame = Image.open('editing/frames/rarity/5_frame.png', 'r')
    img.paste(background, (1,1))
    try:
      img.paste(char, (5,5), char)
    except:
      img.paste(char, (5,5))
    img.paste(frame, (0, 0), frame)
    icon = Image.open('editing/icons/asc.png', 'r')
    icon=icon.resize((52,52))
    img.paste(icon, (5, 164-(icon.height)), icon)
    img = img.resize((130, 130))
    img.save( unit['name'] + '_asc.png')
    return

  elif (unit['type'] == 'attuned'):
    background = Image.open('editing/frames/rarity/5_bg.png', 'r')
    frame = Image.open('editing/frames/rarity/5_frame.png', 'r')
    img.paste(background, (1,1))
    try:
      img.paste(char, (5,5), char)
    except:
      img.paste(char, (5,5))
    img.paste(frame, (0, 0), frame)
    icon = Image.open('editing/icons/attuned.png', 'r')
    icon=icon.resize((52,52))
    img.paste(icon, (5, 164-(icon.height)), icon)
    img = img.resize((130, 130))
    img.save( unit['name'] + '_att.png')
    return

  res = [i for i in unit['ALT_NAME'] if 'CYL' in i]

  if (len(res) > 0):
    background = Image.open('editing/frames/lm_fill.png', 'r')
    frame = Image.open('editing/frames/forma_frame.png', 'r')
    img.paste(background, (1,1))
    try:
      img.paste(char, (5,5), char)
    except:
      img.paste(char, (5,5))
    img.paste(frame, (0, 0), frame)
    img = img.resize((130, 130))
    img.save('./' + unit['name'] + '_brave.png')
    return

  else:
    background = Image.open('editing/frames/rarity/grail_fill.png', 'r')
    frame = Image.open('editing/frames/rarity/grail_frame.png', 'r')
    img.paste(background, (1,1))
    try:
      img.paste(char, (5,5), char)
    except:
      img.paste(char, (5,5))
    img.paste(frame, (0, 0), frame)
    img = img.resize((130, 130))
    img.save('./' +  unit['name'] + '_base.png')

    img = Image.new('RGBA', (169, 169), (255, 0, 0, 0))

    background = Image.open('editing/frames/rarity/5_bg.png', 'r')
    frame = Image.open('editing/frames/rarity/5_frame.png', 'r')
    img.paste(background, (1,1))
    try:
      img.paste(char, (5,5), char)
    except:
      img.paste(char, (5,5))
    img.paste(frame, (0, 0), frame)
    img = img.resize((130, 130))
    img.save('./' +  unit['name'] + '_5.png')
  return



def portrait(key, unit, resp = False):

    page_name = unit['name'] + "+" + unit['title'] + ' Face FC'
    if resp:
      page_name += ' Resplendent'
    page_name = page_name.replace(' ', '+')


    # Follow the same steps for feheroes.fandom
    fandom = requests.get(f'https://feheroes.fandom.com/wiki/Special:Search?fulltext=1&query={page_name.lower()}&scope=internal&contentType=&ns%5B0%5D=6')
    soup = BeautifulSoup(fandom.text, 'html.parser')

    # The information we want on the page is stored under '<div role="document" class="page">
    document = soup.find(class_="page")
    wiki_info = document.find(class_="unified-search__result__thumbnail").find_all('a')
    link = wiki_info[0]['data-thumbnail']
    link = link[0:link.index('thumbnail-down')]
    data = requests.get(link).content
    path = './png/' + key + '.png'

    f = open(path,'wb')
    f.write(data)
    f.close()

    nameStr = key

    if resp:
      nameStr += 'R'

    f = open( path2 + nameStr + '.png','wb')
    f.write(data)
    f.close()    

    color = unit['color'].lower()
    img = Image.new('RGBA', (169, 169), (255, 0, 0, 0))


    if (unit['duo'] or unit['harmonized']):
      print('test')
      page_name = unit['name'] + "+" + unit['title'] + ' Face.webp'
      fandom = requests.get(f'https://feheroes.fandom.com/wiki/Special:Search?fulltext=1&query={page_name.lower()}&scope=internal&contentType=&ns%5B0%5D=6')
      soup = BeautifulSoup(fandom.text, 'html.parser')
      document = soup.find(class_="page")
      wiki_info = document.find(class_="unified-search__result__thumbnail").find_all('a')
      link = wiki_info[0]['data-thumbnail']
      link = link[0:link.index('thumbnail-down')]
      data = requests.get(link).content
      path3 = './png/' + key + ' Face.png'
      f = open(path3,'wb')
      f.write(data)
      f.close()
    


    background = Image.open('editing/frames/colors/' + color + '_fill.png', 'r')
    char = Image.open('./' + path, 'r')

    img.paste(background, (1,1))
    try:
      img.paste(char, (5,5), char)
    except:
      img.paste(char, (5,5))


    frame = Image.open('editing/frames/colors/' + color + '_frame.png', 'r')
    img.paste(frame, (0, 0), frame)



    if (unit['type'] == 'legendary' or unit['type'] == 'mythic'):
      element = Image.open('editing/icons/' + unit['blessing'].lower() + '.png', 'r')
      img.paste(element, (10, 164-(element.height+5)), element)
    if (unit['type'] == 'emblem'):
      icon = Image.open('editing/icons/emblem.png', 'r')
      icon=icon.resize((icon.width-20,icon.height-20))
      img.paste(icon, (5, 164-(icon.height)), icon)


    if unit['type'] == 'ascended':
      icon = Image.open('editing/icons/asc.png', 'r')
      icon=icon.resize((52,52))
      img.paste(icon, (5, 164-(icon.height)), icon)

    if unit['type'] == 'aided':
      icon = Image.open('editing/icons/aided.png', 'r')
      icon=icon.resize((52,52))
      img.paste(icon, (5, 164-(icon.height)), icon)


    if unit['type'] == 'rearmed':
      icon = Image.open('editing/icons/rearm.png', 'r')
      icon=icon.resize((52,52))
      img.paste(icon, (5, 164-(icon.height)), icon)

    if unit['type'] == 'attuned':
      icon = Image.open('editing/icons/attuned.png', 'r')
      icon=icon.resize((52,52))
      img.paste(icon, (5, 164-(icon.height)), icon)

    if unit['duo']:
      icon = Image.open('editing/icons/duo.png', 'r')
      icon=icon.resize((icon.width-20,icon.height-20))
      img.paste(icon, (5, 164-(icon.height)), icon)

    if unit['harmonized']:
      icon = Image.open('editing/icons/harmonic.png', 'r')
      icon=icon.resize((icon.width-20,icon.height-20))
      img.paste(icon, (5, 164-(icon.height)), icon)

    if unit['pool'] == 'seasonal' and unit['rarity'] == 4:
      icon = Image.open('editing/icons/4star.png', 'r')
      icon=icon.resize((55,55))
      img.paste(icon, (5, 164-(icon.height)), icon)


    img.save('./png/' + key + '_color.png')

    if (unit['name'] in maps.lords):
      lordPortrait(unit, char, resp)

    return


def resp_portrait(unit): 
    page_name = unit['name'] + '+' + unit['title'] + ' Face FC' + ' Resplendent'
    page_name = page_name.replace(' ', '+')

    # Follow the same steps for feheroes.fandom
    fandom = requests.get(f'https://feheroes.fandom.com/wiki/Special:Search?fulltext=1&query={page_name.lower()}&scope=internal&contentType=&ns%5B0%5D=6')
    soup = BeautifulSoup(fandom.text, 'html.parser')

    # The information we want on the page is stored under '<div role="document" class="page">
    document = soup.find(class_="page")

    wiki_info = document.find(class_="unified-search__result__thumbnail").find_all('a')

    link = wiki_info[0]['data-thumbnail']

    link = link[0:link.index('thumbnail-down')]

    data = requests.get(link).content

    path = './png/' + unit['name'] + ' ' + unit['title'] + '.png'

    f = open(path,'wb')
    f.write(data)
    f.close()
    char = Image.open('./' + path, 'r')

    
    background = Image.open('editing/frames/colors/colorless_fill.png', 'r')
    frame = Image.open('editing/frames/colors/colorless_frame.png', 'r')
    if unit['rarity'] == 5:
      background = Image.open('editing/frames/rarity/5_bg.png', 'r')
      frame = Image.open('editing/frames/rarity/5_frame.png', 'r')
    if unit['pool'] == 'grail':
      background = Image.open('editing/frames/rarity/grail_fill.png', 'r')
      frame = Image.open('editing/frames/rarity/grail_frame.png', 'r')

    img = Image.new('RGBA', (169, 169), (255, 0, 0, 0))

    img.paste(background, (1,1))
    try:
      img.paste(char, (5,5), char)
    except:
      img.paste(char, (5,5))
    img.paste(frame, (0, 0), frame)
    
    img = img.resize((130, 130))
    img.save('./' + str(unit['name']) + '_resp.png')



def new_portrait(key, resp):

  unit = char[key]

  mainpath = "../database/feh/images/heroes2/"

  page_name = unit['name'] + '+' + unit['title'] + ' Face FC'
  if resp:
    page_name += ' Resplendent'
  page_name = page_name.replace(' ', '+')

  # Follow the same steps for feheroes.fandom
  fandom = requests.get(f'https://feheroes.fandom.com/wiki/Special:Search?fulltext=1&query={page_name.lower()}&scope=internal&contentType=&ns%5B0%5D=6')
  soup = BeautifulSoup(fandom.text, 'html.parser')

  # The information we want on the page is stored under '<div role="document" class="page">
  document = soup.find(class_="page")

  wiki_info = document.find(class_="unified-search__result__thumbnail").find_all('a')

  link = wiki_info[0]['data-thumbnail']

  link = link[0:link.index('thumbnail-down')]

  data = requests.get(link).content

  path = mainpath + key

  if (resp):
    path = path + 'R.png'
  else:
    path = path + '.png'

  f = open(path,'wb')
  f.write(data)
  f.close()

"""
from PIL import Image
import glob, os

size = 128, 128

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        im.thumbnail(size)
        im.save(file + ".thumbnail", "JPEG")
"""
