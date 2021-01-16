from selenium import webdriver, common
from selenium.webdriver.common.keys import Keys
import time

try:
    f=open("/home/olaf/twitterPassword","r")
    f.readline()
    ACCOUNT = f.readline().strip()
    f.readline()
    PASSWORD = f.readline().strip()
except:
    print("no file found")
finally:
    f.close()

driver = webdriver.Firefox()
driver.get("https://twitter.com/")


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
email.send_keys(ACCOUNT)
password.send_keys(PASSWORD)
password.send_keys(Keys.RETURN)
time.sleep(4)
tweet=driver.find_elements_by_xpath("//*[contains(text(), 'unique_tweet_to_color')]")
print(tweet)
#driver.execute_script("arguments[0].style.color = 'lightblue'", tweet[0])
driver.execute_script("arguments[0].style.color = 'blue'", tweet[0])
print(tweet)