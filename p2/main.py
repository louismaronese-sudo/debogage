# Ouvrir un fichier csv et le lire
import os

# Trouve le dossier exact où se trouve ce fichier main.py, peu importe d'où on le lance
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "fichier.csv")

print(current_dir , "\n saut de ligne \n", file_path)
