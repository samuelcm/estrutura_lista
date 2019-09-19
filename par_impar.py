#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
#Imprima os três vetores.

contador = 0
lista_par = []
lista_impar = []

while contador <20:
    numero = int(input("Digite um numero"))
    if numero%2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

    contador += 1

print(lista_par)
print(lista_impar)
