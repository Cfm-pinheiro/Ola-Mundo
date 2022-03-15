'''Calcule seu IMC
paramentros:
- 18.5: abaixo do peso
- 18,5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida'''


from time import sleep

massa  =  float ( input ( "Digite seu peso (em kg): " ))
altura  =  float ( input ( "Digite sua altura (em m):  " ))

imc  = ( massa  / ( altura ** 2 ))

print('Calculando')
sleep(0.50)
print('Seu')
sleep(0.50)
print('Imc')
sleep(0.50)

if  imc  <  18.5:
    print ( "Seu IMC é de: {:.1f}. \33[1;33m Atenção abaixo do peso. " . format ( imc ))
elif  imc < 25:
    print ( "Seu IMC é de: {:.1f}. \33[1;32m Você está no peso ideal." . format ( imc ))
elif  imc < 30:
    print ( "Seu IMC é de: {:.1f}. \33[1;35m Você está com sobrepeso." . format ( imc ))
elif  imc  < 40:
    print ( "Seu IMC é de : {:.1f}. \33[1;31m Você está com obesidade." . format ( imc ))
else:
    print ( "Seu IMC é de {:.1f}. \33[4;31m Você está com obesidade mórbida." . format ( imc ))
