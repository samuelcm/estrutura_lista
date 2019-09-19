#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
#As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
#participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
#ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
#Caso contrário, ele será classificado como "Inocente".


perguntas = []

p1 = input('Telefonou para a vítima?')
p2 = input("Esteve no local do crime?")
p3 = input("Mora perto da vítima?")
p4 = input("Devia para a vítima?")
p5 = input("Já trabalhou com a vítima?")

perguntas.append(p1)
perguntas.append(p2)
perguntas.append(p3)
perguntas.append(p4)
perguntas.append(p5)


valor = 0
for i in perguntas:
    if i == 'sim':
        valor +=1
    else:
        valor+=0

print(valor)

if valor == 2:
    print("Suspeita")
elif valor >=3 and valor <=4:
    print("Cumplice")
elif valor == 5:
    print('Assassino')
else:
    print('Inocente')
