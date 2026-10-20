import re


text = "+7 999 123-45-67, 8 999 123-45-67, +7 (999) 123-45-67, 8 (999) 123-45-67"
pattern = r"(?<!\w)(?:\+7|8) (?:\(\d{3}\)|\d{3}) \d{3}-\d{2}-\d{2}(?!\d)"
res = re.findall(pattern, text)

for i in res:
    print(i)
