x = input("wprowadz litere: ")
if len(x)>1 or len(x)==0:
    print("blad")
    exit()
n=ord('a')-ord('A') #x=32
if 'a'<= x <='z':
    print(chr(ord(x)-n))
elif 'A' <= x <='Z':
    print(chr(ord(x)+n))
else:
    print("to nie jest litera")