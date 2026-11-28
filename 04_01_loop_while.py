###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.ç
comptador = 10
while comptador >= 1:
 print(comptador)
 comptador -= 1
  
# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
numero = 1
suma = 0
while numero <= 20:
    if numero % 2 == 0:
        suma += numero
    numero += 1  # Dins del while (mateix nivell que l'if)

print(f"La suma dels parells és {suma}")

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
numero = int(input("Introdueix un número enter positiu: "))
factorial = 1
i = 1
while i <= numero:
    factorial = factorial * i
    i = i + 1

print(f"El factorial de {numero} és {factorial}")

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
contrasenya = ""
while len(contrasenya) < 8:
    contrasenya = input("Introdueix una contrasenya: ")
    if len(contrasenya) < 8:
        print("La contrasenya ha de tenir almenys 8 caràcters. Torna-ho a provar.")

print("Contrasenya vàlida")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
numero = int(input("Introdueix un número: "))
i = 1

while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.
n = int(input("Introdueix un número enter positiu N: "))
num = 2  # El primer número primer és el 2

while num <= n:
    es_primer = True
    divisor = 2
    
    while divisor < num:
        if num % divisor == 0:
            es_primer = False
            break
        divisor += 1
        
    if es_primer:
        print(num)
    num += 1

# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.
suma = 0
numero = int(input("Introdueix un número enter (0 per acabar): "))

while numero != 0:
    suma += numero
    numero = int(input("Introdueix un número enter (0 per acabar): "))

print(f"La suma total és {suma}")

# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.
numero = int(input("Introdueix un número enter positiu: "))
xifres = 0

if numero == 0:
    xifres = 1
else:
    while numero > 0:
        numero = numero // 10
        xifres += 1

print(f"El número té {xifres} xifres.")

# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.
termes = int(input("Quants termes de Fibonacci vols veure? "))
a = 0
b = 1
comptador = 0

while comptador < termes:
    print(a)
    seguent = a + b
    a = b
    b = seguent
    comptador += 1

# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.
secret = 7
intent = 0

while intent != secret:
    intent = int(input("Endevina el número secret: "))
    if intent < secret:
        print("El número secret és més gran.")
    elif intent > secret:
        print("El número secret és més petit.")

print("Correcte! Has encertat el número secret.")