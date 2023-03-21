#https://www.emobiletracker.com/trace-process.php

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

number = phonenumbers.parse(int(input("Input phone number:"))#enter you phone number
country = geocoder.description_for_number(number,'en')

ISP = carrier.name_for_number(number, 'en')
print("country = {}".format(country))
print("country = {}".format(ISP))



"""
from bs4 import BeautifulSoup
import mechanize

mc = mechanize.Browser()
mc.set_handle_robots(False)


url = ""
mc.open(url)

mc.select_form(name='trace')
mc['mobilenumber'] = ''#enter a mobile number
res = mc.submit().read()

soup = BeautifulSoup(res, "html.parser")
tbl = soup.find_all('table', class_= 'shop_table')
#print(tbl)

data = tbl[0].find('tfoot')
c=0
for i in data:
    c+=1
    if c in (1,4,6,8):
        continue
    th = i.find('th')
    td = i.find('td')
    print(th.text, td.text)


data = tbl[1].find('tfoot')
c=0
for i in data:
    c+=1
    if c in (2,20,22,26):
        th = i.find('th')
        td = i.find('td')
        print(th.text, td.text)
        """
