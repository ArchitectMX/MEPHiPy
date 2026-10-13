import csv

with open("/Users/timurberendeev-mac/Visual Studio/MEPHi/Python/TasksSeminar4/products.csv", "r") as f:
    reader = csv.DictReader(f)
    lst = []
    for i in reader:
        if int(i["price"]) > 100:
            lst.append(i)

with open("expensive.csv", "w", newline="") as nf:
    writter = csv.DictWriter(
        nf,
        fieldnames=['name', 'category', 'price']
    )

    writter.writeheader() 
    writter.writerows(lst)


