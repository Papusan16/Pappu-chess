# Principes fondateurs — Papu Chess

Décisions d'architecture et de conception qui cadrent toutes les
décisions futures. À relire au début de chaque session.

## Nature du Fou
- Le Fou est un COMMENTATEUR pédagogique, pas un moteur de jeu.
- Il est entièrement ÉTEIGNABLE : mode Éteint = absence totale
  (aucune parole, aucun cercle, aucune flèche). L'échiquier reste
  pleinement fonctionnel sans lui.
- Distinction fondatrice FAIT vs VOIX : ce qui est un fait de la
  position (dernier coup, roi en échec / halo rouge) est porté par
  l'échiquier et survit au mode Éteint. Ce qui est la voix du Fou
  (cercles et flèches violets, commentaires) disparaît avec lui.
- DOUBLE FILIATION : le Fou est la FUSION de deux pédagogies : Marc
  Quenehen et Julien Song. Ce n'est pas un socle Marc avec Julien en
  appoint : les deux sont constitutifs de son identité.
  - La fusion est une SYNTHÈSE en une voix unique, pas une
    juxtaposition. Marc est un pédagogue de l'improvisation qui
    dramatise l'échec en direct ; Julien un pédagogue de la structure
    qui pré-empte la confusion. Sur un même objet, ils n'expliquent
    pas pareil : la synthèse relève d'un arbitrage éditorial humain
    (Flavien), entrée par entrée.
  - Le fonds est MULTI-SOURCES PAR CONCEPTION : toute entrée porte sa
    ou ses sources (Marc / Julien / les deux, avec vidéo + timecode).
    Aucune structure du fonds ne doit supposer une source unique.
  - Règle absolue inchangée : inspiration, pas imitation — la
    MÉTHODE, jamais la voix ni les mots.

## Les trois postures de l'utilisateur
- JOUER : contre le Fou, moteur Stockfish WASM local. L'utilisateur
  est joueur. En live, le Fou ne révèle rien qui aiderait (anti-triche
  / anti-"tell").
- ANALYSER : partie FIGÉE (PGN, FEN, lien importé). Jamais demander à
  l'utilisateur de poser les coups d'un camp à la main. Le Fou
  commente le passé.
- S'EXERCER (onglet École) : positions posées à résoudre, "que
  joues-tu ?" à la manière de Marc. Types d'exercices : diagnostic,
  calcul vérifiable, choix commenté, trouve-le-plan. C'est le seul
  mode où le Fou est pleinement professeur.

## Architecture
- Le FONDS (doctrine, fiches d'ouverture OPS, personnes PEOPLE,
  réflexes, exercices) est de la DONNÉE séparée du code, dans des
  structures identifiables. Objectif : pouvoir un jour la servir par
  API sans réécrire le Fou.
- Jeu temps réel contre des humains (éventuel, futur) : déléguer à
  Lichess (API ouverte) plutôt qu'à un backend maison. Chess.com =
  lecture seule (import PGN de parties finies uniquement).
- Pas de localStorage éparpillé : toute persistance future passe par
  une couche redirigeable (navigateur aujourd'hui, API demain).
- L'app reste un fichier HTML autonome, servable tel quel depuis un
  serveur le jour venu, sans réécriture.

## Discipline de canonicité
- Papu_Chess.html dans le dépôt est LA source de vérité, pas les
  conversations ni la mémoire de Claude. Toujours livrer le fichier
  complet et à jour.
- Les réponses de Claude Code sont consignées dans `_sessions/`
  (un fichier par jour, append horodaté) et poussées, pour que
  Claude-conversation les lise DEPUIS LE DÉPÔT au lieu qu'elles soient
  copiées à la main (et tronquées). Voir `_sessions/README.md`.
- Tout travail d'ORGANISATION destiné à servir de socle (protocole,
  principes, plan de route, garde-fous) doit ATTERRIR SUR `main`, jamais
  rester otage d'un chantier applicatif en attente de validation. `main`
  est la branche par défaut : c'est elle qu'une reprise à froid lit en
  premier. Un protocole de reprise dont le point d'entrée n'est pas sur
  `main` n'existe pas pour qui débarque — il ne sert que ceux qui savent
  déjà où regarder, c'est-à-dire personne. Corollaire pratique : dès
  qu'un fichier d'organisation naît sur une branche de chantier, ouvrir
  une branche séparée depuis `main` qui ne porte QUE lui, sans code
  applicatif — son risque est nul, elle n'a pas à attendre une
  validation à l'écran qui porte sur autre chose.

## Discipline des items parqués
- Tout item repoussé à plus tard porte DEUX PORTES, jamais une seule :
  une condition de sommeil (« pas avant… ») ET un signal de réveil
  (« dès que… ») accroché à un événement observable. Un « pas avant »
  seul est une écriture morte : il dit quand ne pas commencer, jamais
  quand commencer, et l'idée se perd en silence.
- Le signal de réveil se pose AU SITE DU SIGNAL, pas seulement là où
  dort l'item : un pointeur depuis la dépendance vers le dépendant, pour
  qu'il tombe sous les yeux au moment où la condition se réalise, pas
  dans un fichier qu'on n'aurait pas rouvert.
- Exemple : l'accueil éditorialisé dort dans `RESTE_A_FAIRE.md` (« pas
  avant que le rayon Histoire soit garni »), mais son réveil est planté
  DANS le rayon Histoire (« ces fiches datées sont sa matière, le
  réveiller »).
