import requests
from bs4 import BeautifulSoup
import time
import random
import smtplib, ssl
import sys
import traceback
import re

pagenum = 1   #variable made for the pagenumber of the URL

time.sleep(5) # sleep for 5 seconds so webpage doesn't block us lol
url= 'https://www.arborsarundel.com/floor-plans/?sort=unitrent&order=ASC&pagenumber=' + str(pagenum) + '&nab=0' #url of website with pagenum variable so we can modify this later
page = requests.get(url)  # get request for page
ParsedHTML = BeautifulSoup(page.content, 'html.parser') #parser and making page code look readable
aptListings = ParsedHTML.find_all('div', class_ = 'mt_list_box')
for entry in aptListings:
    #finding Apartment Unit name
    MessyUnitName = entry.find('div', class_ = 'mt_list_col mt_fp_unit')
    unitName = MessyUnitName.h4.text
    #finding unit size
    MessyUnitSize = entry.find('span', class_ = 'mt_list_col mt_txt_sub')
    unitSize = MessyUnitSize.text
    # finding unit bed/bath 
    messyBedBath = entry.find('span', class_ = 'mt_list_col mt_txt_sub mt_bed_bath')
    beds = messyBedBath.find('span', class_ = 'capitalize').text.strip()
    try:
        baths = re.search('<span>(.+?)</span>', (str(messyBedBath))).group(1)
    except AttributeError:
        #if no <spans> are found
        baths = 'WE AINT FOUND SHIT' # apply your error handling

print(baths+' baths and '+ beds) #print the code gotten from the webpage
