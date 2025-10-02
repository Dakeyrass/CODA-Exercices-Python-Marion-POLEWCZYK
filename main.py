# Exemple avec un seul exercice
def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    name = input("Quel est ton prénom?")
    print("Bonjour " + name)

def exercice3():
    print("Première ligne \nDeuxième ligne \nTroisième ligne")

def exercice4():
    birthday_year = int(input("Quelle est ton année de naissance"))
    current_year = int(input("En quelle année sommes-nous?"))
    age = current_year - birthday_year
    print(f"Tu dois avoir approximativement {age} ans.")

def exercice5():
    first_nbr = int(input("Entrer un premier nombre"))
    second_nbr = int(input("Entrer un second nombre."))
    addition = first_nbr + second_nbr
    print(f"Le résultat est de {addition}.")

def exercice6():
    first_nbr = int(input("Entrer un premier nombre"))
    second_nbr = int(input("Entrer un second nombre."))
    soustraction = first_nbr - second_nbr
    print(f"Le résultat est de {soustraction}.")

def exercice7():
    first_nbr = int(input("Entrer un premier nombre"))
    second_nbr = int(input("Entrer un second nombre."))
    multiplication = first_nbr*second_nbr
    print(f"Le résultat est de {multiplication}.")

def exercice8():
    first_nbr = int(input("Entrer un premier nombre"))
    second_nbr = int(input("Entrer un second nombre."))
    division = first_nbr/second_nbr
    print(f"Le résultat est de {division}.")

def exercice9():
    nbr = int(input("Entrer un nombre"))
    carré = nbr*nbr
    print(f"Le carré de {nbr} est de {carré}.")

def exercice10():
    nbr = int(input("Entrer un nombre"))
    double = nbr*2
    print(f"Le double de {nbr} est de {double}.")

def exercice11():
    nbr = int(input("Entrer un nombre"))
    moitié = nbr/2
    print(f"La moitié de {nbr} est de {moitié}.")

def exercice13():
    i = 0
    for i in range(6):
        print(i)
        i += 1

def exercice12():
    i = 0
    for i in range(5):
        print("feur")
        i += 1 

def exercice14():
    i = 0
    for i in range(5):
        multiplication = 2*i+1
        print(f"2 x {i+1} = {multiplication}")

def exercice15():
    cote = int(input("De quelle longueur est le côté du carré?"))
    perimetre = cote*4
    print(f"Le périmètre du carré est de {perimetre} cm.")

def exercice16():
    cote = int(input("De quelle longueur est le côté du carré?"))
    aire = cote*cote
    print(f"L'aire du carré est de {aire} cm.")

def exercice17():
    euro = int(input("Combien d'euros voulez-vous convertir?"))
    conversion = euro*1.1
    print(f"Vos {euro} euros valent {conversion} dollars.")

def exercice19():
    prix = int(input("Quel est le prix de l'article?"))
    prix_tva = prix*1.2
    print(f"Le prix avec TVA est désormais de {prix_tva}. ")

def exercice18():
    minute = int(input("Combien de minutes ?"))
    conversion_seconde = minute*60
    print(f"{minute} minutes vaut {conversion_seconde} secondes.")

def exercice20():
    age = int(input("Quel est votre age?"))
    nom = input("Quel est ton nom?")
    print(f"Je sais que ton nom est {nom} et que tu as {age} ans.")

def main():
# Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix == "2":
        exercice2()
    elif choix == "3":
        exercice3()
    elif choix == "4":
        exercice4()
    elif choix == "5":
        exercice5()
    elif choix == "6":
        exercice6()
    elif choix == "7":
        exercice7()
    elif choix == "8":
        exercice8()
    elif choix == "9":
        exercice9()
    elif choix == "10":
        exercice10()
    elif choix == "11":
        exercice11()
    elif choix == "12":
        exercice12()
    elif choix == "13":
        exercice13()
    elif choix == "14":
        exercice14()
    elif choix == "15":
        exercice15()
    elif choix == "16":
        exercice16()
    elif choix == "17":
        exercice17()
    elif choix == "18":
        exercice18()
    elif choix == "19":
        exercice19()
    elif choix == "20":
        exercice20()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()
