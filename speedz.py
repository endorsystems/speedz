import speedtest
import humanize
import sys
import os
import csv
from datetime import datetime

servers = []
threads = None

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download(threads=threads)
s.upload(threads=threads)
s.results.share()
results_dict = s.results.dict()

ping = results_dict['ping']
dl = results_dict['download']
ul = results_dict['upload']

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