from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from random import randint
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import re


import csv
nameFile =  open('./name.csv','r')
nameDict= csv.DictReader(nameFile,delimiter=',')
nameList = []
for row in nameDict:
    nameList.append(row)
nameList
file =  open('./details.csv','r')
mycsv= csv.DictReader(file,delimiter=',')
for row in mycsv:
        mycsv= row
if (mycsv['webinar']=='yes'):
        url = 'https://us06web.zoom.us/wc/join/'+str(mycsv['meetingID'])+'?pwd='+str(mycsv['password'])
else:
        url = 'https://us05web.zoom.us/wc/join/'+str(mycsv['meetingID'])+'?pwd='+str(mycsv['password'])
def join(url):
        options = Options()
        # options.headless   = True
        driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
        driver.get(url)
        time.sleep(2)
        title = driver.title
        print(title)
        if ("Zoom" in title):
                try:    
                        text_box = driver.find_element(by=By.NAME, value="inputname")
                        submit_button = driver.find_element(by=By.ID, value="joinBtn")
                        name=str(nameList[randint(0,len(nameList))]['names']).capitalize()
                        text_box.send_keys(name)
                        time.sleep(1)
                        submit_button.click()
                        if ('Zoom meeting on web - Zoom'== driver.title):
                                email_box = driver.find_element(by=By.NAME, value="inputemail")
                                join_button = driver.find_element(by=By.ID, value="joinBtn")
                                email = re.sub('[\s+]', '',name)+str(randint(1,100000))+'@gmail.com'
                                time.sleep(3)
                                email_box.send_keys(email)
                                join_button.click()

                        if('Error' in driver.title):
                                print('This meeting link has expired or invalid')
                                return 'This meeting link has expired or invalid'
                        else:
                                print('joined meeting')
                                time.sleep(10000)

                                return('joined meeting')


                except NoSuchElementException:
                        print('An error occur, the page might have been changed') 
                        return                       
        else:
                print('An error occur, the page might have been changed')
                return
           
join(url)

# time.sleep(10000)
# driver.quit()





