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
- Inspiration, pas imitation : le Fou absorbe la MÉTHODE de Marc
  Quenehen (et plus tard Julien Song), jamais sa voix ni ses mots.

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
