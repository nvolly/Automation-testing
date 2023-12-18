
#Problema 10
a = input("Introduceti un string: ")
print("\n".join(a))

#problema 11
s = 0
p = 1
n = int(input("introduceti limita: "))
for i in range(n+1):
    if (i % 2 == 0):
        s = s + i
        i = i + 1
    else:
        p = p * i
        i = i + 1
print("Suma numerelor pare este", s)
print("Produsul numerelor impare este",p)


Problema 12
n = int(input("Introduceti o limita: "))
for i in range(10, n+1):
    i_str = str(i)
    if (i_str == i_str[::-1]):
        print(i)

Problema 13
n = int(input("Introduceti un numar: "))
if n > 1:
    for i in range(2, n):
        if (n % i == 0):
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")
else:
    print(num,"is not a prime number")


#problema 14
limita = int(input("Introduceti limita: "))
for i in range(2,limita+1):
    for j in range(2, limita):
        if (i % j == 0 and j % i == 0):
            print(i,"Este un numar prim")
            break
    else:
        print(i,"Nu este un numar prim")