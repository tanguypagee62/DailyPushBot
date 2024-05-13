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

# Planifiez l'exécution de la fonction git_push() à minuit chaque jour
schedule.every().day.at("16:09").do(git_push)
schedule.every().day.at("16:10").do(git_push)
schedule.every().day.at("16:11").do(git_push)
schedule.every().day.at("16:12").do(git_push)
schedule.every().day.at("16:13").do(git_push)
schedule.every().day.at("16:14").do(git_push)
schedule.every().day.at("16:15").do(git_push)
schedule.every().day.at("16:16").do(git_push)
schedule.every().day.at("16:17").do(git_push)

# Boucle d'exécution
while True:
    schedule.run_pending()
    time.sleep(5)  # Attendez 60 secondes avant de vérifier à nouveau le planning
