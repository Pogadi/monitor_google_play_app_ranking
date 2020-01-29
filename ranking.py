import time
import csv
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver


def is_ranking(class_post):
    app_id = "com.taransit.transport"
    post_app_id = str(class_post)
    if app_id in post_app_id:
        return True
    else:
        return False


def ranking_index(posts):
    i = 0

    for post in posts:
        i += 1
        if is_ranking(post) == True:
            rank = i
            break
        else:
            rank = "UR"

    return rank


def create_url(country, keyword):
    start = 'https://play.google.com/store/search?q='
    core = keyword
    apps = '&c=apps'
    if country == 1:
        country = '&gl=in'
    elif country == 2:
        country = '&gl=sk'
    else:
        country = '&gl=cz'
    url = ('{}{}{}{}'.format(start, core, apps, country))

    return url


def get_keywords():
    with open("keywords.txt") as file:
        keywords = []

        for row in file:
            keyword = row.rstrip('\n.')
            keywords.append(keyword)

    return keywords


def get_data_from_gp(source):
    soup = BeautifulSoup(source, 'html.parser')
    posts = soup.find_all(class_='poRVub')

    return posts


def keywords_to_url():
    with open("keywords.txt") as file:
        keywords = []

        for row in file:
            keyword = row.replace(' ', '%20').lower()
            keyword = keyword.rstrip('\n.')
            keywords.append(keyword)

    return keywords


def scroll_down_page(driver):

    timesleep = 1.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(timesleep)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    #neccessary to sleep program because driver is loading data, in case of slow interner connection, don't load everything
    time.sleep(timesleep)

    source = driver.page_source

    return source


def main():
    start_time = datetime.now()

    driver = webdriver.Chrome('/Users/martin/Documents/STUDY/5_DEV/1_Python_Scrapig/chromedriver')
    #driver = webdriver.Firefox(executable_path='/Users/martin/Documents/STUDY/5_DEV/1_Python_Scrapig/geckodriver')

    filename = datetime.now().strftime("%Y%m%d-%H%M%S")

    with  open('/Users/martin/Documents/WORK/1_TARANSIT/4_ASO/1_Reports/' + filename + '.csv', 'w') as output:

        keywords_url = keywords_to_url()

        print("\nToday ranking status is: \n")

        for keyword in keywords_url:

            word = keyword.replace('%20', ' ')
            url = create_url(1, keyword)

            driver.get(url)
            posts = get_data_from_gp(scroll_down_page(driver))
            rank = ranking_index(posts)

            number = len(posts)

            line = ("{}, {}, {}\n".format(rank, number, word))
            output.write(line)

            print("{} / {}  ~ {} ".format(rank, number, word))


    print("\nYour rank monitoring was successful !")
    print("Time elapsed:", datetime.now() - start_time)
    print("\nHave a nice day. :) \n")

main()