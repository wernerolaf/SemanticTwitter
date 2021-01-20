from selenium import webdriver, common
from selenium.webdriver.common.keys import Keys
import time
import config
from twitter import Twitter, OAuth
# set driver
driver = webdriver.Firefox()
driver.get("https://twitter.com/")
time.sleep(4)


# login
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
time.sleep(4)

auth = OAuth(
    consumer_key=config.API_KEY,
    consumer_secret=config.API_SECRET,
    token=config.ACCESS_TOKEN,
    token_secret=config.ACCESS_TOKEN_SECRET
)

t = Twitter(auth=auth)

# find and modify your tweets
for tweet_to_modify in t.statuses.home_timeline():
    tweet = driver.find_elements_by_xpath("//*[contains(text(), '{}')]".format(tweet_to_modify["text"]))

    #driver.execute_script("arguments[0].style.color = 'lightblue'", tweet[0])
    driver.execute_script("arguments[0].style.color = 'blue'", tweet[0])
    driver.execute_script("arguments[0].innerHTML = 'magicmagic'", tweet[0])