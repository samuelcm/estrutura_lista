#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre
#a soma dos quadrados dos elementos do vetor.
lista = list(range(10))

lista_n = [x**2 for x in lista]

Sum = sum(lista_n)
print (Sum)
