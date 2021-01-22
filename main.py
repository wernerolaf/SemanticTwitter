from selenium import webdriver, common
from selenium.webdriver.common.keys import Keys
import time
import config
from twitter import Twitter, OAuth
from process_text import processText
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pickle
from random import uniform
# set driver
driver = webdriver.Firefox()


# login
def sleep():
    time.sleep(uniform(4, 8))

def revisit():
    driver.get("https://twitter.com")
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

def visit():
    driver.get("https://twitter.com/login")
    sleep()

    try:
        email = driver.find_element_by_name('session[username_or_email]')
        password = driver.find_element_by_name('session[password]')
    except common.exceptions.NoSuchElementException:
        sleep()
        email = driver.find_element_by_name('session[username_or_email]')
        password = driver.find_element_by_name('session[password]')

    email.clear()
    password.clear()
    email.send_keys(config.ACCOUNT)
    password.send_keys(config.PASSWD)
    password.send_keys(Keys.RETURN)
    sleep()

    # dump cookies
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

#visit()
revisit()
sleep()


auth = OAuth(
    consumer_key=config.API_KEY,
    consumer_secret=config.API_SECRET,
    token=config.ACCESS_TOKEN,
    token_secret=config.ACCESS_TOKEN_SECRET
)

t = Twitter(auth=auth)

# find and modify your tweets
print(t.statuses.home_timeline())
for tweet_to_modify in t.statuses.home_timeline():
    text=tweet_to_modify["text"]
    tweet = driver.find_elements_by_xpath("//*[contains(text(), '{}')]".format(text))

#sentiment
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    neg = score['neg']
    neu = score['neu']
    pos = score['pos']
    if neg > pos and neg > neu:
        driver.execute_script("arguments[0].style.color = 'red'", tweet[0])
        print("negative")
    elif pos > neu:
        driver.execute_script("arguments[0].style.color = 'green'", tweet[0])
        print("positive")
    else:
        print("neutral")

#wikidata entities
    analyze=processText(text)
    for key in analyze:
        if len(analyze[key]) > 0:
            link="<a href =\"https:{}\">{}</a>".format(analyze[key][0]["url"], key)
            text=text.replace(str(key),str(link))

    driver.execute_script("arguments[0].innerHTML = '{}'".format(text), tweet[0])