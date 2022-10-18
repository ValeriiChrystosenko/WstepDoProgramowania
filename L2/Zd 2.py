x = input("Wprowadz litery:")
if len(x) > 1 or len(x) == 0:
    print("blad")
    exit()
if 'a' <= x <= 'z':
    print("litera jest mala")
elif 'A' <= x <= 'z':
    print("litera jest duza")
else:
    print("to nie jest litera")