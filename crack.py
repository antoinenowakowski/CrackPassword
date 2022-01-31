import random

VotrePassword = input("Votre mot de passe : ")

liste = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
         "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
         "-", "_", ";", ",", ".", "!", "*", "{", "(", "`", "'", ")", "}",
         0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def ChoisitAletoirementUnCaractere():
    Caracteres = random.choice(liste)
    return Caracteres


def GenerePassword():
    for NombreDeCaracteres in range(1, 10):
        EstDifferentsDuNombreChoisit = 0
        PasswordEnListe = []
        while EstDifferentsDuNombreChoisit != NombreDeCaracteres:
            Password = ChoisitAletoirementUnCaractere()
            PasswordEnListe.append(Password)
            EstDifferentsDuNombreChoisit += 1

        FinalPassword = "".join(map(str, PasswordEnListe))
        print(FinalPassword)
        NombreDeCaracteres+=1
        if FinalPassword == VotrePassword:
            print(f"Votre mot de passe est {FinalPassword}")
            return FinalPassword
        else:
            continue

while GenerePassword() != VotrePassword:
    GenerePassword()