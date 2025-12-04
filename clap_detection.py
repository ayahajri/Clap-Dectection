import sounddevice as sd
import numpy as np
from collections import deque
import time
from playsound import playsound
import subprocess
import os
import threading

# ===== CONFIG =====
FS = 44100
BLOCKSIZE = 1024
CLAP_THRESHOLD = 0.08
CLAP_DELAY = 0.5
COOLDOWN = 5

AUDIO_FILE = r"C:\Projets\Clap detection\Welcome back Jarvis.mp3"
VSCODE_PATH = r"C:\Users\aya-hajri\AppData\Local\Programs\Microsoft VS Code\Code.exe"

clap_times = deque(maxlen=2)
last_trigger = 0
vscode_opened = False
prev_rms = 0

def play_audio():
    playsound(AUDIO_FILE)

def audio_callback(indata, frames, time_info, status):
    global clap_times, last_trigger, vscode_opened, prev_rms

    rms = np.sqrt(np.mean(indata**2))
    diff = rms - prev_rms
    prev_rms = rms

    if diff < CLAP_THRESHOLD:
        return

    clap_times.append(time.time())

    if len(clap_times) == 2:
        delta = clap_times[1] - clap_times[0]
        if delta < CLAP_DELAY and (time.time() - last_trigger) > COOLDOWN:
            print("Double clap détecté ! 🎉")
            
            # Ouvrir VSCode immédiatement
            if not vscode_opened and os.path.exists(VSCODE_PATH):
                subprocess.Popen([VSCODE_PATH])
                vscode_opened = True
            
            # Jouer l’audio dans un thread séparé pour ne pas bloquer
            threading.Thread(target=play_audio).start()
            
            last_trigger = time.time()
        clap_times.clear()

print("En attente du double-clap…")
with sd.InputStream(callback=audio_callback, channels=1, samplerate=FS, blocksize=BLOCKSIZE):
    while True:
        time.sleep(0.1)
