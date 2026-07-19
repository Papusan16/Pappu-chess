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
