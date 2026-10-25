###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.
num_1 = int(input("Introduiex un nombre:"))
num_2 = int(input("Introduiex un nombre:"))
if num_1 > num_2:
   print(f"El numero {num_1} es mes gran")
else:
   print(f"El numero {num_2} es mes gran")


# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).

num_1 = int(input("Introduiex un nombre:"))
num_2 = int(input("Introduiex un nombre:"))
resultat_suma = num_1 + num_2
print(f"El resultat de la suma es: {resultat_suma}")

# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.

any_transpas = int(input("Introdueix un any:"))

if any_transpas % 4 == 0: 
 print("L'any es de transpas")

elif any_transpas % 100 == 0:
 print("L'any no es de tranpas")

elif any_transpas % 400 == 0:
 print("L'any es de transpas")

else: 
  print("L'any no es de transpas")

# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)
edat=int(input("Introdueix una edat:"))
if edat <= 2:
  print("Nado")
elif edat >= 3 and edat <=12:
  print("Infant")
elif edat >= 13 and edat <=17:
  print("Adolescent")
elif edat >= 18 and edat <=64:
  print("Adult")
else:
  print("Persona gran")


# Exercici 5: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
senyal_rebuda =float(input("Introdueix la senyal rebuda en dBm:"))
if senyal_rebuda >= -50:
 print("Cobertura excel·lent")
elif senyal_rebuda >= -67:
  print("Bona")
elif senyal_rebuda >= -75:
  print("Feble")
else:
  print("Molt fiable")

# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
potencia_optica = float(input("Introdueix la potencia rebuda en dBm:"))
if potencia_optica >= -27:
  print("Potencia baixa")
elif potencia_optica >= -8:
 print("Potencia acceptable")
else:
  print("Potencia alta")

# Exercici 7: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
GB_consumits = float(input("Quants Gb tens cosumits aquest mes:"))
gb_totals = GB_consumits-20
if GB_consumits == 20:
  print("Estas dins del limit de Gb consumits.")
elif GB_consumits > 20:
  print("Has passat el limit de Gb contractat.")
  print(f"El consum total de Gb superior al teu limit es de {gb_totals} Gb")



# Exercici 8: Diagnòstic d'una connexió de fibra
# Demana si l'indicador del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
indicador_terminal = input("El indicador del terminal actiu?\n")
indicador_router = input("El indicador del router esta actiu?\n")
if indicador_terminal == 'si':
  print("Cal revisar cable de la fibra")
elif indicador_router!= "si":
    print("Cal comprovar el servei del proveïdor.")
else:
    print("La connexió sembla funcionar correctament.")

# Exercici 9: Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
percentatge_bateria_SAI = int(input("Quin es el percentatge disponible al SAI?\n"))
if percentatge_bateria_SAI < 20:
  print("Nivell de bateria critic!!")
elif percentatge_bateria_SAI >= 20 and percentatge_bateria_SAI <= 49:
  print("Nivell de bateria baix.")
elif percentatge_bateria_SAI >= 50 and percentatge_bateria_SAI <= 100:
  print("Nivell de bateria suficient.")
else:
  print("Valors fora del rang.")


# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.
latencia = float(input("Introdueix el nivell de latencia en ms:"))
perdua = float(input("Introdueix el percentatge de paquets perduts:"))
if latencia < 0:
  print("La latencia no pot tindre un valor negatiu")
elif perdua < 0 or perdua > 100:
  print("La perdua ha de estar entre el 0 i el 100 %.")
elif latencia <= 30 and perdua <= 1:
  print("La conexio es excel·lent.")
elif latencia <= 80 and perdua <= 3:
  print("La conexio es bona.")
elif latencia <= 150 and perdua <= 5:
  print("La conexio es acceptable.")
else:
  print("La conexio es deficient.")

# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.
pla = input("Introdueix el tipus de pla (basic o plus): ")
consum_mensual = int(input("Introdueix el consum mensual en Gb: "))

if consum_mensual < 0:
    print("El consum no pot ser negatiu.")
elif pla != "basic" and pla != "plus":
    print("Pla no disponible al nostre catàleg.")
elif pla == "basic":
    # Si supera els 10 GB inclosos, calculem l'excés
    if consum_mensual > 10:
        gb_extres = consum_mensual - 10
        cost_total = 10 + (gb_extres * 1.50)
    else:
        cost_total = 10
    print(f"El cost total és de {cost_total} euros.")
elif pla == "plus":
    # Si supera els 30 GB inclosos, calculem l'excés
    if consum_mensual > 30:
        gb_extres = consum_mensual - 30
        cost_total = 20 + (gb_extres * 0.75)
    else:
        cost_total = 20 
    print(f"El cost total és de {cost_total} euros.")

# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.

if compte_actiu != "si":
    print("Accés denegat: el compte està desactivat.")
else:
    contrasenya = input("Introdueix la contrasenya: ")
    if contrasenya != "correcta":  # Pots adaptar-ho a la teva contrasenya de prova
        print("Accés denegat: la contrasenya és incorrecta.")
    else:
        codi_2fa = input("Introdueix el codi de doble verificació: ")
        if codi_2fa != "1234":  # Pots adaptar-ho al codi de prova
            print("Accés denegat: falla el codi de verificació.")
        else:
            print("Accés permès: benvingut al teu compte.")

# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.
router_ences = input("El router està encès? (si/no): ")
if router_ences != "si":
    print("Cal encendre el router.")
else:
    indicador_los = input("L'indicador LOS està encès? (si/no): ")
    if indicador_los == "si":
        print("Cal revisar el cable de fibra.")
    else:
        indicador_internet = input("L'indicador d'Internet està encès? (si/no): ")
        if indicador_internet != "si":
            print("Cal contactar amb el proveïdor.")
        else:
            print("La connexió funciona correctament.")

# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.
servei_critic = input("Afecta un servei crític? (si/no): ")
usuaris_afectats = int(input("Introdueix el nombre d'usuaris afectats: "))
alternativa = input("Hi ha una alternativa de connexió disponible? (si/no): ")

if usuaris_afectats < 0:
    print("Error: El nombre d'usuaris no pot ser negatiu.")
elif (servei_critic == "si" and alternativa == "no") or (usuaris_afectats >= 50 and alternativa == "no"):
    print("Prioritat: Crítica")
elif usuaris_afectats >= 10 or servei_critic == "si":
    print("Prioritat: Alta")
else:
    print("Prioritat: Baixa")