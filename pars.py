from bs4 import BeautifulSoup
import requests


answer = requests.get ('http://books.toscrape.com/')
if 200 <= answer.status_code < 300:
    soup = BeautifulSoup(answer.content, "html.parser")
    for div in soup.select('.image_container > a'):
        print("http://books.toscrape.com/"+div.get("href"))