from bs4 import BeautifulSoup
import csv
import requests
from _datetime import datetime


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
            rank = ">50"

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


def get_data_from_gp(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
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


def main():
    filename = datetime.now().strftime("%Y%m%d-%H%M%S")
    with  open(filename + '.csv', 'w') as output:

        keywords_url = keywords_to_url()

        print("\nToday ranking status is: \n")

        for keyword in keywords_url:
            word = keyword
            url = create_url(1, keyword)
            posts = get_data_from_gp(url)
            rank = ranking_index(posts)

            line = ("{}, {}\n".format(word, rank))
            output.write(line)

            print("{} ranked at: {}".format(word, rank))

    print("\nYour rank monitoring was successful ! \n\nHave a nice day. :) ")

main()