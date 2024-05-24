import os
import sys
from os import listdir
from os.path import isfile, join
import openpyxl
import re
import csv

timeStamp = "5/23/2024 08:05:33"

def dateTimeStr2Tuple(dateTime: str):
    regex = r"(\d+)/(\d+)/(\d+) (\d+):(\d+):(\d+)"
    match = re.search(regex, dateTime)
    dateTimeTuple = tuple(match.group(i+1) for i in range(6))
    return dateTimeTuple

a = '200fs0'
a = a.lstrip('0')
print(a)

""" firstSlashIndex = timeStamp.find('/')
month = timeStamp[:firstSlashIndex]

timeStamp = timeStamp[firstSlashIndex+1:]
secondSlashIndex = timeStamp.find('/')
day = timeStamp[:secondSlashIndex]

timeStamp = timeStamp[secondSlashIndex+1:]
spaceIndex = timeStamp.find(' ')
year = timeStamp[:spaceIndex]

timeStamp = timeStamp[spaceIndex+1:] """

""" print(month)
print(day)
print(year) """




""" path = "expiriment\checkInLogs\Checkin Log K-O copy.xlsx"
book = openpyxl.load_workbook(path)
sheet = book.active
timeCell = sheet.cell(13,1).value
print(f"value: <{timeCell}> of type: {type(timeCell)} of length: {len(timeCell)}") """