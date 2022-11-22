x = 0
y = 0
a = [x, y]
for i in range(2):
    for c in range(20):
        a.append([x, y])
        x += 1
        y = x ** 2
a.pop(1)
a.pop(0)
for i in a:
    print(i)