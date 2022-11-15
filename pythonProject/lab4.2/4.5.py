import random

#punkty = []
# for b in range(15):
#     a = random.uniform(0, 50)
#     c = round(a, 2)
#     punkty.append(a)
#print(punkty)
punkty = [round(random.uniform(0, 50), 2) for i in range(15)]
print(punkty)
print(max(punkty), min(punkty))
g = float(input("prosze podać licbę punktów: "))
if g in punkty:
    print(punkty.index(g))
else:
    print("Brak wartości w liście")
b = sum(punkty)/len(punkty)
b = round(b, 2)
print("srednia:", b)

list1 = []
for i in punkty:
    if i < b:
        list1.append(i)
print(len(list1))
print(list1)

list2 = [i for i in punkty if i > b]
print(len(list2))
print(list2)




