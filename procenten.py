import random 
import math
import time

print("Welkom bij de procenten trainer!")

print("Kies een type som om te oefenen:")
print("1. Bereken het percentage van een getal")
print("2. Bereken het getal als je het percentage weet")
print("3. Bereken het percentage tussen twee getallen")
print("4. Bereken het getal na een procent toename of afname")  
print("5. bereken de procent toename of afname tussen twee getallen")
print("6. Afsluiten")
keuze = input("Voer het nummer van je keuze in (1-6): ")
while keuze != '6':
    if keuze == '1':
        getal = random.randint(1, 100)
        percentage = random.randint(1, 100)
        correct_antwoord = (percentage / 100) * getal
        start_tijd = time.time()
        antwoord = float(input(f"Wat is {percentage}% van {getal}? "))
        eind_tijd = time.time()
        if math.isclose(antwoord, correct_antwoord, rel_tol=1e-2):
            print(f"Correct! Het antwoord is {correct_antwoord:.2f}. Tijd genomen: {eind_tijd - start_tijd:.2f} seconden.")

        else:
            print(f"Fout! Het juiste antwoord is {correct_antwoord:.2f}. Tijd genomen: {eind_tijd - start_tijd:.2f} seconden.")
    elif keuze == '2':
        getal = random.randint(1, 100)
        percentage = random.randint(1, 100)
        correct_antwoord = (getal * 100) / percentage
        start_tijd = time.time()
        antwoord = float(input(f"Welk getal is {percentage}% van {getal}? "))
        eind_tijd = time.time()
        if math.isclose(antwoord, correct_antwoord, rel_tol=1e-2):
            print(f"Correct! Het antwoord is {correct_antwoord:.2f}. Tijd genomen: {eind_tijd - start_tijd:.2f} seconden.")
        else:
            print(f"Fout! Het juiste antwoord is {correct_antwoord:.2f}. Tijd genomen: {eind_tijd - start_tijd:.2f} seconden.")
    elif keuze == '3':
        getal1 = random.randint(1, 100)
        getal2 = random.randint(1, 100)
        correct_antwoord = (abs(getal2 - getal1) / getal1) * 100
        start_tijd = time.time()
        antwoord = float(input(f"Welk percentage is het verschil tussen {getal1} en {getal2} ten opzichte van {getal1}? "))
        eind_tijd = time.time()
        if math.isclose(antwoord, correct_antwoord, rel_tol=1e-2):
            print(f"Correct! Het antwoord is {correct_antwoord:.2f}%. Tijd genomen: {eind_tijd - start_tijd:.2f} seconden.")
        else:
            print(f"Fout! Het juiste antwoord is {correct_antwoord:.2f}%. Tijd genomen: {eind_tijd - start_tijd:.2f} seconden.")
    elif keuze == '4': 
        getal = random.randint(1, 100)
        percentage = random.randint(1, 100)
        toename_of_afname = random.choice(['toename', 'afname'])
        if toename_of_afname == 'toename':
            correct_antwoord = getal * (1 + percentage / 100)
            vraag = f"Wat is het resultaat van een {percentage}% toename van {getal}? "
        else:
            correct_antwoord = getal * (1 - percentage / 100)
            vraag = f"Wat is het resultaat van een {percentage}% afname van {getal}? "
        start_tijd = time.time()
        antwoord = float(input(vraag))
        eind_tijd = time.time()
        if math.isclose(antwoord, correct_antwoord, rel_tol=1e-2):
            print(f"Correct! Het antwoord is {correct_antwoord:.2f}. Tijd genomen: {eind_tijd   - start_tijd:.2f} seconden.")
        else:
            print(f"Fout! Het juiste antwoord is {correct_antwoord:.2f}. Tijd genomen: {eind_tijd - start_tijd:.2f} seconden.")
    elif keuze == '5':
        getal1 = random.randint(1, 100)
        getal2 = random.randint(1, 100)
        correct_antwoord = ((getal2 - getal1) / getal1) * 100
        start_tijd = time.time()
        antwoord = float(input(f"Welk is de procentuele {'toename' if getal2 > getal1 else 'afname'} van {getal1} naar {getal2}? "))
        eind_tijd = time.time()
        if math.isclose(antwoord, correct_antwoord, rel_tol=1e-2):
            print(f"Correct! Het antwoord is {correct_antwoord:.2f}%. Tijd genomen: {eind_tijd - start_tijd:.2f} seconden.")
        else:
            print(f"Fout! Het juiste antwoord is {correct_antwoord:.2f}%. Tijd genomen: {eind_tijd - start_tijd:.2f} seconden.")
    else:
        print("Ongeldige keuze. Probeer het opnieuw.")
    print("\nKies een type som om te oefenen:")
    print("1. Bereken het percentage van een getal")
    print("2. Bereken het getal als je het percentage weet")
    print("3. Bereken het percentage tussen twee getallen")
    print("4. Bereken het getal na een procent toename of afname")
    print("5. bereken de procent toename of afname tussen twee getallen")
    print("6. Afsluiten")
    keuze = input("Voer het nummer van je keuze in (1-6): ")
print("Bedankt voor het gebruiken van de procenten trainer!")
