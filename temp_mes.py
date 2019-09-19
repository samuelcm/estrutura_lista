#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as
#em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas
#as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês
#por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temp = []

contador = 1

while contador <= 12:
    mes = input('Digite o mes:\n')
    temperatura= float(input("Digite a temperatura media:\n"))
    temp.append ([mes, temperatura])
    contador += 1


valor = 0
for i in temp:
    valor += i[1]

media = valor/12

temp_acima_media = []

for i in temp:
    if i[1]> media:
        temp_acima_media.append (i)
print (media.round(2))
print (temp_acima_media)
