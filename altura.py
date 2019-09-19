#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine
#quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
#pip install numpy
import numpy as np

altura = []
contador = 0
while contador < 30:
    for i in np.arange (1.40, 2.):
        altura.append (i)
    contador += 1

print(altura)
