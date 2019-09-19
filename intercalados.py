#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro
#vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
#intercalados dos dois outros vetores.

lista1 = list(range(10))
#print(lista1)

lista2 = list(range(10, 20))
#print(lista2)

lista3 = [x for x in lista1]
n = 1

for i in lista2:
    lista3.insert(n, i)
    n = n+2

print(lista3)
