# Reprise — Papu Chess

Ce fichier est le premier lu à chaque reprise de discussion. Il ne raconte
pas l'histoire du projet — c'est le rôle de `JOURNAL.md` et de
`_sessions/`. Il répond à une seule question : **si je débarque à froid,
que faire dans les 30 premières secondes ?**

---

## 1. Protocole (à exécuter AVANT toute autre réponse)

- **Quand Flavien écrit « reprise »** : lire ce fichier, puis dans
  l'ordre `_fonds/RESTE_A_FAIRE.md` (plan de route en ordre
  d'exécution), `PRINCIPES.md` (règles), et le dernier fichier de
  `_sessions/` (contexte frais) — avant de répondre autre chose.

- **Quand Flavien écrit « consigne », ou en fin de session** : toute
  décision, règle ou idée née dans la conversation doit être gravée AVANT
  clôture. Règle durable → `PRINCIPES.md`. Chantier → `RESTE_A_FAIRE.md`,
  avec ses **deux portes** (« pas avant… » / « dès que… », cf. PRINCIPES,
  « Discipline des items parqués »). Contexte de séance → le
  `_sessions/` du jour.
  - **La consignation se fait AU FIL DE L'EAU**, au moment où la décision
    naît, pas gardée en réserve pour la fin. La clôture de session n'est
    qu'un **filet de rattrapage**, jamais le mécanisme principal : une
    conversation peut mourir brutalement — limite atteinte, réponse qui
    ne charge pas — sans clôture propre. Ce qui n'a pas été écrit à
    l'instant où il est né est ce qu'on perd.

---

## 2. Contrat de mémoire

- Claude-conversation **ne persiste pas** d'une discussion à l'autre : le
  **DÉPÔT est la mémoire du projet, pas Claude**. Toute chose destinée à
  survivre à la conversation doit être écrite dans le dépôt avant la
  clôture, jamais laissée à la seule mémoire de Claude.

---

## 3. Où on en est

> **En cas de divergence entre cette section et l'état git réel, GIT FAIT
> FOI : cette section n'est qu'un pointeur de confort.**

*Rafraîchie par Claude Code **à chaque push** sur la branche de travail,
pas seulement en fin de session — c'est une routine de push, pas un geste
de clôture. État constaté au 2026-08-06.*

- **`main`** : porte désormais **le noyau organisationnel en six
  fichiers** — ce fichier, `PRINCIPES.md`, `_fonds/RESTE_A_FAIRE.md`,
  `.claude/settings.json`, `.gitignore`, `.githooks/pre-push`. PR #1
  (noyau) et #2 (hook) fusionnées par Flavien le 2026-08-06. Le
  protocole est donc **lisible depuis la branche par défaut** : c'était
  le défaut radical relevé par l'audit du noyau (cf. `_sessions/`).
- **Branche active** : `wip-demo-jouable`, poussée sur `origin`
  (upstream configuré), **synchronisée avec `main`** — aucun retard.
- **Hook `pre-push`** : refuse tout push vers `main`, y compris sa
  suppression — là où les règles `deny` ne couvrent que Claude Code, lui
  est dans le chemin de git. **`core.hooksPath` est une config LOCALE :
  versionner le hook ne l'active pas.** Après tout clone, rejouer
  `git config core.hooksPath .githooks` et `chmod +x .githooks/pre-push`.
- **Chantier en cours** : la **démonstration jouable** — FORMAT v7 (règles
  F8/F9/F10), lecteur d'étapes et overlay desktop (`94ed14c`,
  `3171897`, `40cedca`). La branche attend la **validation à l'écran par
  Flavien** avant toute fusion.
- **Décalage connu, non corrigé** : `RESTE_A_FAIRE.md` parle encore de
  « lecteur d'étapes à construire » et de migration « vers v3 », alors
  que `JOURNAL.md` acte le lecteur ramifié fusionné et une cible v5. À
  trancher par Flavien.

---

## 4. Conventions permanentes

- **Prompts Claude Code** : toujours **complets et prêts à coller**, par
  défaut, sans que Flavien le redemande — répertoire de travail, puis
  étapes numérotées.

- **Régime Code autonome sur branche `wip`** : commit et push libres,
  **jamais de merge sur `main`** sans le mot explicite de Flavien ; le
  **diff est toujours montré**, pour la trace. Des règles `deny` dans
  `.claude/settings.json` verrouillent ce point côté outil.

- **La validation à l'écran est la part de Flavien, irremplaçable** :
  rendu piloté = proposition ; son œil = validation.

- **Division du travail** : conversation = raisonnement, pédagogie,
  arbitrage ; Code = fichiers, git, outils locaux ; Flavien = validation
  visuelle et mots d'amorce (« poussé », « reprise », « consigne »).
