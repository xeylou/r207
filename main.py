#!/usr/bin/python3

### init ###

liste_etudiants = [] #  (nom, prénom, age, liste des notes)


# q1
def creerEtudiant(nom, prenom, age):
    identité_etudiant = (nom, prenom, age, [])
    return identité_etudiant

def enregistrerNote(étudiant,note):
    # l'étudiant n'a aucune note, on crée la liste
    tmp = []
    tmp.append(note)

    tmp2 = (étudiant[0], étudiant[1], étudiant[2], tmp)

    # for etud in liste_etudiants:
    #     if etud == étudiant:
    #         etud[3] = [note]
    return tmp2

def afficherEtudiant(Etudiant):
    # je considère Etudiant suit la forme (nom, prénom, age, liste des notes)
    nom = Etudiant[0]
    prenom = Etudiant[1]
    age = str(Etudiant[2])
    notes = str(Etudiant[3])

    return("L'étudiant s'appelle " + nom + " " + prenom + " et a " + age + " ans. Voici ses notes : " + notes)

    # for etud in liste_etudiants:
    #     if Etudiant == etud:
    #         return("L'étudiant s'appelle" etud[0], etud[1], "et a", etud[2], ".\n\nVoici ses notes:", etud[3])

def nbNotes(Etudiant):
    # je considère Etudiant suit la forme (nom, prénom, age, liste des notes)
    
    # for etud in liste_etudiants:
    #     if Etudiant == etud:
    #         for notes in range(len())
    tmp = str(len(Etudiant))
    return("L'étudiant a " + tmp + " notes.")

def calculerMoyenneE(Etudiant):
    somme = Etudiant[3][0]
    tmp = Etudiant[3]
    if tmp == []:
        return(0)
    for note in range(1, len(tmp)):
        somme += tmp[note]
    moyenne = str(int(somme/len(tmp)))
    return("La moyenne des notes de l'étudiant est de " + moyenne)


prom1 = []

def inscrire(Promotion,Etudiant):
    Promotion.append(Etudiant)
    return Promotion

def nbEtudiants(Promotion):
    return("Il y a " + str(len(Promotion)) + " étudiants dans la promotion")

def calculerMoyenne(Promotion):
    moy_générale = 0
    for etud in Promotion:
        moy_etud = calculerMoyenne(etud)
        moy_générale += moy_etud
    return moy_etud / len(Promotion)



### debug ###

prom1 = []

def debugging():
    etud1 = ("Nom1", "Prenom1", 1, [1,2,3])
    etud2 = ("Nom2", "Prenom2", 2, [4,5,6])
    etud3 = ("Nom3", "Prenom3", 3, [7,8,9])

    prom1.append(etud1)
    prom1.append(etud2)
    prom1.append(etud3)

    assert creerEtudiant("Nom4", "Prenom4", 4) == ("Nom4", "Prenom4", 4, [])
    print('\033[32m' + "✓ Test 1 passé")

    assert enregistrerNote(("Nom4", "Prenom4", 4), 10) == ('Nom4', 'Prenom4', 4, [10])
    print('\033[32m' + "✓ Test 2 passé")

    assert afficherEtudiant(("Nom4", "Prenom4", 4, [10])) == "L'étudiant s'appelle Nom4 Prenom4 et a 4 ans. Voici ses notes : [10]"
    print('\033[32m' + "✓ Test 3 passé")

    assert nbNotes(("Nom4", "Prenom4", 4, [10])) == "L'étudiant a 4 notes."
    print('\033[32m' + "✓ Test 4 passé")

    assert calculerMoyenneE(("Nom4", "Prenom4", 4, [10])) == "La moyenne des notes de l'étudiant est de 10"
    print('\033[32m' + "✓ Test 5 passé")

    assert inscrire(prom1,("Nom4", "Prenom4", 4, [])) == [("Nom1", "Prenom1", 1, [1,2,3]), ("Nom2", "Prenom2", 2, [4,5,6]), ("Nom3", "Prenom3", 3, [7,8,9]), ("Nom4", "Prenom4", 4, [])]
    print('\033[32m' + "✓ Test 6 passé")

    assert nbEtudiants(prom1) == "Il y a 4 étudiants dans la promotion"
    print('\033[32m' + "✓ Test 7 passé")


 


# etud1 = ("Nom1", "Prenom1", 1, [1,2,3])
# print(afficherEtudiant(etud1))

# print(nbNotes(("Nom4", "Prenom4", 4, [10])))

# print(calculerMoyenneE(("Nom4", "Prenom4", 4, [10])))
print(debugging())
# print(nbEtudiants(prom1))
# print('\x1b[6;30;42m' + 'Succès!' + '\x1b[0m')
# print(enregistrerNote(("Nom4", "Prenom4", 4), 10))
print('\x1b[6;30;42m' + 'Succès!' + '\x1b[0m')
