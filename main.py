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
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()
