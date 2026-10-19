import re


products = [
    "PRD-12345",
    "PRD-00123",
    "USR-12345",
    "PRD-987",
    "PRD-ABCDE",
    "PRD-54321"
]
res = []

for i in products:
    if re.fullmatch(r"PRD-[0-9]{5}", i):
        res.append(i)

print(res)
