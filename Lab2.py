x = int(input("wprowadz wiek:"))
if x < 4:
   cena = 0
elif x >= 4 and x < 18:
    cena = 10
else:
    cena = 20
    print(f"cena biletu", {cena}, "zl")

