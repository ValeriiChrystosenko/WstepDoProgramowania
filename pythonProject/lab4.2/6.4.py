def zad3(*args):
    print(args)
    for a in args :
        print(a)
    print()

def max(num1, *args):
    m = num1
    for i in args:
        if m < i:
            m = i
    return m
print(max(1, -4, 6))

