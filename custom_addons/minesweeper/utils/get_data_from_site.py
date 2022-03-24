from bs4 import BeautifulSoup
import urllib.request
import time
import json


def get_awards_from_site():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    url = "https://minesweeper.online/ru/help/achievements"

    try:
        with urllib.request.urlopen(url) as response:
            request_result = response.read().decode('utf-8')  # use whatever encoding as per the webpage

    except urllib.request.HTTPError as e:
        if e.code == 404:
            print(f"{url} is not found")
        elif e.code == 503:
            print(f'{url} base webservices are not available')
        else:
            print('http error', e)

    soup = BeautifulSoup(request_result, "html5lib").findChild("tbody", {"id": "rewards_table"})

    result = []
    for i, row in enumerate(soup):
        award = row.findChildren('td')
        award_name = award[0].findChild('img').attrs["alt"]
        award_requirements = award[1].text
        result.append({"award_name": award_name, "award_requirements": award_requirements,})
    return result


def get_players_from_site():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    url = "https://minesweeper.online/ru/best-players"

    try:
        with urllib.request.urlopen(url) as response:
            request_result = response.read().decode('utf-8')  # use whatever encoding as per the webpage

    except urllib.request.HTTPError as e:
        if e.code == 404:
            print(f"{url} is not found")
        elif e.code == 503:
            print(f'{url} base webservices are not available')
        else:
            print('http error', e)

    soup = BeautifulSoup(request_result, "html5lib").findChildren("table", {"class": "table-stat"})
    result = []
    for table in soup:
        for players_row in table.findChildren("tr")[1::]:
            row_cells = players_row.findChildren("td")
            country = row_cells[1].findChild("img").attrs["src"][-6:-4].upper()
            nickname = row_cells[1].findChild("a").getText()
            result.append({"country": country, "nickname": nickname})

    return result


if __name__ == '__main__':
    users = get_players_from_site()
    for user in users:
        print(user)
