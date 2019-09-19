#Faça um Programa que peça a idade e a altura de 5 pessoas,
#armazene cada informação no seu respectivo vetor. Imprima a idade e
#a altura na ordem inversa a da ordem lida.

pessoa1_id = int(input("Qual a idade?\n"))
pessoa1_alt = float(input("Qual a altura?\n"))

pessoa1 = [pessoa1_id, pessoa1_alt]

pessoa2_id = int(input("Qual a idade?\n"))
pessoa2_alt = float(input("Qual a altura?\n"))

pessoa2 = [pessoa2_id, pessoa2_alt]

pessoa3_id = int(input("Qual a idade?\n"))
pessoa3_alt = float(input("Qual a altura?\n"))

pessoa3 = [pessoa3_id, pessoa3_alt]

pessoa4_id = int(input("Qual a idade?\n"))
pessoa4_alt = float(input("Qual a altura?\n"))

pessoa4 = [pessoa4_id, pessoa4_alt]

pessoa5_id = int(input("Qual a idade?\n"))
pessoa5_alt = float(input("Qual a altura?\n"))

pessoa5 = [pessoa5_id, pessoa5_alt]

pessoa1.reverse()
print(pessoa1)

pessoa2.reverse()
print(pessoa2)

pessoa3.reverse()
print(pessoa3)

pessoa4.reverse()
print (pessoa4)

pessoa5.reverse()
print(pessoa5)
