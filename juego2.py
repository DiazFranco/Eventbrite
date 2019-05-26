import random

# variable que utilizaremos para seleccionar un numero al azar
numeros = ('0','1','2','3','4','5','6','7','8','9')

codigo = ''
for i in range(4):
    candidato = random.choice(numeros)
    # elegimos numeros que no se repitan
    while candidato in codigo:
        candidato = random.choice(numeros)
    codigo = codigo + candidato

print ("Te desafío a adivinar el número de 4 cifras que estas pensando!")
print ("Instrucciones: Me debes responder 1B (1 bien, en caso de que algun numero esté en la posición correcta y 1R (1 regular, en caso de que exista pero no esté en la posición)")
codigo = 1234
print ('¿Tu número es : ' , codigo , '?')

numero = int(codigo)  

respuesta = input("Responde: ")

#Guardamos las respuestas separables

for i in respuesta:
    var1 = respuesta[0:1]
    var2 = respuesta[3:4]
    candidato2 = numero + 1
    num1= 0
    if str(codigo)[0:1] == str(candidato2)[0:1]:
        num1 = 1
    else:
        num1 = 0    
    if str(codigo)[1:2] == str(candidato2)[1:2]:
        num2 = 1
    else:
        num2=0
    if str(codigo)[2:3] == str(candidato2)[2:3]:
        num3 = 1
    else:
        num3=0
    if str(codigo)[3:4] == str(candidato2)[3:4]:
        num4 = 1
    else:
        num4=0
    if str(candidato2)[0:1] in str(codigo) and num1 == 1:
        num11 = 0
    else: 
        num11 = 1    
    if str(candidato2)[1:2] in str(codigo) and num2 == 1:
        num22 = 0
    else: 
        num22 = 1 
    if str(candidato2)[2:3] in str(codigo) and num3 == 1:
        num33 = 0
    else: 
        num33 = 1   
    if str(candidato2)[3:4] in str(codigo) and num4 == 1:
        num44 = 0
    else: 
        num44 = 1  

print("respuesta1: " ,num1+num2+num3+num4, "respuesta2: ", num11+num22+num33+num44)      













      





       


 
