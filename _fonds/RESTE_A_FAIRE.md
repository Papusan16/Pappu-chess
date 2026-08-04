# Reste à faire

Journal des chantiers en suspens, pour qu'une conversation neuve sache où
on en est sans avoir à reconstituer l'historique. À relire à côté de
`JOURNAL.md` (fait récemment) et `PRINCIPES.md` (architecture).

---

- Lecteur d'étapes des démonstrations à construire (avancer/reculer dans
  une démo à étapes cumulatives, cf. `_fonds/demonstrations/
  nataf_decouverte.pgn`).

- Vérifier que le lexique de normalisation attrape toutes les variantes
  phonétiques de « cavalier » (cahier, café, caviar…).

- **Signalement dynamique des pièces en prise** (idée pour plus tard).
  Faire réagir discrètement — alternance subreptice de couleur, pulse —
  les pièces mises en prise par le dernier coup. C'est un **FAIT DE
  POSITION, pas une annotation pédagogique** : même famille que le halo
  d'échec, donc **survit au mode Éteint** (cf. `PRINCIPES.md` : ce qui
  est fait de position est porté par l'échiquier ; ce qui est la voix du
  Fou s'éteint). À distinguer nettement des cercles et flèches du Fou.
  Utile en jeu comme en analyse, et **indépendant de l'encyclopédie** —
  ce chantier ne dépend d'aucune phase de la feuille de route.

- Normalisation des coordonnées mal transcrites par YouTube : lettre de
  colonne perdue ou phonétisée (« note 4 » → e4, « le 4 » → e4,
  « 9 8 » → f8) — chantier pour le pipeline video→PGN et la lecture des
  variantes de Marc.

- Flèches de conseil du Fou présentes au coup 0 d'une partie importée
  (négligeable ; à masquer un jour quand `pgnMode` actif au curseur 0).

- Débordement sur très petites fenêtres (1024×600, préexistant), hors
  fourchette laptop standard.

- Commentaire du Fou extrêmement long (plusieurs paragraphes) sur petite
  fenêtre : léger débordement de page (la bulle est à hauteur naturelle,
  la liste des coups absorbe la variation mais finit par toucher son
  plancher). Cas non rencontré avec les commentaires réels du Fou ; à ne
  traiter que si ça se présente.

- Détecteur de mauvais fou (et fouOutpostSquares/fouPassedPawns/fouHangingSquares) : ne
  se déclenche JAMAIS sur une position FEN statique chargée sans le moindre coup — ces
  fonctions rejouent `fullMoves[0..mi]` (rempli par `syncFull()`/`game.history()`), donc
  avec `fullMoves` vide (0 coup importé), `mi` n'a pas de sens et la fonction retourne `[]`
  ; le second point d'appel (panneau coach, ligne ~3670) est en plus gaté par
  `cursor>0`, cursor valant aussi 0 sans coup. Il faut au moins UN coup à naviguer (PGN
  avec historique, même minimal) pour voir un cercle structurel (avant-poste, pion passé,
  mauvais fou) — une position posée seule (FEN nu ou PGN `[SetUp]/[FEN]` sans coup) reste
  silencieuse par construction, ce n'est pas un bug isolé mais une propriété actuelle de
  l'architecture (mi/cursor comme seule notion de "position courante").
- Bug latent (repéré en marge, non corrigé) : ces 4 fonctions rejouent TOUJOURS depuis
  `new Chess()` (position de départ standard), jamais `new Chess(startFen)` — un PGN
  importé avec en-tête `[SetUp "1"]/[FEN ...]` (position de départ non standard) fera
  rejouer les mêmes `{from,to}` depuis la mauvaise position de base. Sans conséquence
  tant que testé sur une partie normale (position de départ standard, ce que fait cette
  note) ; à corriger le jour où l'analyse structurelle doit couvrir une démonstration
  posée sur FEN non standard.

- `doctrine_couleur_synthese.md` annoncée au JOURNAL.md (axiome, loi
  arithmétique, loi de conservation, mauvais fou, verrou, échange) mais
  absente du disque — jamais écrite comme fichier séparé (recherche
  exhaustive : par nom sur tout `~/Téléchargements/Echecs`, par contenu
  `grep -rl` sur "loi de conservation"/"axiome"/"verrou"/"mauvais fou", et
  dans tout l'historique git du dépôt Papu-Chess, `git log --all` et
  `git log --all -S`. Le seul fichier jamais committé au nom proche est
  `_fonds/reflexes_synthese.md`, sans rapport — réflexes de méthode, pas
  doctrine couleur — absorbé depuis dans `reflexes_methode.md`. "loi de
  conservation"/"axiome" n'apparaissent QUE dans JOURNAL.md lui-même,
  jamais dans un fichier de contenu, à aucun commit). À reconstruire
  depuis `_doctrine/Mauvais Fou.txt` / `doctrine_couleur.txt` si besoin —
  la doctrine qualitative de Marc y est intacte (mauvais fou = fou de la
  couleur de ses pions, remède = échanger son mauvais fou contre le bon
  fou adverse), mais aucun seuil chiffré n'y est donné.

- [260722] Piste explorée : Leela & Maia comme outils d'auteur (PAS runtime).
  Contexte : discussion sur Stockfish et ses concurrents. Piste à réévaluer
  plus tard, consignée pour ne pas la perdre.
  Cadre non négociable : Leela (Lc0) NE PEUT PAS remplacer Stockfish comme
  moteur embarqué. Raison : modèle de déploiement navigateur (HTML + WASM
  lite mono-thread). Leela = réseau lourd conçu pour GPU, poids de plusieurs
  Mo à dizaines de Mo, support WebGPU inégal → casse la légèreté de l'app.
  Le runtime reste stockfish-18-lite-single. Point fermé.
  Deux fils distincts à instruire :
  - FIL 1 — Leela en authoring (outil local, hors temps réel) : Lc0 tourné
    en local sur Ubuntu (CPU seul suffit, lenteur sans importance),
    interrogé sur les positions des démonstrations pour récupérer des
    lignes plus « principielles » que Stockfish (coup positionnellement
    propre là où SF part parfois en ligne computer-only injouable pour un
    humain). Contenu figé dans le fonds. Cohérent avec la règle « données
    séparées du code ». Leela = filtre de plausibilité pédagogique, PAS
    générateur de leçon.
  - FIL 2 — Maia comme modèle de l'élève (pour l'onglet S'exercer /
    École) : Maia = dérivé de Leela entraîné à prédire le coup qu'un humain
    d'un Elo donné jouerait (Maia-1100, 1500, 1900...), erreurs comprises.
    Permet d'anticiper l'erreur probable de l'élève à un niveau ciblé →
    construire des pièges calibrés pour l'onglet École (« mettez en pause,
    que joueriez-vous ? »). Attention : Maia prédit le coup humain, ce
    n'est PAS un oracle du meilleur coup. Outil pour MODÉLISER l'élève, pas
    pour lui montrer la vérité.
  Garde-fou transversal : aucun moteur ne verbalise un plan. Ni SF ni Leela
  ne sortent « contrôle de la colonne c, majorité à l'aile dame » en
  français. La verbalisation du plan reste le travail du Fou, inspiré de la
  méthode de Marc, arbitré par Flavien. Leela/Maia n'apportent que de la
  matière (lignes candidates, erreurs probables), jamais la leçon.

- Moteur du Fou : architecture consignée dans `_fonds/moteur_du_fou.md`
  (5 types de déclencheurs, 3 régimes commentaire/démonstration/
  consultation, 3 postures). À implémenter : moteur de sélection
  généralisant le patron du mauvais fou ; premier réflexe de type
  contexte (nom d'ouverture → plan enseigné).

- Feuille de route de l'encyclopédie (régime CONSULTATION, cf.
  `_fonds/moteur_du_fou.md`), dans cet ordre de dépendance :
  - Phase 1 : FIGER LE FORMAT D'UNE ENTRÉE d'encyclopédie (identifiant,
    rayon, explication à angles ouverts, démonstration(s) annotées
    ramifiables, sources multi-auteurs). Clé de voûte : le lecteur le
    lira, l'arbitrage le remplira. À faire avant tout code et avant
    tout arbitrage de masse.
  - Phase 2 : UNE ENTRÉE PILOTE complète, écrite au format, sans
    lecteur — crash-test du format.
  - Phase 3 : LECTEUR D'ÉTAPES RAMIFIÉ (étendre le lecteur linéaire de
    `demonstrations/nataf_decouverte.pgn` aux embranchements),
    développé contre l'entrée pilote réelle.
  - Phase 4 : BRANCHER LA CONSULTATION (interroger le Fou hors partie,
    afficher l'entrée) — chantier léger, à sa fin l'encyclopédie est
    entière à une entrée.
  - Phase 5 : REMPLISSAGE (arbitrage entrée par entrée depuis le
    corpus ; le corpus de Julien s'insère par le même pipeline).
  - Risques identifiés à garder en vue : asymétrie Marc/Julien
    (pipeline calibré sur Marc, corpus Julien non récolté — prévoir un
    lot-test Julien tôt) ; coût de l'arbitrage éditorial des entrées
    bi-sources ; volume d'arbitrage = vrai mur (prioriser par ce que le
    corpus traite le plus) ; pas de critère d'arrêt de la complétude →
    convention : une entrée est publiable quand elle dit ce que ses
    sources disent, la complétude est bornée par le corpus ; poids du
    mono-fichier à surveiller (parade déjà prévue dans PRINCIPES :
    fonds servable par API).

---

## Ouverts au 2026-08-04 (décisions arbitrées le 3-4 août)

Détail et raisons dans `_sessions/2026-08-04.md` ; ici, le chantier seul.

- **Conception de l'ÉCOLE / onglet « S'exercer », avec la collection
  « Top mats ».** Premier cas : le **mat de Nataf**, présenté en MIROIR de
  l'entrée `echec-a-la-decouverte` comme « le mat permis par l'échec à la
  découverte ». Chaque face pointe vers l'autre ; **un seul jeu de faits
  d'échiquier** (coups, `%cal`/`%csl`) partagé par les deux, seule la voix
  du Fou change (fait vs voix).
  Point dur à trancher dans cette conception : aujourd'hui une
  démonstration est **enfermée dans le `.md` de son entrée**, alors que le
  miroir suppose des faits **adressables depuis deux entrées**.
  Dépendance : côté motif, la démonstration doit s'arrêter au moment
  crucial et renvoyer vers la séquence du Top mats — ce renvoi est
  aujourd'hui un **lien-amorce inerte**, et le reste tant que l'École
  n'existe pas.
  Rappel : **l'École est un RÉGIME (axe d'usage), pas un rayon ni un
  onglet de contenu** — la réconciliation des catégories de la phase 4 ne
  la couvre pas.

- **Lecteur — deux corrections d'ergonomie** : mettre les **flèches de
  navigation cliquables en surbrillance** (rien ne signale qu'elles sont
  le geste principal de la lecture) ; **déplacer les boutons de variantes
  SOUS les flèches de navigation**, et non en bas du panneau — à
  l'embranchement, choisir une branche prolonge le geste d'avancer.

- **Vignette-photo au survol du nom d'un personnage** (idée en réserve,
  non arbitrée). Ni la source des images ni le comportement sur téléphone
  (où il n'y a pas de survol) ne sont tranchés.

- **Migrer `mauvais-fou.md` du format v2 vers v3.** Ses **5
  démonstrations ne se jouent pas** : elles sont écrites en « ##
  Démonstrations » + « ### Démonstration N », que le lecteur d'étapes v3
  ne sait pas lire — il n'en tire ni FEN de départ ni étapes. L'entrée
  s'affiche correctement (prose intacte, encadré « non jouable en l'état »
  à la place de chaque bouton), donc rien n'est cassé, mais l'entrée
  pilote de la phase 2 est aujourd'hui la seule entrée dont on ne peut
  rien dérouler. Alternative à peser au moment de le faire : étendre le
  parseur plutôt que migrer l'entrée.
