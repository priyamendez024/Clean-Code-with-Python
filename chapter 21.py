# Chapter 21: Web Scraping with Requests and BeautifulSoup

import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_titles(html):
    soup = BeautifulSoup(html, 'html.parser')
    return [tag.text for tag in soup.select('.title')]

url = 'https://example.com'
html = fetch_html(url)
titles = parse_titles(html)
print(titles)