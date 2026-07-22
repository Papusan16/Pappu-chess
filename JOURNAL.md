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
- Persistance de la fiche profil corrigée : les champs pseudo rapides
  Lichess/Chess.com (Modes & réglages) n'avaient aucun handler et ne
  sauvegardaient jamais rien tant qu'on n'ouvrait pas séparément la fiche
  Profil complète pour cliquer « Enregistrer » — ajout de
  oninput="saveIdentity()" sur les deux champs, comme le pseudo app.
  importLastChesscom() redemandait aussi le pseudo à CHAQUE clic (même
  intra-session) car le pseudo obtenu via prompt() n'était jamais réécrit
  dans le champ ni sauvegardé : corrigé (écrit dans le champ + saveIdentity()
  avant utilisation). Persistance testée par navigation Chromium headless
  séparée sur le même profil navigateur (véritable rechargement, pas la
  mémoire JS d'un seul onglet) : les pseudos survivent bien au rechargement.
  Diagnostic écarté : ce n'était pas un problème d'origine file:// vs
  localhost (le lancement local sert toujours sur le port fixe 8000).
- Orientation automatique du plateau selon le pseudo de l'utilisateur :
  un embryon existait déjà (playerNameFor() comparait déjà les pseudos, mais
  seulement casse+trim, et seulement pour afficher le badge « toi » — rien ne
  pilotait l'orientation). Ajout de normPseudo()/pseudoMatches()/myPseudos()
  (comparaison tolérante : casse, espaces/underscores/tirets équivalents,
  partagée avec le badge « toi » upgradé au passage) et branchement dans
  announceImportedGame() : si [White] ou [Black] du PGN importé correspond à
  un pseudo du profil, chooseColor() bascule automatiquement l'échiquier de
  ce côté, sans clic sur Tourner. Testé (headless, isolé) : pseudo Lichess
  "Papu_San" vs tag PGN chess.com "Papu_san" (casse/underscore différents) →
  matché, flipped=true, colorChosen=true. Cas témoin sans pseudo
  correspondant → aucun flip (pas de faux positif).

- Limite du détecteur de mauvais fou (et de fouOutpostSquares/fouPassedPawns/
  fouHangingSquares) confirmée puis consignée : ces fonctions rejouent
  `fullMoves[0..mi]` (rempli par syncFull()/game.history()) ; sur une position
  FEN statique importée SANS aucun coup, `fullMoves` est vide et les deux
  points d'appel du cercle (commentAnalyzedMove, panneau coach gaté par
  `cursor>0`) restent silencieux par construction — pas un bug isolé, une
  propriété actuelle de l'architecture (mi/cursor = seule notion de position
  courante). Il faut au moins un coup à naviguer pour voir un cercle
  structurel. Bug latent distinct repéré en marge (non corrigé) : ces 4
  fonctions rejouent toujours depuis `new Chess()` (position standard),
  jamais `new Chess(startFen)` — sans effet sur une partie normale, mais un
  PGN `[SetUp]/[FEN]` non standard AVEC des coups serait mal rejoué. Les
  deux points notés dans `_fonds/RESTE_A_FAIRE.md`.
- Détecteur de MAUVAIS FOU REFONDU (4 critères cumulatifs A+B+C+D — mobilité
  SÛRE nulle/SEE 1 coup, étouffement DURABLE par ≥2 pions fixés, comptage de
  couleur seuil N=3, pas d'échappatoire de développement seuil 3) et VALIDÉ À
  L'ÉCRAN sur deux cas :
  - PGN Française d'Avance construite (14 coups, cxd4/cxd4 libère c5,
    13.Nb3-c5 prive le fou c8 de sa seule case légale Bd7, non défendue —
    dame chassée en a7 plutôt qu'en d8) : re-vérifiée hors UI (Node, chess.js
    0.10.3 embarqué, fouBadBishopSquares extraite verbatim — `c8` seul
    candidat, fouOutpostSquares/fouPassedPawns vides) PUIS collée dans
    « Charger le texte » et confirmée à l'écran : cercle sur c8 au dernier
    coup. PGN : `1. e4 e6 2. d4 d5 3. e5 c5 4. c3 Nc6 5. Nf3 Qb6 6. a3 Nh6
    7. Bd3 Be7 8. O-O O-O 9. a4 cxd4 10. cxd4 a6 11. a5 Qa7 12. Nbd2 Re8
    13. Nb3 Kh8 14. Nc5` (⏭ Fin ou clic sur 14.Nc5).
  - Partie chess.com importée par l'utilisateur, coup 14 : le fou personnel
    de l'utilisateur, que l'ancienne définition (mobilité brute ≤4 cases,
    sans notion de sûreté ni de comptage de couleur) aurait signalé à tort,
    n'est plus entouré avec la nouvelle définition — faux positif éliminé,
    confirmé à l'écran.
  Limite FEN-statique et bug latent startFen (ci-dessus) inchangés, toujours
  d'actualité avec cette refonte.

- Message du mauvais fou (`fouBadBishopMsg`) adapté au PROPRIÉTAIRE du fou
  détecté (commit `99317b5`, poussé sur origin/main après un crash du
  laptop qui avait fait perdre le commit initial — vérifié par
  `git log -S "fouBadBishopMsg"` avant de recommit) : 3 messages selon
  comparaison side du fou / couleur utilisateur (`playMode?playerColor
  :(colorChosen?myColor:null)`) — fou perso → invitation à l'échanger ou
  l'activer (« cherche à », pas un ordre) ; fou adverse → garder enfermé et
  exploiter ; camp indéterminé → neutre, sans « ton »/« adverse ». Les deux
  cas orientés VALIDÉS via Node/vm (chess.js 0.10.3 + fouBadBishopSquares/
  fouBadBishopMsg extraits verbatim du fichier réel, aucune modif du
  fichier) :
  - Fou personnel (Française d'avance, c8 Noirs) : même PGN que la refonte
    A+B+C+D ci-dessus (`1. e4 e6 2. d4 d5 3. e5 c5 4. c3 Nc6 5. Nf3 Qb6
    6. a3 Nh6 7. Bd3 Be7 8. O-O O-O 9. a4 cxd4 10. cxd4 a6 11. a5 Qa7
    12. Nbd2 Re8 13. Nb3 Kh8 14. Nc5`), utilisateur déclaré Noir → message
    "Ton fou en c8…".
  - Fou adverse (fou blanc c1) : PGN construit spécifiquement — Blancs
    jouent un système passif (1.c3/2.e3, cavalier b1 dérouté a3-c2-e5 pour
    ne pas défendre/débloquer d2) qui laisse le fou c1 muré derrière b2/d2
    jamais bougés, fixés par le pion noir c4 poussé tôt (`1. c3 c5 2. e3
    Nc6 3. Nf3 Nf6 4. Be2 e6 5. O-O Be7 6. Na3 O-O 7. Re1 d5 8. Nc2 c4
    9. Ne5 Qc7 10. f4 Bd7 11. Bf3 Rad8 12. Qe2 Ne4 13. Kh1`), utilisateur
    déclaré Noir → message "Le fou adverse en c1…". Détecteur confirmé :
    `{s:"c1",side:"Blancs",safe:0,gene:2,colorCount:4,dev:2}`.
  Pas encore chargés à l'écran par l'utilisateur (fournis, prêts à coller
  dans « Charger le texte ») — seule la vérification Node est faite à ce
  stade.

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
