# 题目： 从文档中找到所有<a>标签的链接；


from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
links = []
# with open('result.txt', 'w') as f:
soup = BeautifulSoup(html_doc, "html.parser")

# 核心在于通过 get_text() 方法获取去除掉标签之后的所有文本。
whole_text = soup.get_text()

print(whole_text)
