#Faça um Programa que leia dois vetores com 10 elementos cada.
#Gere um terceiro vetor de 20 elementos, cujos valores deverão ser
#compostos pelos elementos intercalados dos dois outros vetores.
#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

lista1 = list(range(10))
lista2 = list(range(10, 20))
lista3 = list(range(20,30))
print(lista3)
lista4 = [x for x in lista1]

n=1

for i in lista2:
    lista4.insert(n, i)
    n = n+2


lista5 = [x for x in lista4]

p = 2
for i in lista3:
    lista5.insert(p,i)
    p = p + 2
print(lista4)
print(lista5)
