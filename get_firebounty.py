from bs4 import BeautifulSoup
import requests

for i in range(1,714):
    url = "https://firebounty.com/?page={}&sort=created_at&search_field=name&order=desc&search=".format(i)



    # 替换为你想要提取数据的网页地址
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    divs = soup.find_all("div", {"class": "Rtable-row", "data-url": True})
    urls = [div["data-url"] for div in divs]

    for url in urls:
        b="https://firebounty.com" + url
        with open('./cccc.txt', 'a+', encoding='UTF-8') as fp:
            page_txt = fp.write(b + "\n")
            fp.read()
        fp.close()
