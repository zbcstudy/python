# ImageDownloader - Muhammed Shokr
import os
import re
import requests
from PIL import Image
from io import BytesIO


def image_downloader(url):
    response = requests.get(url)
    text = response.text
    p = r'<img.*?src="(.*?)"[^\>]+>'
    img_addrs = re.findall(p, text)

    for i in img_addrs:
        s = str(i)
        if s.startswith('https') or s.startswith("http"):
            print(s)
            get_image(s)
    return 'DONE'


def get_image(image_url):
    response = requests.get(image_url)
    con = response.content
    bytesObj = BytesIO()
    obj = bytesObj.write(con)
    img = Image.open(obj)
    img.show()


# USAGE
image_downloader(
    "https://www.123rf.com/stock-photo/spring_color.html?oriSearch=spring&ch=spring&sti=oazo8ueuz074cdpc48|")
