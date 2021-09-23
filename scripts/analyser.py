import os, json

def retirer():
    filename = filename = os.path.join('data', 'all_data.json')
    full_names = []

    with open(filename) as f:
        retrieved = json.load(f)
    
    for document in retrieved:
        full_names.append([document['Nom'], document['Prenom']])
    return full_names, len(full_names)