# Fonctions de demo pour l'utilsiation de cProfile
# lancer avec python3 -m cProfile -o resultats.prof demo_profile.py
# puis uv run snakeviz resultats.prof pour l'afficher dans votre navigateur
# si vous le lancez sans uv, pensez à activer votre environnement virtuel avec source venv/bin/activate puis snakeviz resultats.prof

import time

def tache_lente():
    total = 0
    for i in range(10_000_000):
        total += i ** 2
    return total

def tache_rapide():
    time.sleep(0.1)
    return "ok"

def main():
    for _ in range(3):
        tache_lente()
        tache_rapide()

if __name__ == "__main__":
    main()