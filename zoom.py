from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from random import randint
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException



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
url = 'https://us05web.zoom.us/wc/join/'+str(mycsv['meetingID'])+'?pwd='+str(mycsv['password'])
def join(url):
        options = Options()
        options.headless   = True
        driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
        driver.get(url)
        time.sleep(5)
        title = driver.title
        print(title)
        if ("Zoom" in title):
                try:    
                        text_box = driver.find_element(by=By.NAME, value="inputname")
                        submit_button = driver.find_element(by=By.ID, value="joinBtn")
                        text_box.send_keys(str(nameList[randint(0,len(nameList))]['names']).capitalize())
                        submit_button.click()
                        time.sleep(10)
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





