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

> **GIT FAIT FOI.** Cette section ne recopie donc **ni SHA, ni nombre de
> commits, ni liste de branches** : recopiés à la main, ils périment en
> silence et finissent par mentir. Pour l'état factuel, demander à git —
> c'est plus court que de le lire ici, et c'est vrai :
>
> ```
> git fetch && git log --oneline main..HEAD && git ls-remote origin refs/heads/main
> ```
>
> (avance de la branche courante sur `main`, puis où en est `main` côté
> serveur ; pour le retard, inverser : `git log --oneline HEAD..main`.)

Ne reste ici que ce que git **ne dit pas** :

- **Chantier en cours** : la **démonstration jouable** — FORMAT v7
  (règles F8/F9/F10), lecteur d'étapes ramifié et overlay desktop, sur la
  branche `wip-demo-jouable`.
- **Le LECTEUR est validé** (le mécanisme : navigation, `isBranchEnd`,
  `no-store`) — vérifié à l'écran par l'instance Claude du navigateur, y
  compris sous clics en rafale. Mesures : `_sessions/2026-08-08.md`.
- **Ce qu'il attend, et que Claude ne peut pas donner** : la validation
  de la **démonstration Nataf dans son ENSEMBLE** — contenu, chapeau,
  viseur, rythme, fin — **par l'œil de Flavien**, avant toute fusion. Une
  instance de Claude peut certifier qu'un mécanisme fonctionne ; le
  jugement de goût sur la démonstration est **la part de Flavien,
  irremplaçable** (cf. `PRINCIPES.md`). **Ne pas déclarer cette
  validation faite tant que Flavien ne l'a pas dite lui-même** — un
  mécanisme vérifié n'est pas une démonstration jugée.
- **Autre geste en attente, côté Flavien** : le **ruleset GitHub
  `protection-main`** — le seul verrou côté serveur, là où les règles
  `deny` et le hook `pre-push` restent locaux et contournables. Marche à
  suivre détaillée dans `_sessions/2026-08-06.md`.
- **Décalage résiduel, mineur** : l'item `mauvais-fou.md` de
  `RESTE_A_FAIRE.md` vise encore « le format v3 », alors que FORMAT est à
  v7. Le chantier reste réel (ses 5 démonstrations ne se jouent pas), seul
  le numéro de cible est périmé. L'autre moitié de ce décalage — « lecteur
  d'étapes à construire » — est **fermée** depuis le 2026-08-08.
- **Piège d'installation** : `core.hooksPath` est une config **locale** —
  versionner `.githooks/pre-push` ne l'active pas. Après tout clone :
  `git config core.hooksPath .githooks && chmod +x .githooks/pre-push`.

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

- **Le dépôt est PRIVÉ depuis le 2026-08-09.** Décision de Flavien,
  assumée et réversible : `gh repo edit Papusan16/Pappu-chess
  --visibility public --accept-visibility-change-consequences` (le flag
  est exigé dès qu'on touche `--visibility` ; il n'existe qu'à partir des
  `gh` récents — le paquet Ubuntu 2.45 ne le connaît pas). **GitHub Pages
  est désactivé** tant que le dépôt est privé — Pages sur dépôt privé
  demande un compte Pro. `papusan16.github.io/Pappu-chess/` répond 404, et
  ne redémarrera pas tout seul au retour au public : il faudra le
  réactiver dans Settings.

- **La conversation Claude ne lit plus le dépôt en direct.** C'était le
  canal monté pour que le journal lui parvienne sans troncature ; le
  passage en privé le ferme. **Sa source de vérité est désormais Claude
  Code**, selon un partage à tenir :
  - **Réponse longue** (rapport, diagnostic, reconnaissance, diff
    commenté) → **consignée dans `_rapports/AAAA-MM-JJ-sujet.txt`**, que
    Flavien joint au fil. Le fichier porte la réponse ENTIÈRE, non
    résumée : c'est tout l'intérêt du montage.
  - **Vérification courte** (un hash, un `diff --stat`, une visibilité)
    → **le terminal suffit**, ça se copie sans se tronquer.
  - **Validation à l'écran** → l'**instance Chromium** exécute et
    constate. Elle certifie qu'un mécanisme fonctionne ; elle ne remplace
    pas **le jugement de goût, qui reste la part de Flavien** (cf. la
    convention ci-dessus, et `_sessions/2026-08-08.md`).

  **`_rapports/` n'est PAS versionné** (cf. `.gitignore`) : ce sont des
  transcriptions jetables. Ce qui doit survivre à la séance va dans
  `_sessions/`, qui l'est. Les deux ne se remplacent pas — un rapport est
  un moyen de transport, une entrée de `_sessions/` est de la mémoire.
