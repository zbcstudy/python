import requests
from lxml import html, etree

def spider(sn):
    # 爬取一号店的数据
    url = "https://list.tmall.com/search_product.htm?q={0}".format(sn)
    # 获取HTML源码
    html_doc = requests.get(url).text
    # xpath 对象
    selector = html.fromstring(html_doc)
    ul_list = selector.xpath('//div[@id="J_ItemList"]/div')
    print(len(ul_list))
    for li in ul_list:
        price_html = li.xpath('//product/p[@class="productPrice"]/p')
        print(etree.tostring(price_html))


if __name__ == '__main__':
    spider("python")
