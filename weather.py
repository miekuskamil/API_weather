#!/usr/bin/python3
import requests
import pandas as pd
import plotly.express as px
import json
import csv
import datetime
from pprint import pprint
from shutil import copyfile

def convert_temp(celvin):
    celsius = (celvin - 273.15)
    return(celsius)

datetime_object = datetime.datetime.today()

today = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Edinburgh,GB&APPID=e101e212e9a6c9542feb0cef323ae537')
response_today = today.json()
temperature = (convert_temp(response_today['main']['temp']))


with open('weather.csv', 'a') as data:
    writer = csv.writer(data)
    writer.writerow([datetime_object, temperature])


#with open('weather.csv', 'r') as data:
#    reader = csv.reader(data)
#    for row in reader:
#        pprint(row)

df = pd.read_csv('weather.csv')
fig = px.line(df, x = 'time', y = 'temperature', title='TEMPERATURE TREND IN EDINBURGH')
fig.write_html('weather.html')

copyfile('weather.html', '/var/www/html/weather.html')
