# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida
vel1 = int(input("digite a velocidade"))
if (vel1>60) :
    print ("multa")
multa = (vel1-60)*7
print (f"sua multa é {multa}")
