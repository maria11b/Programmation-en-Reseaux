import time
import json
import pickle
import pprint
import requests
import pandas as pd

from selenium import webdriver
from urllib import request as urlrequest
from selenium.webdriver.chrome.options import Options
from proxy_requests import ProxyRequests, ProxyRequestsBasicAuth

res = requests.get(input("Enter Proxy site URL: "))
# res = requests.get("https://free-proxy-list.net/") 

proxies = pd.read_html(res.text)
proxies = proxies[0][:80] 
with open("proxies.txt", "w") as f:
    for index,row in proxies.iterrows():
        f.write("%s:%s\n"%(row["IP Address"],int(row["Port"])))
        print("%s:%s"%(row["IP Address"],int(row["Port"])))

text_file = open("proxies.txt", 'r')
first_proxy = text_file.readline()
print("We'll use:", first_proxy)

proxy = {"http": first_proxy}
url = 'https://999.md/ro//'
resp = requests.get(url, proxies=proxy)
print("Get method:", resp)

r = requests.post(url, data={'number': 12524, 'type': 'issue', 'action': 'show'}, proxies=proxy)
print("Post method:", r.status_code, r.reason)
print(r.text[:300] + '...')

x = requests.head(url, proxies=proxy)
print("Head method:", x.headers)

verbs = requests.options(url, proxies=proxy)
print("Options method:", verbs.status_code)
verbs = requests.options('http://a-good-website.com/api/cats')
print(verbs.headers['allow'])

def save_cookies(driver, location):
    pickle.dump(driver.get_cookies(), open(location, "wb"))

def load_cookies(driver, location, url=None):
    cookies = pickle.load(open(location, "rb"))
    driver.delete_all_cookies()
    driver.get("https://google.com" if url is None else url)
    for cookie in cookies:
        if isinstance(cookie.get('expiry'), float):
            cookie['expiry'] = int(cookie['expiry'])
        driver.add_cookie(cookie)

def delete_cookies(driver, domains=None):
    cookies = driver.get_cookies()
    for cookie in cookies:
        if domains is not None:
            if str(cookie["domain"]) in domains:
                cookies.remove(cookie)
        else:
            driver.delete_all_cookies()
            return
    driver.delete_all_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)

cookies_location = "D:\Travail1/cookies.txt"

driver = webdriver.Chrome('D:\Travail1/chromedriver.exe')
driver.get("https://999.md/")
elem = driver.find_element_by_xpath("/html/body/div[4]/header/div[2]/nav/ul/li[2]/a") 
elem.click()
elem = driver.find_element_by_name('login')
elem.send_keys("Elinuta")
elem = driver.find_element_by_name('password')
elem.send_keys("Maria11")
elem = driver.find_element_by_xpath("/html/body/div/div[1]/form/div[4]/button") 
elem.click()
save_cookies(driver, cookies_location)
time.sleep(10)
driver.close()

driver = webdriver.Chrome('D:\Travail1/chromedriver.exe')
load_cookies(driver, cookies_location)
driver.get("https://999.md/")
time.sleep(10)
driver.quit()