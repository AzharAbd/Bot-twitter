import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from getpass import getpass

def scrape(url):
    driver = webdriver.Chrome()
    driver.get(url)
    #source_code = requests.get(url) #get the source code
    source_code = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()
	#testing github
    soup = BeautifulSoup(source_code, 'html.parser')

    box = soup.find('div',{'class' : 'upcoming challenge-list'})
    listofChallenges = box.find_all('div',{'class' : 'challenge-card-modern'})
    for challenge in listofChallenges:
        challenge_type = challenge.find('div',{'class' : 'challenge-type'}).string
        challenge_type = challenge_type.replace("\n","")
        challenge_type = challenge_type.strip()
        challenge_name = challenge.find('div',{'class' : 'challenge-name'})['title']
        challenge_date = challenge.find('div',{'class' : 'date'}).string
        challenge_link = "https://www.hackerearth.com" + challenge.find('a', {'class' : 'challenge-card-wrapper'})['href']
        twiit = challenge_type +"\n" + challenge_name+ "\n" + challenge_date + "\n" + challenge_link
        tweet(twiit)

def login():

    usr = input('Username: ')
    pwd = getpass('Password: ')

    username_box= drivertweet.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
    username_box.send_keys(usr)
    sleep(3)

    password_box= drivertweet.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
    password_box.send_keys(pwd)

    login_button = drivertweet.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
    login_button.submit()
    sleep(3)

def tweet(twiit):
    tweet_box = drivertweet.find_element_by_xpath('//*[@id="tweet-box-home-timeline"]')
    tweet_box.send_keys(twiit)

    tweet_button = drivertweet.find_element_by_xpath('//*[@id="timeline"]/div[2]/div/form/div[3]/div[2]/button')
    tweet_button.click()
    sleep(5)

drivertweet = webdriver.Chrome()
drivertweet.get('https://twitter.com/login')
login()
scrape('https://www.hackerearth.com/challenges/')
