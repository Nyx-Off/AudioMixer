# AudioMixer

AudioMixer est un script Python qui ajoute automatiquement une musique de fond à tous les fichiers `.mp3` présents dans le répertoire d'exécution. Chaque fichier `.mp3` traité est placé dans un dossier portant le même nom que le fichier d'origine, accompagné du fichier résultant avec la musique de fond ajoutée.

## Fonctionnalités

- Ajoute une musique de fond à tous les fichiers `.mp3` dans le répertoire d'exécution.
- Crée un dossier pour chaque fichier `.mp3` d'origine avec le fichier traité et le fichier résultant.
- Ajuste le volume de la voix et de la musique.
- Télécharge et installe automatiquement FFmpeg si nécessaire.
- Installe automatiquement les dépendances Python requises (`pydub`, `requests`).

## Prérequis

- Python 3.x
- pip (gestionnaire de paquets pour Python)

## Installation

1. Clonez le dépôt GitHub :
    ```sh
    git clone https://github.com/votre-utilisateur/AudioMixer.git
    cd AudioMixer
    ```

2. Exécutez le script Python :
    ```sh
    python start.py
    ```

Le script vérifiera et installera automatiquement les dépendances nécessaires.

## Utilisation

1. Placez vos fichiers `.mp3` dans le même répertoire que le script `start.py`.
2. Placez votre fichier musical de fond (`Musique.mp3`) dans le même répertoire que le script.
3. Modifiez les paramètres de volume dans le script `start.py` si nécessaire :
    ```python
    texte_volume = 0  # Ajustez le volume du texte ici (en dB)
    musique_volume = 2  # Ajustez le volume de la musique ici (en dB)
    ```

4. Exécutez le script :
    ```sh
    python start.py
    ```

Les fichiers audio générés seront placés dans des dossiers portant le même nom que les fichiers `.mp3` d'origine.

## Contribuer

Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour discuter des modifications que vous souhaitez apporter.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Auteurs

- [Nyx-Off](https://github.com/Nyx-Off)

---

**Note :** Assurez-vous d'avoir une connexion Internet active lors de la première exécution du script pour permettre le téléchargement des dépendances et de FFmpeg.
