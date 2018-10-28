
import datetime as dt
import os
import time

import requests as req
from bs4 import BeautifulSoup as bs
import json
import Config


def handle_word(word_to_translate):
    if word_to_translate == 'USA':
        return 'United_States'
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={}&lang={}'.format(
        Config.key, word_to_translate, 'no-en')
    res = req.get(url, timeout=10)
    soup = bs(res.content, 'html.parser')
    json_dict = json.loads(soup.text)
    obj = json_dict['text'][0]
    return obj.replace(' ', '_')


def get_location(location):
    try:
        url = 'https://www.yr.no/soek/soek.aspx?sted=' + \
            location+'&land=&region1=&sok=Search'
        res = req.get(url, timeout=10)
        soup = bs(res.content, 'html.parser')
        content = soup.find('a', {"title": location}).get('href')
        words = list(filter(None, content.split("/")))

        words = [w.replace(w,handle_word(w)) for w in words]
        words[-1] = location.replace(' ', '_')
        return 'https://www.yr.no/' + '/'.join(words)
    except:
        print('Could not get forecast for that location. Please check if {} is a valid location.'.format(location))
        quit()


def get_forecast(url):
    try:
        res = req.get(url, timeout=10)
        content = bs(res.content, 'html.parser')
        return content.findAll('div', {"class": "yr-content-stickynav-three-fifths"})
    except:
        print('Could not get information. Please contact the developer.')
        quit()


def get_today(soup):
    print(soup[0].findAll('caption')[0].text)
    body = soup[0].findAll('tbody')[0].findAll('tr')
    for content in body:
        for weather in content.findAll('td'):
            print(weather.get('title', ''))
    print("""

    ---------------------------

    """)


def get_tomorrow(soup):
    print(soup[0].findAll('caption')[1].text)
    body = soup[0].findAll('tbody')[1].findAll('tr')
    for content in body:
        for weather in content.findAll('td'):
            print(weather.get('title', ''))
    print("""

    ---------------------------

    """)


def get_overmorrow(soup):
    print(soup[0].findAll('caption')[2].text)
    body = soup[0].findAll('tbody')[2].findAll('tr')
    for content in body:
        for weather in content.findAll('td'):
            print(weather.get('title', ''))


def main():
    location = input('Please enter a town or city: ')
    url = get_location(location)
    soup = get_forecast(url)
    
    get_today(soup)
    get_tomorrow(soup)
    get_overmorrow(soup)


if __name__ == "__main__":
    main()
