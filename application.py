"""Base de données pour tous les informations concernant les cas de police"""
import scripts.consulter as consulter
import scripts.enregistrer as enregistrer
import scripts.modifier as modifier
import scripts.analyser as analyser

print()
print("| Republique du Congo |".center(115), '\n')
print("Base de Données, Police Nationale", "Zone Owando".rjust(80))
print('*'*115, '\n')

def welcome():
    print("Entez 'C' pour consulter, 'E' pour enregistrer un nouveau cas, 'M' pour modifier, ou 'Q' pour quitter le programme.")
    print("Pour voir le nombre total de cas enregistrés, entrez 'T'.")
    print('-'*115)
    answer = input('Reponse: ').upper()
    return answer.upper()

n = welcome()
while True:
    if n == 'Q':
        print('Programme Terminé.')
        break
    elif n == 'C':
        print('Consultation de la base de données.'.center(115))
        print('\t'*4, '-'*50)
        nom= input("Entrer le nom du concerné: ").title()
        prenom = input("Entrer le Prénom du Concerné: ").title()
        consulter.consulter(nom, prenom)
        print('-'*115)
        n = welcome()
    elif n == 'E':
        print('Enregistrement de nouvelles données'.center(115))
        print('\t'*4, '-'*50)
        information = enregistrer.infos()
        enregistrer.enregistrer(information)
        print('-'*115)
        n = welcome()
    elif n == 'M':
        print('Modification de données'.center(115))
        print('\t'*4, '-'*50)
        nouveau = modifier.modifier()
        modifier.renouveler(nouveau)
        print('-'*115)
        n = welcome()
    elif n == 'T':
        noms, nombre = analyser.retirer()
        print()
        print('~-'*16)
        print('Nombre total de cas enregistrés: ', nombre)
        print('~-'*16)
        print()
        print('-'*115)
        n = welcome()
    else:
        print('Non determiné. Veuillez reprendre.'.center(115))
        print('-'*115)
        n = welcome()