#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Serveur local pour l'app d'échecs.
Relie l'échiquier (dans le navigateur) au moteur Stockfish installé sur ce PC.

Lancement :
    python3 serveur_echecs.py

Puis ouvre dans ton navigateur :  http://localhost:8000
"""

import http.server
import socketserver
import subprocess
import json
import os
import sys
import urllib.parse
import threading

PORT = 8000
HTML_FILE = "Papu_Chess.html"

# --- Détection de Stockfish ---
def trouver_stockfish():
    for chemin in ["/usr/games/stockfish", "/usr/bin/stockfish", "/usr/local/bin/stockfish", "stockfish"]:
        try:
            p = subprocess.Popen([chemin], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
            p.stdin.write("quit\n"); p.stdin.flush(); p.wait(timeout=2)
            return chemin
        except Exception:
            continue
    return None

STOCKFISH = trouver_stockfish()

# --- Un moteur Stockfish persistant, protégé par un verrou ---
_lock = threading.Lock()
_engine = None

def demarrer_moteur():
    global _engine
    if STOCKFISH is None:
        return None
    _engine = subprocess.Popen([STOCKFISH], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.DEVNULL, text=True, bufsize=1)
    _envoyer("uci"); _attendre("uciok")
    _envoyer("isready"); _attendre("readyok")
    return _engine

def _envoyer(cmd):
    _engine.stdin.write(cmd + "\n"); _engine.stdin.flush()

def _attendre(mot):
    while True:
        ligne = _engine.stdout.readline()
        if not ligne:
            return None
        if mot in ligne:
            return ligne

def coup_adversaire(fen, elo=1320, mouvement_temps=0.3):
    """Fait jouer Stockfish à une force Elo donnée (mode 'jouer contre'). Renvoie un coup UCI."""
    with _lock:
        if _engine is None:
            return None
        # activer la limitation de force
        _envoyer("setoption name UCI_LimitStrength value true")
        _envoyer("setoption name UCI_Elo value " + str(int(elo)))
        _envoyer("position fen " + fen)
        _envoyer("go movetime " + str(int(mouvement_temps * 1000)))
        coup = None
        while True:
            ligne = _engine.stdout.readline()
            if not ligne:
                break
            if ligne.startswith("bestmove"):
                parts = ligne.split()
                coup = parts[1] if len(parts) >= 2 and parts[1] != "(none)" else None
                break
        # remettre la pleine force pour les analyses suivantes
        _envoyer("setoption name UCI_LimitStrength value false")
        return coup

def meilleur_coup(fen, profondeur=14):
    """Renvoie (coup_uci, score_cp, mat) pour une position FEN.
    score_cp = évaluation en centipions du point de vue du camp au trait.
    mat = nombre de coups avant mat (positif = le camp au trait mate), ou None."""
    with _lock:
        if _engine is None:
            return None, None, None
        _envoyer("position fen " + fen)
        _envoyer("go depth " + str(profondeur))
        score_cp = None
        mat = None
        while True:
            ligne = _engine.stdout.readline()
            if not ligne:
                return None, score_cp, mat
            if ligne.startswith("info") and " score " in ligne:
                parts = ligne.split()
                try:
                    idx = parts.index("score")
                    kind = parts[idx + 1]
                    val = int(parts[idx + 2])
                    if kind == "cp":
                        score_cp = val; mat = None
                    elif kind == "mate":
                        mat = val; score_cp = None
                except (ValueError, IndexError):
                    pass
            if ligne.startswith("bestmove"):
                parts = ligne.split()
                coup = parts[1] if len(parts) >= 2 and parts[1] != "(none)" else None
                return coup, score_cp, mat

# --- Serveur HTTP ---
class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass  # silencieux

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)

        if parsed.path == "/ping":
            self._json({"ok": True, "moteur": STOCKFISH or "absent"})
            return

        if parsed.path == "/bestmove":
            params = urllib.parse.parse_qs(parsed.query)
            fen = params.get("fen", [None])[0]
            prof = params.get("depth", ["14"])[0]
            try: prof = max(4, min(20, int(prof)))
            except: prof = 14
            if not fen:
                self._json({"bestmove": None}); return
            coup, score_cp, mat = meilleur_coup(fen, prof)
            self._json({"bestmove": coup, "cp": score_cp, "mate": mat})
            return

        if parsed.path == "/play":
            params = urllib.parse.parse_qs(parsed.query)
            fen = params.get("fen", [None])[0]
            elo = params.get("elo", ["1320"])[0]
            try: elo = max(1320, min(3190, int(elo)))
            except: elo = 1320
            if not fen:
                self._json({"move": None}); return
            coup = coup_adversaire(fen, elo)
            self._json({"move": coup})
            return

        if parsed.path == "/" or parsed.path == "":
            self.path = "/" + HTML_FILE
        return super().do_GET()

    def _json(self, obj):
        data = json.dumps(obj).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def main():
    print("=" * 50)
    print("  Serveur d'échecs local")
    print("=" * 50)
    if STOCKFISH is None:
        print("\n⚠️  Stockfish introuvable !")
        print("   Installe-le avec :  sudo apt install stockfish")
        print("   L'app fonctionnera quand même, mais sans les flèches du moteur.\n")
    else:
        print(f"\n✓ Stockfish trouvé : {STOCKFISH}")
        demarrer_moteur()
        print("✓ Moteur démarré et prêt")

    if not os.path.exists(HTML_FILE):
        print(f"\n⚠️  Le fichier '{HTML_FILE}' est introuvable dans ce dossier.")
        print("   Place 'serveur_echecs.py' et 'echecs_local.html' dans le MÊME dossier.\n")
        sys.exit(1)

    print(f"\n➜  Ouvre ton navigateur sur :  http://localhost:{PORT}\n")
    print("   (Pour arrêter le serveur : Ctrl+C)\n")

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServeur arrêté. À bientôt !")


if __name__ == "__main__":
    main()
