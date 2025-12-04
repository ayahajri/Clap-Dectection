# 🎤 Clap Detection — Double Clap Trigger

Ce projet permet de détecter un **double clap en temps réel** via le micro, puis d'exécuter automatiquement :

- 🔊 Lecture du son *"Welcome back Jarvis"*
- 💻 Ouverture automatique de Visual Studio Code

---

## 🚀 Fonctionnalités

- 🎧 Analyse audio en temps réel via le micro
- 👏 Détection intelligente d’un **double clap**
- ⚡ Basé sur la variation RMS + seuil dynamique
- ⏱️ Système de cooldown pour éviter les déclenchements multiples
- 🔊 Lecture audio dans un thread séparé
- 🖥️ Ouverture automatique de VS Code
- 📦 Configuration simple et modifiable

---

## 📦 Installation

### 1️⃣ Installer les dépendances Python

```bash
pip install sounddevice numpy playsound
```

> ⚠ Sous Windows : si erreur PortAudio → installer depuis ici :  
> https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

---

## 📁 Structure du Projet

```
Clap Detection/
│── clap_detection.py
│── start_clap_detection.bat
│── Welcome back Jarvis.mp3
└── README.md
```

---

## ⚙️ Configuration

Modifie les chemins selon ton PC :

```python
AUDIO_FILE = r"C:\Projets\Clap detection\Welcome back Jarvis.mp3"
VSCODE_PATH = r"C:\Users\aya-hajri\AppData\Local\Programs\Microsoft VS Code\Code.exe"
```

Paramètres de détection :

```python
FS = 44100            # Sampling rate
BLOCKSIZE = 1024      # Taille d’un bloc audio
CLAP_THRESHOLD = 0.08 # Sensibilité
CLAP_DELAY = 0.5      # Max delay entre deux claps
COOLDOWN = 5          # Temps avant nouveau déclenchement
```

---

## ▶️ Lancer le Programme

### Option A — Depuis Python :

```bash
python clap_detection.py
```

### Option B — Avec le script Windows :

Double-cliquer sur :

```
start_clap_detection.bat
```

---

## 🤖 Fonctionnement (Résumé Technique)

1. Lit le micro en flux continu (44100 Hz)  
2. Calcule le **RMS** de chaque bloc audio  
3. Détecte un clap si l’augmentation dépasse `CLAP_THRESHOLD`  
4. Stocke les timestamps  
5. Si deux claps < `CLAP_DELAY` → **double clap détecté**  
6. Le programme :
   - 🔊 Joue le son Jarvis  
   - 💻 Ouvre VS Code  
   - ⏳ Démarre un délai `COOLDOWN`  

---

## 📌 Exemple Console

```
En attente du double-clap…
Double clap détecté ! 🎉
```

---

## 🛠️ Améliorations futures

- Auto-réglage de la sensibilité
- Détection de patterns (triple clap, séquences)
- Dashboard + interface graphique
- Support MacOS et Linux

---

## 🧑‍💻 Auteur

Développé par **Aya Hajri**.

---

## ⭐ Support

N’hésite pas à mettre une ⭐ sur GitHub si ce projet t'a plu !
