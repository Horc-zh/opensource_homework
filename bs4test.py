import requests
import bs4

url = "http://oscar-lab.org/people/~zren/"
response = requests.get(url)
print(response.status_code)

print(response.encoding)

print(response.apparent_encoding)

response.encoding = response.apparent_encoding
# print(response.text)

doc = bs4.BeautifulSoup(response.text)
print(doc.prettify())
doc.a  # 文档中的首个a节点

doc.title  # 文档首个（唯一）标题

print(doc.title.parent)  # 使用parent遍历父节点

print(list(doc.title.parents))  # 反向遍历祖先节点


def tree(node, prefix, last):
    if not isinstance(node, bs4.element.Tag):
        pass
    else:
        print(prefix + last + node.name)
        children = [c for c in node.children if isinstance(c, bs4.element.Tag)]
        if children:
            for child in children[:-1]:
                tree(child, prefix + " |", "--")
            tree(children[-1], prefix + "  ", "`-")


tree(doc, "", "")
