import Webscraper
import requests
from bs4 import BeautifulSoup
import pandas as pd

# This file will take the page for the list of heroes and loop through a list containing the url of each hero on the
# page. To do this, it calls Webscraper.scrape_page(url) function for each url, and receives a list of the unit's
# info, which can then be placed into an excel sheet when finished.

# To start, we need the list of heroes from the List of Heroes page
hero_list_site = requests.get('https://feheroes.fandom.com/wiki/List_of_Heroes')
soup = BeautifulSoup(hero_list_site.text, 'html.parser')

hero_list = []

document = soup.find(class_="mw-parser-output")

inputs = document.table.find_all('tr')
inputArray = []

for i in inputs:
    if i.a is not None:
        inputArray.append(i.a.get('href'))

# create the dataframe and set up the Excel sheet
columns = ['Hero Name', 'Title', 'Date Added', 'Series Origin', 'Rarity', 'Weapon Type', 'Move Type', 'BST',
           'HP', 'ATK', 'SPD', 'DEF', 'RES', 'Has Superboon', 'Has Superbane']

df = pd.DataFrame()

for i in inputArray:
    url = i
    unit_info = Webscraper.scrape_page(url)

    if url == inputArray[0]:

        df = pd.DataFrame(
            {
                columns[0]: [unit_info[0]],
                columns[1]: [unit_info[1]],
                columns[2]: [unit_info[2]],
                columns[3]: [unit_info[3]],
                columns[4]: [unit_info[4]],
                columns[5]: [unit_info[5]],
                columns[6]: [unit_info[6]],
                columns[7]: [unit_info[7]],
                columns[8]: [unit_info[8]],
                columns[9]: [unit_info[9]],
                columns[10]: [unit_info[10]],
                columns[11]: [unit_info[11]],
                columns[12]: [unit_info[12]],
                columns[13]: [unit_info[13]],
                columns[14]: [unit_info[14]],
            }
        )

        df.index = [f"{unit_info[0]}: {unit_info[1]}"]

        writer = pd.ExcelWriter('FEH units.xlsx')
        df.to_excel(writer, sheet_name='FEH units', index=False, na_rep='NaN')

        # with all the data in the csv, now adjust column size, so it's readable
        for column in df:
            column_width = max(df[column].astype(str).map(len).max(), len(column)) + 1
            col_idx = df.columns.get_loc(column)
            writer.sheets['FEH units'].set_column(col_idx, col_idx, column_width)

        # convert data types for excel
        # df['Date Added'] = pd.to_datetime(df['Date Added']).dt.date

        writer.close()
        print(unit_info[0])

    else:
        # There is already a dataframe, so we just add to it
        df.loc[len(df.index)] = [unit_info[0], unit_info[1], unit_info[2], unit_info[3], unit_info[4], unit_info[5],
                                 unit_info[6], unit_info[7], unit_info[8], unit_info[9], unit_info[10], unit_info[11],
                                 unit_info[12], unit_info[13], unit_info[14]]

        writer = pd.ExcelWriter('FEH units.xlsx')
        df.to_excel(writer, sheet_name='FEH units', index=False, na_rep='NaN')

        # with all the data in the csv, now adjust column size, so it's readable
        for column in df:
            column_width = max(df[column].astype(str).map(len).max(), len(column)) + 1
            col_idx = df.columns.get_loc(column)
            writer.sheets['FEH units'].set_column(col_idx, col_idx, column_width)

        # convert data types for excel
        # df['Date Added'] = pd.to_datetime(df['Date Added']).dt.date

        writer.close()
        print(unit_info[0])
