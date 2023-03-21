import os
import requests
import IP2Location

import socket 


os.system('cmd /k "netstat -af')
os.system('cmd /k "netstat -an')

ip = input("Input IP address: ")



response = requests.get(f"https://geolocation-db.com/json/{ip}&position=true").json()
#https://geolocation.com/?ip=105.112.63.84#ipresult

print(response)
"""


database = IP2Location.IP2Location(os.path.join("data", "IP2LOCATION-LITE-DB11.BIN"))


rec = database.get_all('12.112.12.112')

print(rec.country_short)
print(rec.country_long)
print(rec.region)
print(rec.city)
print(rec.isp)
print(rec.latitude)
print(rec.longitude)
print(rec.domain)
print(rec.zipcode)
print(rec.timezone)
print(rec.netspeed)
print(rec.idd_code)
print(rec.area_code)
print(rec.weather_code)
print(rec.mcc)
print(rec.mnc)
print(rec.mobile_brand)
print(rec.elevation)
print(rec.usage_type)



import re
import json
from urllib2 import urlopen

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']

print 'Your IP detail\n '
print 'IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP)

"""
