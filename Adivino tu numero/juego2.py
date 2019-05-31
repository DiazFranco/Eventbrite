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

print ("Te desafío a que adivino el número de 4 cifras que estas pensando!")
print ("Instrucciones: Me debes responder en bien, las cifras que están en la posición correcta y en regular, las cifras que se encuentren dentro de tu número pero en diferente posición")


#Guardamos las respuestas separables
while True: 
 print ('¿Tu número es : ' , codigo , '?')
 bien = input("Bien: ")
 regular = input("Regular: ")
 if bien == "4":
      print("Adiviné tu número! Es: ", codigo) 
 break

numero = int(codigo)  

candidato2 = numero + 1

while candidato2 != codigo:
    b= 0
    r = 0
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    for i in range(4):   
     if str(codigo)[0:1] == str(candidato2)[0:1] :
        num1 = 1
        b = 1  
     if str(codigo)[1:2] == str(candidato2)[1:2]:
        num2 = 1
        b = b + 1
     if str(codigo)[2:3] == str(candidato2)[2:3]:
        num3 = 1
        b = b + 1
     if str(codigo)[3:4] == str(candidato2)[3:4]:
        num4 = 1
        b = b + 1
     if str(candidato2)[0:1]  in str(codigo) and num1 != 1:
        r =  1
     if str(candidato2)[1:2]  in str(codigo) and num2 != 1:
        r = r + 1
     if str(candidato2)[2:3]  in str(codigo) and num3 != 1:
        r = r + 1
     if str(candidato2)[3:4]  in str(codigo) and num4 != 1:
        r = r + 1 
     continue
while b == bien and r == regular:
   print("Tu número es: ", candidato2,  "?") 
   bien = input("Bien: ")
   regular = input("Regular: ")



  















      





       


 
