#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma,
# a multiplicação e os números.
numeros = list(range(1,6))

soma = sum(numeros)
produto = 1
for n in numeros:
    produto *= n

print (produto)
print(numeros)
print(soma)
