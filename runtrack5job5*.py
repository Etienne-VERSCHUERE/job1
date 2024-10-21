import random
L = []
for i in range(1,6):
    random_int = random.randint(1,10)
    L.append(random_int)
print(L)
print(L[1])
L[3]=L[2]+L[4]
print(L)
print(L[4])