import re


text = "alice@example.com bob@test.org alice@example.com admin@company.ru"
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
res = []

for i in emails:
    if i not in res:
        res.append(i)

for i in res:
    print(i)
