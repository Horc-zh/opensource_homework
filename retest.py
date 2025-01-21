import re

print(re.findall(r"\bw[a-z]*", "which foot or hand fell fastest"))

print(re.sub(r"(\b[a-z]+) \1", r"\1", "cat in the the hat hat mother"))

html = """\
<html>
    <head>
    </head>
    <body>
        <h1>Title</h1>
        <p> This is a paragraph</p>
        <table>
            <tr>
                <td> <a href='a.html'>link a</a> </td>
            </tr>
        </table>
        <a href='b.html'>link b</a>
    </body>
</html>
"""
print(re.findall("href='(.*?)'", html))

print(re.match(r"ab*", "abbbb").group())

print(re.match(r"ab*?", "abbbb").group())

print(re.match(r"a\d{3,4}", "a1234567").group())

# 使用|表示或，\|表示字面值
print(re.match(r"(abc)|(def)", "abc").group())

p = re.compile("\d+")
txt = "12 drummers drumming, 11 pipers piping, 10 lords a-leaping"
print(p.findall(txt))

p = re.compile("(a(b)c)d")
m = p.match("abcd")
print(m.group(0))
print(m.group(1))
print(m.group(2))


print(re.findall(r"(.)\1", "你好妈妈生的"))
