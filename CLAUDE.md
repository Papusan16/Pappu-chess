# Papu Chess

Application d'échecs **mono-fichier HTML autonome**, sans build ni
dépendance : `Papu_Chess.html` s'ouvre tel quel. Le **fonds pédagogique**
(`_fonds/`) est de la **donnée** séparée du code — encyclopédie, PGN.

## Au démarrage — ordre de lecture

1. Lire `REPRISE.md` **avant toute autre réponse**. Il désigne la suite :
   `_fonds/RESTE_A_FAIRE.md` (plan de route), `PRINCIPES.md` (règles), et
   le dernier fichier de `_sessions/` (contexte frais).
2. Puis **confronter cette lecture à l'état git réel** : `git fetch`, et
   des comparaisons **dans les deux sens** (avance *et* retard) entre la
   branche de travail et `origin/main`. Les fichiers décrivent une
   intention ; git décrit un fait. **La confrontation révèle ce que les
   fichiers taisent** — branche orpheline, PR fusionnée, chiffre périmé.

*(Chemins en backticks, à lire au besoin — pas en `@import`, qui
chargerait chaque fichier en entier à chaque session.)*

## Non-négociables

- **`Papu_Chess.html` est la source de vérité** de l'application, et se
  **livre complet** : jamais d'extrait présenté comme le fichier, jamais
  de version partielle écrite par-dessus.
- **Jamais de merge sur `main`** sans le mot explicite de Flavien. Sur
  branche de travail, commit et push libres. Ouvrir une PR oui ; la
  fusionner non — c'est son clic.
- **Le diff est toujours montré**, pour la trace.
- **Toute réponse substantielle se consigne dans `_sessions/AAAA-MM-JJ.md`
  AU FIL DE L'EAU** — au moment où elle est donnée, non gardée pour la
  clôture : une conversation peut mourir sans clôture propre.
- **Dépôt PRIVÉ depuis le 2026-08-09** (réversible : `gh repo edit
  --visibility public`). GitHub Pages est désactivé tant qu'il l'est.

## Les deux mots d'amorce

- **« reprise »** → relire le protocole (`REPRISE.md` et ce qu'il
  désigne) et le confronter à git, **avant** de répondre autre chose.
- **« consigne »** → graver au fil de l'eau toute décision, règle ou idée
  née dans l'échange : règle durable dans `PRINCIPES.md`, chantier dans
  `_fonds/RESTE_A_FAIRE.md` avec ses deux portes, contexte dans
  `_sessions/`. Détail dans `REPRISE.md`.

## Division du travail

Conversation = raisonnement et arbitrage ; Code = fichiers, git, outils
locaux ; Chromium = exécution et constat à l'écran ; **Flavien = le
jugement**, irremplaçable — un mécanisme certifié n'est pas une
démonstration jugée.

**Le dépôt étant privé, la conversation ne le lit plus en direct : Code est
sa source de vérité.** Réponse longue → `_rapports/AAAA-MM-JJ-sujet.txt`
(ENTIÈRE, non résumée, non versionnée), que Flavien joint au fil ; vérif
courte → le terminal. `_sessions/` reste la mémoire. Cf. `REPRISE.md` § 4.
