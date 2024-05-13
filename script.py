import schedule
import time
import os
from git import Repo

# Fonction pour effectuer le push sur GitHub
def git_push():
    # Chemin vers le répertoire de votre projet
    repo_path = 'C:/Users/tanguy.pagee/Bureau/Bot/DailyPushBot'

    # Changez de répertoire vers le dépôt Git
    os.chdir(repo_path)

    # Initialisez l'objet Repo
    repo = Repo(repo_path)

    # Ajoutez tous les fichiers modifiés pour l'index
    repo.git.add('--all')

    # Commit avec un message
    repo.git.commit('-m', 'Automated daily push')

    # Poussez les modifications vers le dépôt distant
    repo.git.push()

# Fonction pour afficher et modifier une variable
def changer_variable():
    global ma_variable  # Indique que nous utilisons la variable globale ma_variable
    print("Valeur actuelle de ma_variable:", ma_variable)
    ma_variable += 1  # Incrémente la variable
    with open('fichier.txt', 'a') as f:
        f.write('a\n')  # Ajoute une ligne avec un 'a' à chaque fois que la fonction est appelée
    git_push()  # Appel de la fonction pour effectuer le push sur Git à chaque changement de la variable

# Initialisez la variable
ma_variable = 0

# Planifiez l'exécution de la fonction changer_variable() chaque seconde
schedule.every(0.001).seconds.do(changer_variable)

# Boucle d'exécution infinie
while True:
    schedule.run_pending()
    time.sleep(1)  # Attendez 1 seconde avant de vérifier à nouveau le planning
    
#TestTestTest
