from selenium import webdriver
from getpass import getpass
from time import sleep

driver = webdriver.Chrome()
driver.get('https://twitter.com/login')

usr = input('Username: ')
pwd = getpass('Password: ')

username_box= driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
username_box.send_keys(usr)
sleep(3)

password_box= driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
password_box.send_keys(pwd)

login_button = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
login_button.submit()
sleep(3)

tweet = input('Tweet : ')

tweet_box = driver.find_element_by_xpath('//*[@id="tweet-box-home-timeline"]')
tweet_box.send_keys(tweet)

tweet_button = driver.find_element_by_xpath('//*[@id="timeline"]/div[2]/div/form/div[3]/div[2]/button')
tweet_button.click()
