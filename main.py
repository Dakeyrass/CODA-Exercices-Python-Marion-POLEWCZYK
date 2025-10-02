# Exemple avec un seul exercice
def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    prénom = input("Quel est ton prénom?")
    print("Bonjour " + prénom)

def main():
# Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix == "2":
        exercice2()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()
