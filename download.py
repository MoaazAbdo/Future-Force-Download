import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import os, shutil
import xlrd
from xlrd import sheet

# Start Prepare Input
loc = input("Please enter path of your input file: ")
web = xlrd.open_workbook(loc)
sheet = web.sheet_by_index(0)
links = []
for i in range(sheet.nrows):
    links.append(sheet.cell_value(i,0))

#print(len(links))

outputDir = "E:\\moaaz\\Future Force download Code\\Future"

if os.path.exists(outputDir) == False:
    os.mkdir(outputDir)
else:
    shutil.rmtree(outputDir)
    os.mkdir(outputDir)
# moaz code
# for i in range(len(links)):
#     r = requests.get(links[i], allow_redirects=True)
#     open(outputDir+"\\"+str(i)+'.csv', 'wb').write(r.content)
#     print(i)



for i in range(len(links)):
    r = requests.get(links[i], allow_redirects=True)
    file = outputDir+"\\"+str(i)+'.csv'
    with open(file, 'wb') as f:
        f.write(r.content)
    print(i)