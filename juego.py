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

print ("Te desafío a adivinar el número de 4 cifras que estoy pensando!")
print ("Te dejo una ayuda, las cifras son distintas")


while True:
    respuesta = input("¿Que número crees que estoy pensando?: ")
    valida = True
    for letra in respuesta:
        if letra not in numeros:  #Validamos que ingrese sólo números
           print("Debe ingresar numeros ")
           valida = False
           break   
        elif len(respuesta)!= 4:  #Validamos que ingrese sólo números de 4 cifras
           print("Debe ingresar números de 4 cifras") 
           valida = False
           break   

    if valida == True:
        break                    
            

#Contamos los intentos y respuestas regulares o correctas
intentos = 1
while respuesta != codigo:
    intentos = intentos + 1
    bien = 0
    regular = 0

    # recorremos la respuesta del usuario y comparamos en el codigo
    for i in range(4):
        if respuesta[i] == codigo[i]:
            bien = bien + 1
        elif respuesta[i] in codigo:
            regular = regular + 1
    print ("Tu respuesta ", respuesta, " tiene", bien, \
          "numero/s correcto/s y ", regular, "numero/s en posición incorrecta.")
    # pedimos siguiente respuesta
    respuesta = input("Ingresa otro número: ")  

print ("Felicitaciones! Adivinaste el codigo en", intentos, "intentos.")