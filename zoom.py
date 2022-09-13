from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from random import randint


import csv
file =  open('./details.csv','r')
mycsv= csv.DictReader(file,delimiter=',')
for row in mycsv:
        mycsv= row
url = 'https://us05web.zoom.us/wc/join/'+str(mycsv['meetingID'])+'?pwd='+str(mycsv['password'])

def join(url):
    driver = webdriver.Chrome('/usr/bin/chromedriver')
    driver.get(url)
    time.sleep(5)
    text_box = driver.find_element(by=By.NAME, value="inputname")
    submit_button = driver.find_element(by=By.ID, value="joinBtn")
    text_box.send_keys("user1"+str(randint(1,100000)))
    submit_button.click()

join(url)

# time.sleep(10000)
# driver.quit()





