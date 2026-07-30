---
id: mauvais-fou
nom: Le mauvais fou
rayons: [Technique, Méthode]
phase: milieu
alias:
  - mauvais fou
  - mauvais-fou
  - bon fou mauvais fou
  - fou de la couleur de ses pions
  - fou enterré
  - fou passif
sources:
  - nature: heritee
    auteur: Marc Quenehen
    video: "Europe Échecs — mini-stratégie « Le mauvais fou »"
    fichier: _doctrine/Mauvais Fou.txt
    timecodes:
      - "1:20–1:32 — définition : blocages de pions → diagonales fermées → bon fou / mauvais fou ; le mauvais fou est celui de la couleur de ses pions"
      - "1:47–2:00 — le bon fou collabore ; pions et fou sur couleurs opposées = équilibre du contrôle des couleurs ; le mauvais fou fait double emploi avec ses pions"
      - "2:12–2:26 — remède : échanger son mauvais fou contre le BON fou adverse"
      - "2:54–3:12 — le mauvais fou laissé à l'adversaire est un fardeau positionnel ; toutes les finales en pâtissent"
    note_provenance: >
      URL et titre exacts de la vidéo non consignés dans le corpus ;
      seul le transcript timecodé est présent (À_COMPLÉTER).
  - nature: elaboree
    auteur: Fonds (arbitrage — Flavien)
    fichier: _fonds/mauvais_fou_definition_proposee.md
    video: null
    timecodes: null
    note_provenance: >
      Document de travail : refonte opérationnelle de la doctrine de
      Marc en critères A/B/C/D. Ni Marc ni Julien — voir la note
      « Tension d'attribution » ci-dessous. Positions de test :
      _fonds/mauvais_fou_fen_test_c8.txt,
      _fonds/mauvais_fou_implementation_resultats.txt.
liens:
  - doctrine-couleur
  - bon-fou
  - francaise-avance
  - finale-fou-contre-cavalier
  - controle-des-couleurs
---

# Le mauvais fou

> Entrée PILOTE (phase 2 de la feuille de route encyclopédie). Écrite
> pour éprouver `_fonds/encyclopedie/FORMAT.md` avant tout lecteur.
> Les frictions rencontrées sont consignées en fin de fichier, section
> « Crash-test du format » — elles sont le vrai livrable de cette phase.

## L'idée, en une phrase

Un fou est *mauvais* quand il vit sur la même couleur de cases que ses
propres pions : il se cogne dedans, son influence est réduite, et il
fait double emploi avec eux au lieu de compléter leur travail.

## Pourquoi ça arrive : les pions ferment la position

C'est un phénomène de STRUCTURE, pas de case isolée. Quand les pions se
bloquent au centre, les diagonales se ferment ; il apparaît alors
presque toujours un bon fou et un mauvais fou. Le mauvais est celui dont
la couleur coïncide avec celle sur laquelle ses pions sont fixés : il ne
peut ni les dépasser ni les défendre utilement. Le bon fou, lui,
travaille sur l'autre couleur et complète les pions — pions et fou se
partagent alors le contrôle des deux couleurs. (Marc, 1:20–2:00.)

## Le remède de Marc : échanger le mauvais contre le bon

Le bon coup n'est pas de garder son mauvais fou en espérant l'activer,
mais de s'en débarrasser en retirant à l'adversaire son BON fou : on
échange notre pièce faible contre sa pièce forte. Laissé sur l'échiquier,
le mauvais fou adverse devient un fardeau positionnel permanent, et toutes
les finales tournent contre son camp. (Marc, 2:12–3:12.)

## Ce que « mauvais » veut dire précisément (élaboration du fonds)

La doctrine de Marc est qualitative. Pour que le Fou puisse *détecter* un
mauvais fou sur un échiquier réel, le fonds l'a refondue en quatre
conditions cumulatives (source interne, cf. note d'attribution) :

- **A — aucune case sûre.** Le fou n'a aucun coup légal qui ne le fasse
  capturer gratuitement (mesure SEE 1 coup).
- **B — étouffement durable par des pions.** Sur au moins deux
  diagonales, le premier obstacle est un pion ami lui-même fixé (sa case
  d'avance est occupée par un pion, ou tenue par un pion adverse). Une
  pièce mobile de passage ne compte pas comme fixation.
- **C — comptage de couleur (le cœur de la doctrine de Marc).** Au moins
  N pions amis (proposé N=3) sont fixés sur des cases de la couleur du
  fou.
- **D — pas d'échappatoire à court terme.** Pousser un pion gêneur
  adjacent — éventuellement pour y relocaliser le fou (motif
  fianchetto) — ne rend pas au fou une mobilité suffisante.

Un fou n'est signalé que si A **et** B **et** C **et** D sont réunies.
Le critère D est ce qui évite de condamner un fou seulement mal placé
mais qui peut respirer au coup suivant.

### Note d'attribution (tension à résoudre — voir crash-test)

Le comptage de couleur (C) vient de Marc ; il ne donne **aucun seuil
chiffré**. N=3 et le seuil de développement sont des choix d'ingénierie
du fonds, sans source doctrinale. La condition A/B/D et tout l'appareil
de calcul sont une **élaboration interne** (arbitrage Flavien), pas une
parole de Marc ni de Julien. C'est pourquoi la deuxième source de
l'en-tête porte `auteur: Fonds` : voir le crash-test, point 1.

## Démonstrations

### Démonstration 1 — Française fermée : le fou c8 enterré

`role: exemple`

Position construite pour isoler le cas proprement (structure française
d'avance fermée, verrou c5/e5). Vérifiée sur la fonction réelle de
`Papu_Chess.html` : `{safe:0, gene:2, colorCount:3, dev:1}` → mauvais fou
confirmé, et le fou blanc c1 (encore chez lui) n'est **pas** signalé.

Position de départ (trait aux Noirs) :

```
FEN: rNb2rk1/pp3ppp/2n1pq2/2PpP3/3P4/5N2/PP3PPP/R1BQK2R b - - 0 12
```

Convention de couleur (comme `demonstrations/nataf_decouverte.pgn`) :
R rouge = pièce condamnée / cible, Y jaune = les pions qui emprisonnent,
G vert = case ou coup de travail. Annotations CUMULATIVES.

**ÉTAPE 1 — les pions clairs qui verrouillent**
`[%csl Yb7,Ye6,Yd5]`
Le Fou : « Regardez les pions noirs : b7, e6, d5 — tous cloués sur des
cases claires. »

**ÉTAPE 2 — + le fou, sur la même couleur**
`[%csl Yb7,Ye6,Yd5,Rc8]`
Le Fou : « Le fou c8 vit sur ces mêmes cases claires que ses pions. Il
fait double emploi avec eux : c'est le mauvais fou. »

**ÉTAPE 3 — + sa seule sortie, déjà gardée**
`[%csl Yb7,Ye6,Yd5,Rc8,Gd7][%cal Rb8d7]`
Le Fou : « Son unique coup, Fd7, tombe sur le cavalier b8 : Fd7, Cxd7 —
le fou meurt avant d'avoir vécu. Zéro case sûre. »

**ÉTAPE 4 — + la tentative d'évasion qui échoue**
`[%csl Yb7,Ye6,Yd5,Rc8,Gd7][%cal Rb8d7,Gb7b6]`
Le Fou : « On essaie de l'aérer par b6 ; mais c5 tient la case, et même
Fb7 ne lui rend que deux cases. Pas d'échappatoire — le verrou tient. »

**ÉTAPE 5 — réinitialisation** (aucune annotation ; l'échiquier redevient
nu, comme l'étape 6 de la démo Nataf).

### Démonstration 2 — La source de Marc : le fou g7 fianchetto — À_COMPLÉTER

`role: exemple`

Marc illustre la doctrine sur un fou g7 fianchetto, bloqué (« papillon
5,6 », h4 et c5), dans une partie de deux grands maîtres néerlandais
(`_doctrine/Mauvais Fou.txt`, 1:24–3:12). **La position n'est pas
reconstructible proprement depuis le transcript** (auto-transcription
trop dégradée pour un FEN légal fiable). À écrire dès que la position
exacte de la vidéo est retrouvée. NB : la définition A/B/D actuelle ne
détecte de toute façon presque jamais un fou fianchetto (voir crash-test,
point 4) — cette démonstration est aussi le contre-exemple qui documente
ce trou.

### Démonstration 3 — Contre-exemple : le fou f8 qui n'est PAS mauvais

`role: contre-exemple`

Partie réelle **kanukmjj – Papu_san**, chess.com, 2026-07-11
(`Analyse/260711_kanukmjj_vs_Papu_san.pgn`,
<https://www.chess.com/game/171412766004>). Un fou f8 resté au repos que
l'**ancien** détecteur (mobilité brute ≤ 4 cases, sans notion de sûreté
ni de couleur) signalait à tort comme mauvais fou — faux positif éliminé
par la définition A/B/C/D (confirmé à l'écran, cf. `JOURNAL.md`). Montrer
ce qui N'EST PAS un mauvais fou est le geste pédagogique du
contre-exemple.

Position au coup 14, **trait aux Noirs** (rejeu vérifié avec le chess.js
0.10.3 du dépôt) :

```
FEN: 2kr1b1r/ppp3pp/8/3p1b2/2Bn2nq/BPN3NP/P1PP1PP1/R3QRK1 b - - 2 14
```

Convention : R rouge = le fou soupçonné, Y jaune = la diagonale qui le
sauve, G vert = cases et coup de travail. Annotations CUMULATIVES.

**ÉTAPE 1 — le soupçon**
`[%csl Rf8]`
Le Fou : « Un fou encore chez lui, en f8. L'ancien réflexe criait au
mauvais fou : au repos, donc enterré. Piège. »

**ÉTAPE 2 — la diagonale est ouverte**
`[%csl Rf8][%cal Yf8a3]`
Le Fou : « Regardez la diagonale f8–a3 : e7 et d6 sont vides. Elle est
grande ouverte — rien n'enferme ce fou. »

**ÉTAPE 3 — les cases réellement disponibles**
`[%csl Rf8,Ge7,Gd6,Gc5,Gb4][%cal Yf8a3]`
Le Fou : « Fe7, Fd6, Fc5, Fb4 : quatre cases sûres d'un coup. Un mauvais
fou n'en a aucune ; celui-ci croule sous les choix. »

**ÉTAPE 4 — le clou : il gagne même une pièce**
`[%csl Rf8,Ga3][%cal Gf8a3]`
Le Fou : « Et il prend au bout : Fxa3, le fou blanc est indéfendu — une
pièce nette. Le "suspect" est en réalité l'agresseur. »

**ÉTAPE 5 — la morale**
`[%csl Ge7,Gd6,Gc5,Gb4,Ga3]`
Le Fou : « Un fou au repos n'est pas un mauvais fou. Ce qui compte, c'est
la couleur de ses pions et une diagonale fermée — ici, ni l'un ni
l'autre. »

**ÉTAPE 6 — réinitialisation** (aucune annotation ; l'échiquier redevient
nu).

### Démonstration 4 — Finale « bon cavalier contre mauvais fou » — À_COMPLÉTER

`role: exemple`

Marc décrit ailleurs (`doctrine_couleur.txt`, ~12:00, autre vidéo) le cas
où l'on joue un bon cavalier posté contre un fou incapable de défendre sa
couleur — « très agréable pour les Blancs ». Matière en prose seulement,
**pas de FEN** ; à écrire quand une position de finale est fixée.

## Crash-test du format (livrable de la phase 2)

Endroits où `FORMAT.md` a coincé, résisté ou manqué. Frictions 1, 2 et 5
**tranchées et appliquées** (FORMAT v2) ; 3 et 4 restent en état légitime
`À_COMPLÉTER`.

1. **[RÉSOLU — FORMAT v2] Attribution des sources non pédagogiques.**
   FORMAT.md posait `sources` avec `auteur : Marc / Julien`. Or cette
   entrée repose *aussi* sur une élaboration interne (critères A/B/C/D,
   seuil N=3) sans auteur externe ni timecode. Résolution : chaque source
   porte désormais une `nature` parmi `heritee` (Marc/Julien) / `externe`
   (autre matériel pédagogique) / `elaboree` (arbitrage interne du fonds,
   Flavien). Ici Marc = `heritee`, le document A/B/C/D = `elaboree`. La
   distinction protège « inspiration, pas imitation ».

2. **[RÉSOLU — FORMAT v2] Syntaxe de l'en-tête.** FORMAT.md ne fixait pas
   la syntaxe (YAML ? liste à puces ?). Résolution : YAML front-matter
   délimité par `---`, entériné dans FORMAT.md avec un exemple complet.
   Cet en-tête s'y conforme.

3. **Champs manquants sur une source réelle.** La vidéo de Marc n'a ni
   URL ni titre exact dans le corpus, seulement le transcript timecodé.
   J'ai mis `note_provenance … À_COMPLÉTER`. Le format gagnerait à
   prévoir explicitement des sources partiellement connues (timecode oui,
   URL non).

4. **Démonstrations sans échiquier.** Deux des quatre démonstrations
   (démos 2 et 4) n'ont **pas de position reconstructible** dans le
   corpus (transcripts en prose, pas de FEN). Le format exige une
   position de départ (FEN ou coups) ; le corpus de Marc, lui, est
   surtout du TRANSCRIT. C'est exactement le risque « asymétrie corpus /
   format » noté dans `RESTE_A_FAIRE.md`. Convention proposée pour le
   lecteur : une démonstration `À_COMPLÉTER` (sans FEN) est licite et
   affichée comme « à venir », l'entrée reste publiable si au moins une
   démonstration est board-complète.

   Sous-cas révélateur, résolu par le rejeu (démo 3) : le PGN visé
   « ounkar6 vs Papu_san » n'existait pas, et la partie réellement
   disponible (kanukmjj) ne portait PAS la leçon supposée (g6/Fg7). Rejeu
   avec le chess.js du dépôt → la vraie leçon (diagonale f8–a3 ouverte,
   Fxa3 gagne une pièce). Leçon de méthode : **ne jamais écrire une
   démonstration sans rejouer la position** ; le format doit être nourri
   de FEN vérifiés, pas de souvenirs de partie.

5. **[RÉSOLU — FORMAT v2] La démo qui NIE l'objet.** La démonstration 3
   (un fou qui n'est PAS mauvais) est pédagogiquement essentielle mais
   n'entrait dans aucune catégorie. Résolution : chaque démonstration
   porte un `role` — `exemple` ou `contre-exemple` — entériné dans
   FORMAT.md. La démo 3 est marquée `contre-exemple`.
