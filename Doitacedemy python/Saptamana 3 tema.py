'''
Problema1
a = int(input("Valoarea lui a este=: "))
b = int(input("Valoarea lui b este=: "))
c = int(input("Valoarea lui c este=: "))
print(type(a))
x = (c-b) / a
print("Valorea necunoscutei x este=", x)

Problema2
a = input("Introduceti va rog un string: ")
print("Stringul cu majuscule va arata asa: ",a.upper())
'''

'''''
Problema3
a = input("Introduceti va rog un string:")
if(str.isdigit(a) == True):
    print("Sunt doar cifre in string")
else:
    print("Nu sunt doar cifre in string")
'''''
'''
Problema 4
a = int(input("Va rog sa introduceti un numar: "))
if(a % 2 == 0):
    print("numarul este par")
else:
    print("numarul nu este par")
'''
'''
Problema 5
a = input("Va rog sa introduceti un string: ")
if(str.isdigit(a) == True):
    print("Stringul devine numar intreg", int(a))
else:
    print("Eroare")
'''

'''
#Problema 6
a = input("Va rog sa introduceti un string: ")
b = input("Va rog sa introduceti un numar: ")
if(len(a) == b):
    print("Lungimea stringului este egala cu numarul", b)
else:
    print("Lungimea stringului nu este egala cu numarul introdus", b)
'''

'''
#Problema 7
n = int(input("Va rog sa introduceti un string: "))
i = 0
while (i <= n):
        print(i)
        i = i + 1
'''
'''
#problema 8
n = int(input("Va rog sa introduceti un string: "))
i = 0
while (i <= n):
    if(i % 2 == 0):
        print(i)
    i = i + 1
'''

'''
#Problema 9
n = int(input("Va rog sa introduceti un numar: "))
invers = 0
while n !=0:
    invers = invers * 10 + n % 10
    n = n // 10
'''