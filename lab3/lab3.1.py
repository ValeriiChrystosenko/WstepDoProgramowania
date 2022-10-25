x = int(input("proszę podać x"))
y = int(input("proszę podać y"))
if x < y:
    x, y = y, x
while y <= x:
    print(y)
    y += 1


