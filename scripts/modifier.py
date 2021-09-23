import os, json

def retirer():
    filename = os.path.join('data', 'all_data.json')
    with open(filename) as lire:
        fichier = json.load(lire)

    return fichier

def modifier():
    fichier = retirer()

    if fichier:
        list_infos = [x for x in list(fichier[0].keys())]
        print('='*50)
        nom = input("Entrer le nom du concerné: ").title()
        prenom = input('Entrer le prenom du concerné: ').title()
        
        all_values = []

        for a_dictionary in fichier:
            for val in a_dictionary.values():
                if type(val) != dict:
                    all_values.append(val)

        if nom and prenom in all_values:
            print('-'*50)
            print(f"\nVeuillez Entrer le nom de l'information que vous souhaitez modifier pour {prenom} {nom} tel que specifié.")
            print('~'*115)
            print("Liste des informations:", end=' ')
            print(*list_infos, sep=' | ')
            print('~'*115)

            information = input('Information à modifier: ').title()

            for personne_folder in fichier:
                for key, info_old in personne_folder.items():
                    if key == "Fiche Judiciaire":
                        if information == key:
                            sub_infos = [y for y in list(info_old.keys())]
                            print(':'*115)
                            print('Details: ', end='')
                            print(*sub_infos, sep=' | ')
                            print(':'*115)
                            branche = input(f'Detail de {key} à changer: ').title()
                            for a, b_old in info_old.items():
                                if a == branche:
                                    b_new = input(f'Entrez nouveau {a}: ')
                                    print("Entrez 'O' pour confirmer et 'N' pour annuler.")
                                    que = input(f"Vous allez changer {a} de {b_old} à {b_new}: ").upper()

                                    while True:
                                        if que == 'O':
                                            break
                                        elif que == 'N':
                                            b_new = ""
                                            break
                                        else:
                                            print("Choix non specifié.")
                                    if b_new:
                                        info_old[a] = b_new

                    else:
                        if information == key:
                            info_new = input(f'Entrez nouveau {key}: ')
                            print("Entrez 'O' pour confirmer et 'N' pour annuler.")
                            while True:
                                quest = input(f"Vous allez changer l'information {key} de {info_old} à {info_new}: ").upper()
                                if quest == 'O':
                                    break
                                elif quest == 'N':
                                    info_new = ""
                                    break
                                else:
                                    print("Choix non specifié. Reprendre.")
                            if info_new:
                                personne_folder[key] = info_new
            return fichier
        else:
            print(f"\n{prenom} {nom} n'existe pas dans la base de données.")
            return None

    else:
        print('Rien à modifier.\n')
        return None

def renouveler(fichier):
    if fichier:
        filename = os.path.join('data', 'all_data.json')
        with open(filename, 'w') as d:
            json.dump(fichier, d, indent=4)
        print("Informations sauvegardées.\n")
    else:
        pass
