import re


text = "Это   строка    с     большим    количеством   пробелов."
res = re.sub(r" +", " ", text).strip()
print(res)

text = "   Текст   с   пробелами   "
res = re.sub(r" +", " ", text).strip()
print(res)
