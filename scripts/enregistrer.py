import os, json

def enregistrer(all):
    if all:
        filename = os.path.join('data', 'all_data.json')
        with open(filename) as lire:
            fichier = json.load(lire)
        fichier.append(all)

        with open(filename, 'w') as d:
            json.dump(fichier, d, indent=4)
        print()
        print('=-'*13)
        print("Informations sauvegardées.")
        print('=-'*13)
        print()
    else:
        return None

def infos():
    keys = ["Date Enregistrement", "Nom", "Prenom", "Age", "Sexe", "District", "Fiche Judiciaire"]
    fiche = ["Motif Interpellation Recente", "Nombre Emprisonnements", "Personnalité", 
    "Substance Addictive"]
    donnée = {}
    print("Pour confirmer, repondre 'O' pour 'Oui' et 'N' pour 'Non'.\n")
    for k in keys:
        if k == "Fiche Judiciaire":
            print('\t'*2, '*'*4, k, '*'*4)
            sample = {}
            for d in fiche:
                ans = input(f"\t{d}: ").title()
                while True:
                    if ans:
                        quest= input(f'Confirmer {d}?: ').upper()
                        if quest == 'N':
                            ans = input(f"{d}: ").title()
                        elif quest == 'O':
                            break
                        else:
                            print("Oui a été choisit par defaut")
                            break
                    else:
                        print(f"\tVous devez entrer {d}")
                        ans = input(f"\t{d}: ").title()
                sample[d] = ans
            donnée[k] = sample
            
        else:
            n = input(f"{k}: ").title()
            while True:
                if n:
                    question = input(f'Confirmez-vous {n} comme {k}?: ').upper()
                    if question == 'N':
                        n = input(f"{k}: ").title()
                    elif question == 'O':
                        break
                    else:
                        print("Oui a été choisit par defaut")
                        break
                else:
                    print(f"Vous devez entrer {k}.")
                    n = input(f"{k}: ").title()
            donnée[k] = n
    filename = os.path.join('data', 'all_data.json')

    with open(filename) as data:
        all_infos = json.load(data)

    count = 0

    for question, answer in donnée.items():
        for dictionary in all_infos:
            if question == 'Nom':
                if answer in list(dictionary.values()):
                    count += 1
            if question == 'Prenom':
                if answer in list(dictionary.values()):
                    count += 1
            if question == 'Age':
                if answer in list(dictionary.values()):
                    count += 1
    if count >= 3:
        print()
        print('¤'*58)
        print(f"Données rejetés.  Deja existants dans la base de données.")
        print('¤'*58)
        print()
        return None
    else:
        return donnée
