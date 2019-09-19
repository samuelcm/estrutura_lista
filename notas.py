#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num
#vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

contador = 0
media_alunos = []

while contador <10:
    nota1 = int(input("Digite uma nota"))
    nota2 = int(input("Digite uma nota"))
    #nota3 = int(input("Digite uma nota"))
    #nota4 = int(input("Digite uma nota"))
    media = (nota1 + nota2)/2
    media_alunos.append(media)
    contador = contador +1

alunos = [d for d in media_alunos if d>=7]
print(alunos)
