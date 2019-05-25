import random

digitos = ('0','1','2','3','4','5','6','7','8','9')

codigo = ''
for i in range(4):
    candidato = random.choice(digitos)
    # vamos eligiendo digitos no repetidos*
    while candidato in codigo:
        candidato = random.choice(digitos)
    codigo = codigo + candidato

print ('¿Tu número es : ' + codigo + '?')

respuesta = input()

for i in range(4):
    if respuesta[:2] 
       


 
