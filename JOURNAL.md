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

## 2026-08-01 → 08-03 — Encyclopédie : FORMAT v3, lecteur ramifié, overlay porte unique

Chantier mené sur la branche `claude/lecteur-etapes-ramifie-8jgzz1`,
**non fusionnée dans main**. Le grain fin est dans `_sessions/2026-08-01.md`
et `_sessions/2026-08-03.md` ; ci-dessous la continuité seule.

- **FORMAT v3 entériné** (`_fonds/encyclopedie/FORMAT.md`) : sept frictions
  du crash-test ramifié — clé `verification` (rejeu obligatoire, trois FEN
  successifs s'étaient révélés faux sur la seule position Nataf), clé
  `coup` (étape d'annotation vs étape de coup), cumul des annotations à
  l'embranchement (deux sœurs n'héritent jamais l'une de l'autre), FEN
  d'entrée de branche redondant contre la divergence silencieuse, G
  redéfini (« le coup à l'étude », quel qu'en soit le camp), `nature` au
  grain de l'étape, et le **lien-amorce** : un lien vers une entrée
  inexistante est assumé, pas une erreur.
- **Phase 3 — lecteur d'étapes ramifié** : conçu puis implémenté dans
  `Papu_Chess.html` (parsing du Markdown dans l'app, sans pipeline de
  build ; arbre résolu une fois au chargement ; navigation = lecture pure ;
  vérification mécanique des invariants avec bannière). `echec-a-la-decouverte.md`
  corrigée au passage (étape A1 nommait deux coups, sous-branches sans FEN
  d'entrée — non conforme v3).
- **Phase 4 — l'overlay 📚 devient la porte unique de l'encyclopédie.**
  Conception d'abord (`bf47778`), puis implémentation en quatre pas :
  - `5858fa8` — `encyLoadEntry` coupée en parsing pur (`encyResolveEntry`)
    et prise en main de l'échiquier (`encyStartDemo`) : c'est la couture
    qui permet à l'overlay d'afficher une entrée sans rien lancer.
  - `3fdd600` — bascule fiche-en-dur / entrée riche. Manifeste
    `_fonds/encyclopedie/INDEX.json` (généré par `generer_index.py`) pour
    savoir quelles entrées existent, `fetch` du `.md` au clic comme vérité.
    Clé `remplace:` : le fichier neuf déclare la fiche en dur qu'il périme
    (`decouverte`, `bon-mauvais-fou`), sans toucher au bloc JSON de l'app.
    Toute défaillance (manifeste absent, 404, Markdown illisible) redonne
    la fiche courte — on ne perd jamais un contenu. Panneau encyclopédie
    enterré dans la zone PGN **supprimé** ; chargeur de rédaction (collage /
    fichier `.md`) **déplacé en pied d'overlay**, replié.
  - `be84768` — liens internes. Un seul résolveur : entrée riche > fiche en
    dur > **amorce** (visible, grisée, non cliquable). Syntaxe `[[id]]`
    rendue (elle était déjà employée dans les entrées sans être ni gravée
    ni affichée), champ `liens:` en bandeau « Ça rejoint : », auto-liage
    des noms cités sur segments de texte uniquement.
  - `b4f3037` — onglets **🏛️ Histoire** (qui absorbe les fiches PEOPLE,
    plus d'onglet Personnages) et **🎯 Pratique**. Le rayon reste la
    classification de fond portée par l'entrée ; l'onglet en est dérivé par
    l'app (table premier rayon + phase), avec la clé `onglet:` en
    dérogation, aveugle au moteur.
- **RIEN N'EST ENCORE VALIDÉ À L'ÉCRAN.** Tout le chantier phase 4 repose
  sur un banc d'essai Node (contexte VM, DOM de capture) : ni Playwright ni
  Chromium headless utilisables sur cette machine. La validation visuelle
  par Flavien (`serveur_echecs.py`, overlay 📚, bande des sept onglets en
  largeur téléphone) est le **prochain geste bloquant avant toute fusion
  dans main**.
- Restes connus de ce chantier : `mauvais-fou.md` est au format v2, ses 5
  démonstrations ne se jouent pas ; conventions de prose du lecteur
  (`ÉTAPE X — …`, `### Branche A — « … »`) encore implicites.

## 2026-08-04 — PALIER : la branche lecteur-etapes-ramifie fusionnée dans main

**Premier état public de l'encyclopédie-overlay.** Fusion validée à
l'écran par Flavien, commit de fusion explicite (`--no-ff`) : 24 commits,
13 fichiers. La branche est conservée, non supprimée.

Reste ouvert :

- **École / Top mats** — deux amorces `top-mats-nataf` l'attendent déjà
  (le « ici » de la pause de `echec-a-la-decouverte`, et le champ `liens`
  de `nataf`). Elles s'allumeront d'elles-mêmes le jour où l'entrée
  portera cet id.
- **Migration de `mauvais-fou` du format v2 vers v5** : ses cinq
  démonstrations ne se jouent pas (prose intacte, encadré « non jouable »
  à la place de chaque bouton).
- **Vérifications Nataf à la vidéo** : la fiche porte une biographie tenue
  pour vérifiée mais dont la référence bibliographique n'est pas
  consignée, et la position de la démonstration n'est rattachée à aucune
  partie identifiée.

## 2026-09-05 — Consignation de la capture premium Chess.com du 04/09

**Sauvegarde des données premium du compte « Papu_san » avant expiration
de l'abonnement Diamant** (capture faite le 4 septembre, consignée le 5).

- Deux blobs de données, **gitignorés** (backup via Google Drive) :
  `papu_san_chesscom_data.json` (~176 Ko) et
  `papu_san_chesscom_data.csv` (~61 Ko). Contenu : profil Diamant,
  classements et records, stats avancées par thème, et l'historique
  rating partie par partie — **577 parties Rapide + 27 En différé, dont
  14 classées** (bilan officiel 5 V / 0 N / 9 D) et 13 amicales.
  Les PGN des parties avaient déjà été exportés par ailleurs.
- **Versionnés** : le détail chiffré — d'abord écrit dans `_rapports/`,
  migré le 2026-09-06 vers `_sessions/2026-09-05.md` (§ « Archive
  intégrale ») — et le manifeste `_sauvegardes/chesscom/MANIFESTE.md`,
  qui dit ce qui existe, où et de quand ça date.
- **Point clos** : l'écart apparent En différé (14 au bilan contre 27 à
  l'historique) n'en était pas un — deux périmètres qui coexistent,
  14 classées + 13 non classées. Le Rapide, lui, est classé à 100 %
  (268 + 44 + 265 = 577). Aucun écart réel.

## 2026-09-06 — Le détail premium rentre dans le rang : `_rapports/` redevient transient

**Correction de doctrine, pas de contenu** — pas un chiffre n'a bougé.

- Le détail chiffré de la capture premium sort de
  `_rapports/rapport_2026-09-04-donnees-premium-chesscom.txt` (fichier
  supprimé) et rejoint **`_sessions/2026-09-05.md`, section « Archive
  intégrale »**, repris tel quel. La veille il n'était entré dans git que
  par un `git add -f` contre le `.gitignore` : l'exception est levée,
  `_rapports/` retrouve son statut de **transport jetable**, `_sessions/`
  reste la mémoire. Le manifeste pointe désormais vers `_sessions/`.
- **Branche parasite : supprimée côté serveur le 2026-09-06.**
  `claude/chesscom-premium-backup-va8zki`, créée par le harnais distant,
  est un doublon exact de `wip-sauvegarde-chesscom`. Elle est supprimée
  sur GitHub depuis une session locale :
  `git push origin --delete claude/chesscom-premium-backup-va8zki` a
  renvoyé `[deleted]` et le code 0, et elle est absente de
  `git ls-remote`. Le refus HTTP 403 noté la veille venait du proxy git du
  conteneur distant, pas des droits sur le dépôt. Le SHA `7346e84` reste
  conservé par GitHub tant que l'objet vit, donc la branche est recréable
  si besoin : `git push origin 7346e84:refs/heads/<nom>`. La branche
  canonique reste `wip-sauvegarde-chesscom`, seule conforme à la
  convention `wip-` du dépôt.
- **Chantier `sauvegarde-chesscom` clos.** Deux exports du 4 septembre
  coexistaient dans `~/Téléchargements` ; le diagnostic a tranché pour
  celui de **13:03**, qui porte une partie en différé de plus — 604 parties
  dont 27 en différé, contre 603 dont 26 pour l'export de 07:25 — et une
  clé `note` disant qu'il inclut les parties du jour. Les deux n'ont pas le
  même schéma : `manualStats` pour l'ancien, `summary` + `detailedStats`
  pour le retenu. Ce dernier est archivé sous `_sauvegardes/chesscom/`
  (gitignoré, sauvegardé par bisync Drive). Le manifeste est corrigé aux
  **octets exacts** — 179 920 et 63 015, là où il annonçait « ~176 Ko /
  ~61 Ko » sans les avoir mesurés — et documente désormais le schéma pour
  les scripts à venir. Le décompte « 577 Rapide + 27 En différé » qu'il
  portait déjà était celui de ce jeu-ci, pas de l'autre. Reste à la main de
  Flavien : **la fusion vers `main`**.

## 2026-09-10 — Audit de véracité des assertions de reprise (lecture seule)

Toutes les assertions de la reprise de 07:35 passées au crible, verdict
explicite et sortie brute à l'appui ; aucun fichier touché hors
`_sessions/2026-09-10.md` et celui-ci. Détail complet dans
`_sessions/2026-09-10.md` (entrée de 07:55).

- **3 verdicts FAUX sur 10**, tous du côté `gdrive-sync`, aucun sur
  Papu-Chess : deux crons vestigiaux (`~/rclone_sync_bidirectionnel*.sh`)
  tournent toutes les 10 min sans aucun garde-fou du moteur et **échouent
  silencieusement depuis le 31/08 et le 01/09** ; le `client_secret_*.json`
  n'est plus dans le périmètre synchronisé (item à fermer) ; `gdrive-sync`
  n'a pas tourné le 09/09 — son journal s'arrête au 08/09 10:21.
- **Conséquence pour ce dépôt** : le manifeste de `_sauvegardes/chesscom/`
  annonce un « backup via Google Drive » que plus rien n'assure depuis le
  08/09. Les octets des deux blobs sont exacts (179 920 / 63 015), leur
  poussée vers Drive ne l'est pas.
- **Tenue du journal** : aucune entrée fausse, aucune date fausse — mais
  la mémoire est **dispersée sur quatre branches**. `main` ne porte que 6
  des 15 fichiers `_sessions/`, la fusion de la PR #6 (09/09) n'est
  journalisée nulle part, et `REPRISE.md` renvoie depuis `main` à
  `_sessions/2026-08-06.md`, absent de `main`.

## 2026-09-15 — Cron vestigial neutralisé ; RECTIFICATIF : la sauvegarde Drive était bien prouvée

Détail complet dans `_sessions/2026-09-10.md` (entrée du 15/09, 07:20 —
l'append reste dans le fichier du 10/09, comme demandé).

- **Neutralisation faite.** Les deux lignes `*/10 * * * *` appelant
  `rclone_sync_bidirectionnel*.sh` sont retirées du crontab (sauvegardé
  avant dans `~/.local/state/gdrive-sync/crontab-avant-2026-09-10.txt` —
  il ne contenait rien d'autre) ; les deux scripts sont renommés
  `.sh.desactive-2026-09-10`, contenu intact. Le cron n'a **pas** été
  réparé et aucun `--resync` n'a été lancé : sa panne était protectrice.
  Plus aucun déclencheur automatique ne subsiste (crontab vide, aucun
  timer utilisateur, `/etc/cron.d/` sans rapport, `~/.config/autostart/`
  vide).
- **Passphrase rclone : à changer, geste de Flavien.** Elle apparaît dans
  trois fichiers — les deux scripts désactivés (ligne 2, mode 700) et
  `~/.bash_history` (19 occurrences, mode 600). **Aucun sur Drive, aucun
  suivi par git.** Marche à suivre (`rclone config` → `s` → `c`, puis
  `gdrive-sync set-password`) dans le fichier de session. Rien n'a été
  changé par Claude Code.
- **RECTIFICATIF de l'entrée du 2026-09-10.** L'audit concluait que « la
  sauvegarde annoncée n'est pas prouvée ». **C'était faux.**
  `history.jsonl` porte bien un run `gdrive2` réussi le **07/09 à
  06:48:40**, dont le log `20260907-063855.log` montre les deux blobs
  `Copied (new)` à 06:47:37-38 — et dont le `run_stamp` est exactement le
  dossier `.gdrive-sync-archive/20260907-063855` vu sur le Drive. Un
  `rclone lsl` sur la destination confirme les trois fichiers aux octets
  exacts. Le « 01/09 » de l'audit venait du journal du **cron**
  (`~/.cache/rclone/bisync.log`), pas de celui du moteur : deux sources
  distinctes, conclusion abusive. **Le manifeste de
  `_sauvegardes/chesscom/` disait vrai.**
- Reste : changer la passphrase, puis `gdrive-sync install-units` pour
  retrouver une synchronisation automatique **avec** les garde-fous que le
  cron n'avait pas.

## 2026-09-15 (2) — Unités natives posées mais non armées ; le `.git` de 20 Mo purgé du Drive

Détail dans `_sessions/2026-09-15.md`.

- **PRÉALABLE NON REMPLI, signalé.** Le prompt supposait la passphrase
  rclone déjà changée. Elle ne l'est pas : la valeur du trousseau est
  identique à celle qui traîne en clair dans les deux scripts désactivés
  et dans `~/.bash_history`. `gdrive-sync check` répond « passphrase
  lisible ✓ » précisément parce que rien n'a bougé. Le travail a donc été
  fait **sans rien activer**. **Ne pas armer les timers avant le
  changement.**
- **`gdrive-sync install-units` exécuté** : `gdrive-sync@.service`,
  `gdrive-sync@.timer` et deux drop-ins d'intervalle (30 min pour
  `gdrive2`, 1 h pour `gdrive` — les valeurs de `config.toml`).
  `Persistent=true` et `RandomizedDelaySec` (2 min au gabarit, 300 s /
  600 s aux drop-ins) sont bien présents. **Rien n'est activé** ;
  `Linger=no`, signalé sans y toucher. Effet de bord noté :
  `~/.config/autostart/gdrive-sync-tray.desktop` a été créé — l'icône ne
  déclenche aucune synchro d'elle-même, vérifié dans son code.
- **`~/.local/bin/gdrive-status` écrit** (non lancé) : cinq lignes —
  dernier succès et âge par destination, échecs depuis, retard du clone
  GoogleDrive2 sur `origin/main`, taille des archives, ligne ALERTE.
  Seuils par variables d'environnement.
- **Rétention des archives : le moteur n'en a aucune.** `prune_logs` ne
  couvre que les logs (`log_keep_days = 30`) ; `.gdrive-sync-archive`
  n'est jamais purgé. Aujourd'hui négligeable (un seul dossier,
  `20260907-063855`, rien en local). Commande de purge proposée, **N = 30
  recommandé, à valider par Flavien**. Rien n'a été purgé.
- **`gdrive2:Echecs/Papu-Chess/.git` PURGÉ — 20 181 832 octets, 844
  objets.** Confirmé inerte avant suppression : ses treize refs figées
  existent toutes dans le dépôt vivant et sont toutes joignables depuis
  une ref de `origin` ; son `HEAD` pointait sur `wip-fonds-couleurs`
  quand le clone est sur `wip-sauvegarde-chesscom`. C'était un miroir
  Drive périmé, figé au 12/08 par l'exclusion `**/.git/**`. Le `.git`
  local du clone est intact, le reste du dossier Drive aussi.
- **Les quatre fichiers de `pre-resync-backup/` déplacés**, pas
  supprimés, vers `~/Documents/recuperes-gdrive-sync/` (2,1 Mo,
  horodatages préservés). Documents personnels sans rapport avec les
  échecs, à trier par Flavien ; `~/Documents` est hors périmètre
  synchronisé.

## 2026-09-15 (3) — Passphrase réparée et reliquats effacés ; armement SUSPENDU

Détail dans `_sessions/2026-09-15.md` (entrée de 17:25).

- **RECTIFICATIF : `gdrive-sync check` ne prouve rien.** Il teste que le
  trousseau est lisible, pas que sa valeur déchiffre `rclone.conf` — il
  répondait « lisible ✓ » alors que le moteur était cassé. Le geste a
  deux moitiés (`rclone config` puis `set-password`) qui s'étaient
  désolidarisées le 15/09 ; seules `rclone listremotes` et le mtime de
  `rclone.conf` font foi. Passphrase changée depuis par la voie non
  interactive (`rclone config encryption set --password-command`, appelé
  deux fois dont une avec `RCLONE_PASSWORD_CHANGE=1`), vérifiée dans les
  deux sens, tailles des comptes conformes (10,7 / 6,7 Gio). Ancienne
  valeur effacée partout : sauvegarde `shred`ée, 19 lignes retirées de
  `.bash_history`, ligne 2 des deux scripts neutralisée, **balayage final
  à 0 fichier**.
- **ARMEMENT SUSPENDU.** Le run de contrôle `gdrive2` est pourtant passé
  (133,1 s, `Bisync successful`, aucune suppression malgré huit jours de
  dérive) — mais son unique transfert était `GSYNC_MDP.txt`, déposé à la
  racine de `~/GoogleDrive2`, **donc dans le périmètre synchronisé**, et
  contenant la passphrase neuve. Il est désormais en clair sur Google
  Drive. Timers laissés `disabled`, run `gdrive` non lancé : armer
  re-propagerait ce fichier à chaque passage.
- **À trancher par Flavien** : sortir le fichier du périmètre, supprimer
  la copie Drive et vider la corbeille, considérer la passphrase neuve
  comme exposée et la changer une troisième fois — puis seulement armer.

## 2026-09-15 (4) — Rotation n°3 : l'incident `GSYNC_MDP.txt` et sa leçon

Détail dans `_sessions/2026-09-15.md` (entrée de 17:32).

- **L'incident.** La passphrase de la rotation n°2 avait été déposée dans
  `~/GoogleDrive2/GSYNC_MDP.txt`, **à la racine d'un dossier
  synchronisé** : le run de contrôle de 17:20 l'a téléversée en clair sur
  Drive. Rotation n°3 faite dans la foulée — nouvelle valeur générée et
  posée au trousseau **avant** toute destruction, donc sans fenêtre sans
  passphrase valide. Vérifiée dans les deux sens (le trousseau déchiffre,
  l'ancienne ne déchiffre plus, mtime réécrit, comptes à 10,721 / 6,721
  Gio). Elle n'existe qu'au trousseau, affichée nulle part.
- **Exposée détruite** : fichier local `shred`é, copie Drive supprimée
  définitivement (`--drive-use-trash=false`, pas de passage par la
  corbeille — plutôt que `rclone cleanup`, qui aurait vidé toute la
  corbeille du compte), et une copie inattendue trouvée puis `shred`ée
  dans `~/.config/libreoffice/4/user/backup/`. **Balayage final à 0
  fichier** sur toute la machine. Timers laissés `disabled`.
- **La leçon — un secret ne se dépose jamais dans un dossier
  synchronisé.** Troisième occurrence du même motif sur ce chantier après
  le `client_secret_*.json` et la passphrase des scripts cron.
  **Interdits : `/home/lui/GoogleDrive` et `/home/lui/GoogleDrive2`, tous
  sous-dossiers compris** — rien n'y est à l'abri, l'exclusion ne couvre
  que `.git`, les archives et quelques temporaires. Se méfier aussi des
  sauvegardes d'éditeur, qui recopient ailleurs sans le dire.

## 2026-09-18 — Les archives Drive descendent en local au lieu d'être détruites ; inventaire non versionné de GoogleDrive2/Echecs

Détail complet : `_sessions/2026-09-18.md`, bloc 08:15–08:32.

- **`gdrive-archives-prune` ne détruit plus rien** : un dossier distant
  de plus de N jours est descendu dans `~/Archives-gdrive-sync/<remote>/`
  (`rclone move --drive-use-trash=false`), puis le script contrôle le
  nombre de fichiers, les octets et l'absence sur le Drive. **La purge
  locale est retirée.** La destination est vérifiée hors périmètre
  synchronisé à chaque lancement. Timer quotidien maintenu et descriptions
  reformulées. Nom plus juste proposé, non appliqué :
  `gdrive-archives-rapatrier`.
- **`gdrive2:.gdrive-sync-archive/20260902-181732` descendu** : 9
  fichiers, 1005,1 Kio, absent du Drive, rien dans la corbeille.
  `20260907-063855` reste sur Drive comme copie hors site et descendra
  seul vers le 08/10. Une commande interrompue avait en fait déjà agi :
  **constater avant d'affirmer « rien n'a bougé »**.
- **Inventaire de `~/GoogleDrive2/Echecs`** (rien déplacé) : 142 Mio hors
  dépôt, surtout les médias et transcriptions de Marc Quenehen (92 Mio),
  plus les blobs chesscom et `_rapports/`, ignorés par git dans le dépôt.
  « Analyse » (espace finale) est entièrement contenu dans `Analyse`. Le
  `.mp3` de `_meta/` est un doublon exact de celui de Marc Quenehen.
- **JOURNAL.md et REPRISE.md : Téléchargements fait foi.** La branche de
  GD2 (`wip-sauvegarde-chesscom`) est un ancêtre de
  `wip-reprise-2026-09-10`, avec 9 commits de retard et 0 ligne propre.
- **Pas encore tranché** : l'architecture des deux clones. Mémoire,
  `CLAUDE.md` et exclusions de gdrive-sync sont intacts.

- **Suite de la séance (08:45–09:10)** : commande `sync?` (une phrase,
  d'après le verrou), et progression dans l'applet grâce à `rclone --rc`
  **sur socket Unix**, car un port TCP sans authentification est
  atteignable par n'importe quelle page web. L'applet affiche une barre et
  un pourcentage quand le total est connu, « analyse en cours… » sinon, et
  l'heure du dernier passage réussi au repos. Testé sur des passages
  réels. systemd-inhibit reste en attente de l'arbitrage de Flavien.

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
