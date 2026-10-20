import re


text = ("Полезные сайты: https://python.org, http://example.com/page, "
        "https://example.com/docs/index.html и ftp://files.example.com/data.")
res = re.findall(r"https?://[^\s<>]+", text)

for i in res:
    print(i.rstrip(".,;:!?"))
