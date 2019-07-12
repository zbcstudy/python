import bs4
import ssl
import lxml
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


def news(xml_news_url):
    context = ssl._create_unverified_context()
    client = urlopen(xml_news_url, context=context)
    xml_page = client.read()
    client.close()

    soup_page = soup(xml_page, "xml")
    new_list = soup_page.findAll("item")

    for news in new_list:
        print(f'new title: {news.title.text}')
        print(f'news link:    {news.link.text}')
        print(f'news pubDate: {news.pubDate.text}')
        print("+-"*20, "\n\n")


news_url = "http://baijiahao.baidu.com/s?id=1628515595093586707"
sports_url = "https://news.google.com/news/rss/headlines/section/topic/SPORTS.en_in/Sports?ned=in&hl=en-IN&gl=IN"


news(news_url)
# news(sports_url)


