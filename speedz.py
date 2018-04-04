import sys
import os
import pyspeedtest
import humanize
import csv
from datetime import datetime

# Creating primary variable for speedtest
speedz = pyspeedtest.SpeedTest()

# Defining classes for speed testing and storing in variables
ping = speedz.ping()
dl = speedz.download()
ul = speedz.upload()

# Getting current time for the row
time = datetime.now().strftime('%Y-%m-%d %H:%M')

# Open and writing to csv table all the varbles and time
with open('logs.csv', 'a') as f:
    fieldnames = ['datetime', 'ping', 'download', 'upload']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writerow({
    'datetime': time,
    'ping': int(ping),
    'download': humanize.naturalsize(dl, gnu=True),
    'upload': humanize.naturalsize(ul, gnu=True)})
