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

# Planifiez l'exécution de la fonction git_push() à l'heure spécifiée chaque jour
schedule.every().day.at("16:17").do(git_push)
schedule.every().day.at("16:18").do(git_push)

# Boucle d'exécution infinie
while True:
    schedule.run_pending()
    time.sleep(1)  # Attendez 1 seconde avant de vérifier à nouveau le planning
