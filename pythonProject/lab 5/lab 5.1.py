a1 = [10, 20, 30]
a2 = ["ten", "twenty", "thirty"]
#D1 = dict(zip(a1, a2))
#print(D1)
#print(list(zip(a1, a2)))
D1={}
for i in range (len(a2)):
    D1[a2[i]]=a1[i]
print(D1)
D1={a2[i]:a1[i] for i in range (len(a2))}
print(D1)

D2 = dict(thirty=30,forty=40, fifty=50)
print (D2)

D3={}
D3.update(D1)
D3.update(D2)
print(D3)

