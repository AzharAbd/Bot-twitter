import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def scrape(url):
    driver = webdriver.Chrome()
    driver.get(url)
    #source_code = requests.get(url) #get the source code
    source_code = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()

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
        print(challenge_type)
        print(challenge_name)
        print(challenge_date)
        print(challenge_link)

scrape('https://www.hackerearth.com/challenges/')
