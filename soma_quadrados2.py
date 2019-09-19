#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre
#a soma dos quadrados dos elementos do vetor.
lista = list(range(10))
valor = 0
for i in lista:
    valor += i**2
print(valor) 
