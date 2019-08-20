# 题目： 从文档中找到所有<a>标签的链接；

from bs4 import BeautifulSoup
from urllib import request

with open('result.txt', 'w') as f:
    links = []
    html = request.urlopen("http://www.ukcert.org.uk/repository/archive/db/")
    soup=BeautifulSoup(html, "html.parser")

    # with open('result.txt', 'w') as f:
    # soup = BeautifulSoup('C:\Users\e0267730\Desktop\Indexofrepositoryarchivedb.html.html', )

    for i in soup.find_all('a'):
        # 注意这里使用 get_url() 跑不出来结果。
        links.append(i.get('href'))
    f.write(str(links))
