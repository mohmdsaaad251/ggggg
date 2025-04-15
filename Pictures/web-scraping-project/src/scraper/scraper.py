import requests
from bs4 import BeautifulSoup
import time
import random
from fake_useragent import UserAgent

ua = UserAgent()

def fetch_data(url):
    headers = {
        "User-Agent": ua.random
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def parse_data(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    try:
        price = soup.find("span", {"class": "text-2xl"}).text
        return price
    except AttributeError:
        print("Failed to extract data. The structure might have changed.")
        return None

def scrape(url):
    html_content = fetch_data(url)
    if html_content:
        price = parse_data(html_content)
        return price
    return None