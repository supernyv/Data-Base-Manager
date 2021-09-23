import os, json

def consulter(nom, prenom):
    filename = os.path.join('data', 'all_data.json')
    found = False

    with open(filename, 'r') as d:
        infos = json.load(d)
    print()
    for a_dict in infos:
        if nom and prenom in list(a_dict.values()):
            found = True
            for a, b in a_dict.items():
                if type(b) == dict:
                    print('\t'*2, '*'*4, a, '*'*4)
                    for x, y in b.items():
                        print('\t'*2, f"{x} : {y}")
                else:
                    print(f"{a} : {b}")
    if found == False:
        print(f"Le nom {nom} {prenom} n'existe pas dans la base de données.\n")
