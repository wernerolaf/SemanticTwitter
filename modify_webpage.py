from selenium import webdriver, common
from selenium.webdriver.common.keys import Keys
import time
from random import uniform
import config

driver = webdriver.Firefox()
driver.get("https://twitter.com/login")


time.sleep(4)

try:
    email = driver.find_element_by_name('session[username_or_email]')
    password = driver.find_element_by_name('session[password]')
except common.exceptions.NoSuchElementException:
    time.sleep(3)
    email = driver.find_element_by_name('session[username_or_email]')
    password = driver.find_element_by_name('session[password]')

email.clear()
password.clear()
email.send_keys(config.ACCOUNT)
password.send_keys(config.PASSWD)
password.send_keys(Keys.RETURN)
time.sleep(uniform(4, 8))

# div:
# css-901oao r-jwli3a r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0

# span:
# css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0

# span2:
# /html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[4]/div/div/section/div/div/div[4]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span
# css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0

# div:
# css-901oao r-jwli3a r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0
# css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0

xpath = "/html/body/div/div/div/div/main/div/div/div/div/div/div/div/div/section/div/div/div/div/div/article/div/div/div/div/div/div/div/div/span"
#tweets=driver.find_elements_by_xpath(xpath)
tweets = driver.find_elements_by_css_selector("span .css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0")
texts = [tweet.text for tweet in tweets]
print(tweets[0])
#driver.execute_script("arguments[0].style.color = 'lightblue'", tweets[0])
driver.execute_script("arguments[0].style.color = 'blue'", tweets[0])
print(tweets[0])
