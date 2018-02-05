import xlrd
import pandas
import math
from bs4 import BeautifulSoup
import urllib.request
import os
import sys

from urllib.parse import quote
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'country1.xls')


url='https://he.wikipedia.org/wiki/'
xls = pandas.ExcelFile(filename)
sheetX = xls.parse() #2 is the sheet number
var1 = sheetX['birth_country']
text = ["" for x in range(120)]
text={}
saveNext= False
    
for x in range(0, 49):
    print(var1[x]) #1 is the row number...
    if isinstance(var1[x], str):
        try:
            url1 = 'https://he.wikipedia.org/wiki/' + quote(var1[x])
            print(url1)
            thepage=urllib.request.urlopen(url1)
            soup=BeautifulSoup(thepage, "html.parser")
            albumdatasaved=""
            # find all table ,get the first
            table = soup.find_all('table')[0]  # Only use the first table
            # iter over it
            for record in table.findAll('tr'):
                for data in record.findAll('td'):
                    if saveNext:
                        text.update({var1[x]: {"continent": data.text}})

                        saveNext= False
                    elif data.text == "יבשת":
                        saveNext=True
        except:
            text.update({var1[x]: {"continent": ""}})
                
df = pandas.DataFrame(text).T
df.to_excel('/Users/Timna/Downloads/cou1.xls')


