import os
import subprocess
import sys
import requests
import zipfile

FFMPEG_URL = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
FFMPEG_DIR = "ffmpeg"

# Fonction pour installer les dépendances
def installer_dependances():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pydub", "requests"])

# Installer les dépendances au début du script
installer_dependances()

# Maintenant, importer les modules après avoir installé les dépendances
from pydub import AudioSegment

def verifier_ffmpeg():
    try:
        subprocess.run(['ffmpeg', '-version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("FFmpeg est déjà installé.")
    except (subprocess.CalledProcessError, FileNotFoundError):
        chemin_ffmpeg = trouver_ffmpeg()
        if chemin_ffmpeg:
            print("FFmpeg est déjà téléchargé mais n'est pas trouvé dans PATH. Ajout à PATH.")
            ajouter_au_path(chemin_ffmpeg)
        else:
            print("FFmpeg n'est pas installé. Téléchargement en cours...")
            telecharger_ffmpeg()

def trouver_ffmpeg():
    for root, dirs, files in os.walk(FFMPEG_DIR):
        if 'ffmpeg.exe' in files:
            return root
    return None

def telecharger_ffmpeg():
    local_zip = "ffmpeg.zip"
    with requests.get(FFMPEG_URL, stream=True) as r:
        r.raise_for_status()
        with open(local_zip, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print("Téléchargement de FFmpeg terminé. Décompression en cours...")
    with zipfile.ZipFile(local_zip, 'r') as zip_ref:
        zip_ref.extractall(FFMPEG_DIR)
    os.remove(local_zip)
    chemin_ffmpeg = trouver_ffmpeg()
    if chemin_ffmpeg:
        ajouter_au_path(chemin_ffmpeg)
        print("FFmpeg a été installé et configuré.")
    else:
        print("Erreur : FFmpeg n'a pas pu être trouvé après le téléchargement.")

def ajouter_au_path(chemin):
    os.environ["PATH"] += os.pathsep + chemin
    print(f"Le chemin {chemin} a été ajouté au PATH.")
    with open("add_to_path.bat", "w") as bat_file:
        bat_file.write(f'setx PATH "%PATH%;{chemin}"\n')
    subprocess.run("add_to_path.bat", shell=True)
    os.remove("add_to_path.bat")

def ajouter_musique(son_texte, musique_chemin, sortie_finale, texte_volume=0, musique_volume=0):
    musique = AudioSegment.from_file(musique_chemin)
    duree_cible = len(son_texte) + 3000  # en millisecondes
    son_texte = son_texte + texte_volume
    musique = musique + musique_volume
    musique = musique[:duree_cible]
    mix = musique.overlay(son_texte)
    mix.export(sortie_finale, format='mp3')

def traiter_fichier(fichier_mp3, fichier_musique, texte_volume=0, musique_volume=0):
    nom_fichier_mp3 = os.path.basename(fichier_mp3)
    nom_base = os.path.splitext(nom_fichier_mp3)[0]
    dossier_sortie = os.path.join(".", nom_base)
    os.makedirs(dossier_sortie, exist_ok=True)
    
    son = AudioSegment.from_file(fichier_mp3)
    fichier_sortie = os.path.join(dossier_sortie, f"{nom_base}_final.mp3")
    ajouter_musique(son, fichier_musique, fichier_sortie, texte_volume, musique_volume)
    
    # Copie du fichier d'origine dans le dossier de sortie
    fichier_original_sortie = os.path.join(dossier_sortie, nom_fichier_mp3)
    os.rename(fichier_mp3, fichier_original_sortie)
    
    print(f"Fichier audio final généré : {fichier_sortie}")

def main():
    verifier_ffmpeg()
    repertoire_racine = "."  # Spécifiez le répertoire racine
    fichier_musique = "Musique.mp3"  # Fichier de musique de fond
    
    fichiers_mp3 = [f for f in os.listdir(repertoire_racine) if f.endswith('.mp3') and f != fichier_musique]
    
    texte_volume = 0  # Ajustez le volume du texte ici
    musique_volume = 2  # Ajustez le volume de la musique ici
    
    for fichier_mp3 in fichiers_mp3:
        chemin_fichier_mp3 = os.path.join(repertoire_racine, fichier_mp3)
        traiter_fichier(chemin_fichier_mp3, fichier_musique, texte_volume, musique_volume)

if __name__ == "__main__":
    main()
