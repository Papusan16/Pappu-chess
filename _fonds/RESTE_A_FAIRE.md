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
