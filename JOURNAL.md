# Journal d'avancement — Papu Chess

Mis à jour en fin de session. Une nouvelle conversation commence par
"relis PRINCIPES.md et JOURNAL.md".

## Fait récemment
- Halo rouge d'échec (fait de position) + primitive cercle du Fou
  (voix) : câblés.
- Récolement transcripts Marc Quenehen CLOS : 2 chaînes, ~880 vidéos
  valides, 9 échecs irrécupérables. Dans _doctrine/ et Marc Quenehen/.
  7 dossiers en trop investigués (doublons/vides parasites) : aucun
  transcript valide perdu, négligés d'un commun accord.
- 9 index de contenu (A–I) construits. G stérile (fermée), C traité
  (fiches d'ouverture), H → doctrine couleur.
- doctrine_couleur_synthese.md : synthèse de la doctrine signature de
  Marc (axiome, loi arithmétique, loi de conservation, mauvais fou,
  verrou, échange). En grande partie calculable.
- Détecteur de MAUVAIS FOU VALIDÉ : câblé dans identify + seuil
  mauvais fou (verrou de pions) + Éteint coupe les cercles. 3 critères
  (≥2 pions gêneurs amis sur la couleur du fou, mobilité ≤4 cases,
  gêneurs fixés dont verrou de pion adverse via pawnHoldsSquare).
  Cercle violet + phrase du Fou. Validé en isolant fouBadBishopSquares
  dans Node (chess.js 0.10.3) sur 4 positions : fou c8 muré derrière
  verrou c5/e5 (détecté), fou sorti en f5 (silence), position de
  départ (silence), milieu de jeu ouvert (silence). identify() appelle
  bien fouOutpostSquares/fouPassedPawns/fouBadBishopSquares ; la
  branche cercles de commentAnalyzedMove est gatée sur fouMode !== 'off'.
- personnes.md : 9 fiches biographiques (format PEOPLE), local.
- Carte des réflexes adoptée : 5 rayons (Histoire, Théorie, Technique,
  Pratique, Méthode). reflexes_methode.md créé (M1 ordre de calcul,
  M2 pré-requis de combinaison, enrichi des indices combinatoires ;
  M3 vérifier les défenses ; M4 vigilance à la déprotection). Rayon
  Technique ouvert (reflexes_technique.md : graine finales de pions,
  graine vigilance au pat / sous-promotion). reserve_arbitrage.md créé
  : catalogue des éléments repérés non encore placés (motifs nommés
  catégorie E, prophylaxie, méfiance aux principes dogmatiques,
  économie des forces, progression du calcul en série, pièce attaquée
  bougée mécaniquement).
- Distinction actée entre réflexes (principes de méthode) et
  démonstrations de calcul (les séquences que Marc énonce en traçant
  flèches/cercles sur une position) : ces dernières sont à capturer en
  PGN annoté `%cal`/`%csl` via le pipeline video→PGN — nouvel usage du
  corpus tactique, distinct de l'extraction de réflexes.
- Import PGN (« Charger le texte ») corrigé : une position posée via
  en-tête `[SetUp "1"]`/`[FEN ...]` initialise désormais l'échiquier
  sur cette position (y compris sans aucun coup), et ses annotations
  `%cal`/`%csl` s'affichent (flèches/cercles) dès la position de
  départ. Bug additionnel corrigé au passage : le retrait des en-têtes
  PGN détruisait par erreur les annotations `%cal`/`%csl` situées à
  l'intérieur des commentaires `{ }`, quelle que soit la position de
  départ. Testé visuellement (Chromium piloté). La chaîne des
  démonstrations de calcul annotées (position + flèches Marc) est
  fonctionnelle de bout en bout.
- Première démonstration à étapes consignée : `_fonds/demonstrations/
  nataf_decouverte.pgn` (échec à la découverte, Igor Nataf). Format
  établi « position + étapes cumulatives » (un bloc commenté numéroté
  par étape, %cal/%csl déjà lisibles par extractVisuals()) + convention
  de couleur (R cible / Y ligne d'attaque / G case-coup de travail).
  Lecteur d'étapes dans l'app : à construire.
- Affichage réagencé (laptop) : nav-controls (⏮◀▶⏭) et statut moteur
  déplacés de sous l'échiquier vers la colonne droite (sous
  Annuler/Nouvelle/Tourner), statut moteur discret. fitBoard() corrigé
  en conséquence (réservation de hauteur pour la nav supprimée,
  sous-estimation préexistante de la ligne a-h + bordure du plateau
  comblée, margin par défaut du navigateur neutralisé) : débordement
  vertical ramené de ~50px à ~1px sur les résolutions laptop courantes.
  Liste des coups plafonnée (#movesPlayed, défilement interne) pour
  qu'une longue partie chargée ne pousse plus l'échiquier hors écran.
  Flèches de conseil livre/moteur masquées dès qu'une position FEN est
  imposée ou en mode PGN/démonstration (n'ont pas de sens hors d'une
  partie jouée depuis le départ, se superposaient aux %cal/%csl d'une
  démonstration importée). extractVisuals() corrigé : prend la
  DERNIÈRE occurrence de %cal/%csl d'un commentaire (pas la première),
  pour qu'une démonstration multi-étapes (sans lecteur dédié, étapes
  concaténées en un seul commentaire) affiche l'état cumulatif final.
- Design de la colonne droite (coach) densifié : boutons resserrés
  (hauteurs et espacements réduits partout), polices agrandies sur les
  textes clés (liste des coups, commentaire du Fou, noms des joueurs).
  Liste des coups étirée pour occuper l'espace vertical restant jusqu'au
  bas de l'échiquier, défilement interne. Bulle du Fou à hauteur
  NATURELLE (jamais coupée ni en scroll interne, un commentaire long
  s'affiche en entier) : c'est la liste des coups qui absorbe la
  variation de hauteur en se réduisant/s'étirant, les boutons entre les
  deux gardent une taille fixe. Validé par rendu piloté (Chromium
  headless) avec commentaire court et commentaire long, sur plusieurs
  résolutions laptop : aucun débordement de page, fitBoard() et layout
  mobile non affectés.

- Mise en page repensée en « page défilable assumée » (desktop) : la liste des
  coups (#movesPlayed) n'a plus de plafond ni de scroll interne nulle part
  (overflow:visible ; le .moves-played{max-height:86px} global — qui touchait
  aussi le mobile — a été retiré, contre-productif). L'échiquier + les plaques
  de joueurs (board-eval-wrap) sont en position:sticky;top:6px sur desktop :
  ils restent visibles tout en haut pendant que la page défile pour dérouler
  une longue partie. Ordre tabs→Trait→contrôles→nav→bulle du Fou→liste des
  coups déjà en place (session précédente), non modifié. Bulle du Fou :
  hauteur naturelle par défaut, scroll interne (65vh) en dernier recours
  seulement pour un commentaire vraiment très long (avant : jamais de scroll,
  jamais de plafond). Bug latent corrigé au passage : .player-plate n'avait
  pas de largeur définie (shrink-to-fit centré par align-items:center du
  parent), donc le nom (max-width:60%) se résolvait contre une boîte minuscule
  et tronquait "Noirs" en "No…" — invisible à .96rem, devenu flagrant en
  l'agrandissant. Fixé par .player-plate{width:100%}. Noms des joueurs
  agrandis (1.12rem, weight 800, contraste renforcé) sur desktop et centrés
  horizontalement sur la largeur du plateau (justify-content:center + padding
  symétrique ; avant : calés à gauche via un padding-left:20px orphelin). Titre
  "Coach & Encyclopédie" → "Papu-Chess", cliquable (h1 + mini-title),
  réinitialise l'app comme le bouton Nouvelle (onclick="reset()"). Validé par
  rendu piloté (Chromium headless, serveur local) : défaut, partie très
  longue (300+ demi-coups synthétiques), commentaire très long, et mobile
  (position:static conservée, liste non plafonnée aussi bénéfique côté
  mobile). Piège méthodologique noté : --screenshot de Chromium headless ne
  restitue pas fidèlement un window.scrollTo() déclenché en JS avant capture
  (une div position:fixed;top:0 n'apparaît pas à y=0 sur l'image) — la preuve
  fiable du sticky a été obtenue via getBoundingClientRect() (DOM), pas par
  inspection visuelle du screenshot à cet instant précis.

## Prochains chantiers (ordre indicatif)
- Schéma de données d'un EXERCICE (position FEN, type, consigne,
  réponses, explication, source). À figer avant de peupler.
- Peupler les exercices depuis les "mettez en pause" du corpus Marc
  (déjà repérés dans la doctrine couleur).
- Suite de la doctrine couleur calculable : comptage de couleur,
  détection du verrou.
- Catégories d'index encore à arbitrer : A, E, F, I.
- Fiches personnes + repertoire_C à insérer dans OPS/PEOPLE.
- Sous-doctrine "fous de couleurs opposées" (repérée, non traitée).
