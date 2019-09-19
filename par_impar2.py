#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
#Imprima os três vetores.


numeros = list(range(20))
print(numeros)

lista_par = [n for n in numeros if n%2==0]
print(lista_par)
lista_impar = [n for n in numeros if n%2 !=0]
print(lista_impar)
