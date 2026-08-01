---
id: echec-a-la-decouverte
nom: L'échec à la découverte
rayons: [Technique, Méthode]
phase: milieu
alias:
  - découverte
  - decouverte
  - échec à la découverte
  - attaque à la découverte
  - attaque découverte
  - coup à la découverte
  - batterie
  - pièce masquante
  - double échec
sources:
  - nature: heritee
    auteur: Marc Quenehen
    video: "« Le Cavalier à l'attaque du Roi ! » — 20 positions d'attaque de mat où le cavalier est déterminant"
    fichier: "Marc Quenehen/Le Cavalier à l'attaque du Roi !/transcript.txt"
    timecodes:
      - "0:32–0:53 — présentation de la position 1 : Igor Nataf avec les Blancs contre un GM que Marc dit ne pas connaître ; les Noirs viennent d'attaquer la dame"
      - "1:14–1:31 — l'idée : on ne bouge PAS la dame attaquée, « les Noirs ont un problème plus important, ils ont leur roi qui est sous le viseur du fou » ; « avec les Blancs on va chercher à bouger le cavalier pour que le fou attaque le roi »"
      - "1:31–1:41 — le coup joué : Ce4 ; « on verra que cavalier e8 marchait également »"
      - "1:41–1:45 — branche de l'interposition : « si la dame vient en e7 ou en f6, bien sûr elle va être attrapée sur échec par le fou » (tout ce que Marc en dit)"
      - "1:48–1:58 — branche du roi : « le roi il n'a qu'une seule case, c'est d'aller en c8 » ; puis Cd6, « ça serait la même chose s'il est en e8 » ; échec et mat"
      - "1:58–2:13 — anatomie du mat : la fourchette du cavalier ; le pion c7 cloué sur la colonne ne peut pas prendre ; la dame contrôle d7 ; le fou contrôle d8 ; « et là la tour »"
      - "4:11–4:43 — position 3 (Widmar avec les Blancs, les Noirs à l'attaque) : Marc NOMME le motif — « le roi est sous le viseur du fou g7 et donc on va faire une attaque à la découverte, c'est-à-dire qu'on va bouger le cavalier ; avec cette découverte du fou ça va dévoiler la diagonale du fou, et le cavalier peut aller en c4 ou en d3, les deux cas sont possibles » ; puis le double échec : « le cavalier et le fou font échec, donc il y a double échec, donc c'est pour ça que le pion blanc ne peut pas prendre le cavalier »"
    note_provenance: >
      Transcription automatique très bruitée (voir la section « Note de
      transcription » en fin d'entrée pour les décodages retenus). Les
      timecodes sont ceux du fichier ; le titre exact et l'URL de la
      vidéo ne sont pas consignés dans le corpus (À_COMPLÉTER).
      La position 3 (4:11–4:43) est ajoutée aux sources héritées bien
      qu'elle sorte de la position Nataf : c'est le SEUL endroit du
      corpus où Marc nomme et définit le motif de vive voix.
  - nature: elaboree
    auteur: Fonds (arbitrage — Flavien)
    fichier: _fonds/demonstrations/nataf_decouverte.pgn
    video: null
    timecodes: null
    note_provenance: >
      Relèvent de l'élaboration interne, et non de Marc : (a) la
      correction du FEN de la position, relevée sur captures vidéo et
      vérifiée par rejeu (pas de pion f5 ; le fou noir est en b7, donc
      c8 est vide) ; (b) la définition générale du motif — batterie,
      pièce masquante, « coup gratuit » — que Marc n'énonce nulle part
      sous cette forme ; (c) dans la branche A, le fait que Fxf6+
      attaque en outre la tour h8 et gagne la qualité en plus de la
      dame ; (d) la méthode de repérage en trois questions ; (e) le
      choix de nommer les branches.
liens:
  - fourchette
  - clouage
  - double-echec
  - deviation
  - batterie
---

# L'échec à la découverte

> Deuxième entrée du format, et **première à variantes ramifiées** : sa
> démonstration embranche vers deux suites nommées, dont l'une
> ré-embranche à son tour. Elle sert de cible au lecteur ramifié
> (phase 3). Les frictions rencontrées sont consignées en fin de
> fichier, section « Crash-test du format — variantes ramifiées ».

## L'idée, en une phrase

Une pièce en masque une autre sur une ligne qui vise le roi adverse :
quand elle s'écarte, l'échec part **de la pièce restée immobile**, et
celle qui a bougé est libre d'aller faire son propre travail ailleurs.

## La batterie : ce qui rend la découverte possible

Une découverte ne s'invente pas au coup par coup, elle se **constate**.
Il faut trois choses alignées, dans cet ordre, sur une même ligne
(colonne, rangée ou diagonale) :

1. une pièce à longue portée — dame, tour ou fou — qui « regarde » la
   ligne ;
2. une pièce à soi posée devant elle, la **pièce masquante**, qui
   intercepte le regard ;
3. le roi adverse au bout.

Cet attelage s'appelle une **batterie**. Tant que le masque est en
place, rien ne se voit : la ligne est neutralisée par une pièce amie, ce
qui est exactement pourquoi on ne la remarque pas. C'est le pire angle
mort du joueur débutant — il cherche des échecs *actifs*, alors que la
découverte est un échec qui existe déjà, éteint, et qu'il suffit de
rallumer.

Dans la position Nataf, la batterie est : **fou h4 — cavalier f6 — roi
d8**, sur la diagonale h4-g5-f6-e7-d8. Marc la fait voir avant tout
autre chose, et c'est le geste de méthode à retenir : « les Noirs ont
leur roi qui est sous le viseur du fou » (1:22).

## Pourquoi c'est si fort : le coup gratuit

L'échec vient de la pièce qui **n'a pas bougé**. La pièce masquante,
elle, n'a aucun devoir : elle peut aller n'importe où, même sur une case
où on peut la prendre, même très loin du roi — l'adversaire n'a pas le
temps de s'en occuper, il doit d'abord parer l'échec.

C'est ce qui donne à la découverte son caractère de **coup gratuit** :
on joue deux coups en un. D'où deux conséquences pratiques :

- **On ne bouge pas ce qui est attaqué.** À 1:14, Marc pose la position
  en désamorçant le premier réflexe : « la dame elle est attaquée
  certes, et pourtant on ne va pas la bouger, on va rester là jusqu'au
  bout ». Une dame en prise n'est pas un problème tant que l'adversaire
  n'a pas le loisir de la prendre. La découverte achète ce loisir.
- **La case d'arrivée du masque est souvent secondaire.** Marc dit deux
  fois la même chose, dans deux positions différentes : ici, « il est
  venu en e4, on verra que cavalier e8 marchait également » (1:35) ;
  et à 4:31, sur la position 3, « le cavalier peut aller en c4 ou en d3,
  les deux cas sont possibles ». Ce n'est pas une approximation de sa
  part : c'est la démonstration même. Ce qui compte, c'est **que la
  diagonale s'ouvre** ; la case choisie n'est qu'un chemin vers la même
  finalité — d'e4 comme d'e8, le cavalier ira mater en d6.

## Le double échec, cas extrême

Quand la pièce masquante donne elle aussi échec en s'écartant, les deux
échecs sont simultanés et le camp attaqué **ne peut plus rien parer** :
on ne peut pas capturer deux pièces en un coup, on ne peut pas
s'interposer contre deux lignes à la fois. Il ne reste que la fuite du
roi. Marc le formule à 4:36 : « le cavalier et le fou font échec, donc
il y a double échec, donc c'est pour ça que le pion blanc ne peut pas
prendre le cavalier ».

La position Nataf n'est **pas** un double échec : Ce4 ne donne pas
échec lui-même, seul le fou attaque. C'est ce qui laisse aux Noirs trois
réponses légales au lieu d'une — et donc c'est précisément ce qui rend
cette position démonstrative, puisqu'il y a des branches à explorer.

## Comment le repérer

Trois questions, dans l'ordre, à chaque fois que le roi adverse est mal
logé :

1. **Une de mes pièces à longue portée regarde-t-elle vers le roi
   adverse ?** Sans se demander encore ce qu'il y a sur le chemin.
2. **Qu'y a-t-il sur le chemin ?** Si c'est une pièce à moi, et une
   seule, j'ai une batterie.
3. **Où cette pièce peut-elle aller ?** Toutes ses cases sont
   candidates, y compris celles qui ont l'air absurdes. On cherche celle
   qui menace le plus — mat, fourchette, prise majeure.

Le signe de reconnaissance de l'exercice, c'est l'ordre inverse de
l'intuition : on ne cherche pas un beau coup pour la pièce qui bouge, on
cherche d'abord la ligne éteinte, et seulement ensuite le beau coup.

## Ce que cette position enseigne en particulier

Trois choses que l'exemple porte mieux que l'énoncé général :

- **La découverte fabrique du forcé.** Après Ce4+, les Noirs n'ont plus
  que trois coups légaux dans toute la position — deux interpositions et
  une case de roi. C'est ce rétrécissement qui rend le calcul possible
  jusqu'au mat : on ne calcule pas un arbre, on épuise une liste.
- **La découverte prépare la fourchette.** Le mat final n'est pas donné
  par le fou de la batterie mais par le cavalier qui l'avait masqué :
  Cd6 est une **fourchette royale**, roi c8 et dame f7 en même temps.
  La découverte a servi à emmener le cavalier là où il fallait, avec
  un tempo gratuit. Deux motifs se relaient — voir [[fourchette]].
- **Le mat tient par les clouages et par les pièces noires elles-mêmes.**
  Le pion c7 ne peut pas prendre le cavalier parce qu'il est cloué sur
  la colonne c par la dame c6 ; la tour b8 et le fou b7 bouchent eux-mêmes
  les deux cases de fuite de leur roi. Voir [[clouage]].

---

## Démonstration — la découverte de Nataf

**Rôle** : `exemple`
**Nature (racine)** : `heritee` — sauf indication contraire portée par une
branche ou une étape.
**Source** : Marc Quenehen, « Le Cavalier à l'attaque du Roi ! »,
position 1, 0:32–2:16. Igor Nataf a les Blancs.
**Trait aux Blancs.**

**FEN** : `1r1k3r/pbp2q2/1pQ2N2/3Pp2p/3P3B/P7/1PP5/1K1R4 w - - 0 1`

> FEN **corrigé** par rapport à la première version de
> `_fonds/demonstrations/nataf_decouverte.pgn`, sur captures vidéo puis
> vérification par rejeu (chess.js 0.10.3, celui de `Papu_Chess.html`) :
> pas de pion noir en f5 ; le fou noir a quitté c8 pour b7, ce qui
> libère c8. Contrôles passés : `Ce4+` légal ; après Ce4+ les Noirs
> n'ont que **trois** coups légaux, `Rc8` `Df6` `De7`, et `Rc8` est la
> seule case du roi ; `Cd6` est **mat**.
> Le pion noir reste en **c7** — voir « Crash-test », friction 1.

```yaml
verification:
  outil: "chess.js 0.10.3 (celui embarqué dans Papu_Chess.html)"
  date: 2026-08-01
  invariants:
    - "Ce4+ est légal et donne échec"
    - "après Ce4+, les Noirs n'ont que trois coups légaux : Rc8, Df6, De7"
    - "Rc8 est le SEUL coup de roi"
    - "Cd6 est mat, zéro échappatoire"
    - "depuis e8 aussi : Ce8+ Rc8 Cd6 est mat"
    - "Ce8+ ne permet PAS Rxe8 (la dame c6 défend e8)"
    - "branche A.1 : Ce4+ De7 Fxe7+ est légal et donne échec"
    - "branche A.2 : Ce4+ Df6 Fxf6+ Rc8 Fxh8 est jouable jusqu'au bout"
    - "sous-branches A.1/A.2 : FEN d'entrée explicite (après 1…De7 /
      1…Df6) contrôlé identique au FEN dérivé par rejeu depuis la
      racine — ajouté phase 3, voir note sous chaque sous-branche"
```

Convention de couleur, reprise de `nataf_decouverte.pgn` et entérinée en
FORMAT v3 : **R** rouge = cible, **Y** jaune = ligne d'attaque, **G**
vert = case ou coup **à l'étude, quel qu'en soit le camp** — y compris
une réponse noire.

### Mise en place — position fixe, annotations cumulatives

Aucun coup n'est joué : seules les annotations changent, chacune
reprenant celles de l'étape précédente.

```
ÉTAPE 1
coup: —
[%csl Rd8]
Le Fou : « Leur roi, en d8, est dans le viseur… »

ÉTAPE 2
coup: —
[%csl Rd8][%cal Yh4d8]
Le Fou : « …du fou h4, le long de la diagonale. Il ne le voit pas
encore : quelque chose est posé devant. »

ÉTAPE 3
coup: —
[%csl Rd8,Gf6][%cal Yh4d8]
Le Fou : « C'est notre propre cavalier, en f6, qui bouche la ligne.
Avec les Blancs, on cherche à le bouger pour ouvrir l'échec. »

ÉTAPE 4
coup: —
[%csl Rd8,Gf6][%cal Yh4d8,Gf6e4]
Le Fou : « Nataf est venu en e4. »

ÉTAPE 5
coup: —
[%csl Rd8,Gf6][%cal Yh4d8,Gf6e4,Gf6e8]
Le Fou : « On verra que cavalier e8 marchait aussi. Peu importe la
case : ce qui compte, c'est que la diagonale s'ouvre. »

ÉTAPE 6 — réinitialisation : aucune annotation, l'échiquier redevient nu.
```

### Le coup

```
ÉTAPE 7
coup: 1. Ce4+
[%csl Rd8][%cal Yh4d8]
Le Fou : « Le cavalier s'écarte, et l'échec part du fou, qui n'a pas
bougé. La dame blanche est toujours en prise en c6 — et alors ? Les
Noirs doivent d'abord répondre à l'échec. »

ÉTAPE 8 — RAMIFICATION
coup: —
[%csl Rd8,Gc8,Ge7,Gf6][%cal Yh4d8]
Le Fou : « Les Noirs n'ont plus que trois coups dans toute la position.
Ou la dame vient s'interposer, en e7 ou en f6 — ou le roi fuit en c8.
Regardons les deux. »
```

> À partir d'ici, la démonstration **embranche**. Chaque branche part de
> la position après 1. Ce4+, redonnée en FEN pour que le lecteur puisse
> l'atteindre sans rejouer la ligne principale.

### Branche A — « La dame s'interpose »

`nature: elaboree` — sauf l'étape A1, `heritee`.
Position de branche : `1r1k3r/pbp2q2/1pQ5/3Pp2p/3PN2B/P7/1PP5/1K1R4 b - - 1 1`
(dérivable par rejeu depuis la racine : identique au FEN obtenu après
1. Ce4+, contrôlé.)

Marc écarte cette branche en trois secondes (1:41–1:45) : « si la dame
vient en e7 ou en f6, bien sûr elle va être attrapée sur échec par le
fou ». Le fonds la développe un cran plus loin, parce qu'elle explique
*pourquoi* le roi est obligé de fuir dans la branche B.

```
ÉTAPE A1
nature: heritee
coup: —
[%csl Rd8][%cal Yh4d8,Gf7e7,Gf7f6]
Le Fou : « Les deux cases marchent pour boucher la diagonale — c'est
tout ce que la dame peut faire. Mais boucher une diagonale avec sa dame
quand un fou la garde, c'est la donner. »
```

> **Corrigé phase 3** : cette étape jouait auparavant `coup: 1… De7 (ou
> 1… Df6)` — deux coups à la fois, ce que la clé `coup:` (F2 de v3)
> interdit. Elle est désormais une étape d'ANNOTATION pure (`coup: —`) :
> elle montre les deux cases candidates sans en jouer aucune. Le coup
> réel est déplacé en tête de chaque sous-branche, avec son propre FEN
> d'entrée explicite (F4 de v3, qui manquait aux deux sous-branches).

Les deux interpositions ne se valent pas. La branche ré-embranche.

#### Sous-branche A.1 — « en e7 »

`nature: elaboree` — sauf sa première étape (le coup de la dame),
`heritee` comme A1 : Marc nomme la case, ce qu'il en dit s'arrête à
« attrapée sur échec par le fou ». Sœur de A.2 : les deux repartent des
annotations de A1, jamais l'une de l'autre.
Position de branche : `1r1k3r/pbp2q2/1pQ5/3Pp2p/3PN2B/P7/1PP5/1K1R4 b - - 1 1`
(identique au FEN de Branche A : la dame n'a pas encore bougé à
l'entrée de cette sous-branche, c'est l'étape A1.1 qui joue le coup.
Dérivable par rejeu depuis la racine : 1. Ce4+, contrôlé.)

```
ÉTAPE A1.1
nature: heritee
coup: 1… De7
[%csl Rd8][%cal Yh4d8,Gf7e7]
Le Fou : « La dame va en e7 — elle bouche la diagonale, mais elle se
met dans la ligne du fou. »

ÉTAPE A1.2
coup: 2. Fxe7+
[%csl Rd8][%cal Gh4e7]
Le Fou : « Le fou la prend, et il la prend AVEC ÉCHEC — les Noirs n'ont
même pas le temps de souffler. »

ÉTAPE A1.3
coup: —
[%csl Rd8,Ge7]
Le Fou : « Les Noirs reprennent le fou (2… Rxe7) ou fuient en c8. Dans
les deux cas les Blancs ont donné un fou et gagné une dame. La partie
est jouée, mais il n'y a pas de mat : c'est pour ça que Marc n'insiste
pas. »

ÉTAPE A1.4 — réinitialisation.
```

#### Sous-branche A.2 — « en f6 »

`nature: elaboree` — sauf sa première étape (le coup de la dame),
`heritee` comme A1. Sœur de A.1 : elle repart de A1, PAS de A1.3.
Position de branche : `1r1k3r/pbp2q2/1pQ5/3Pp2p/3PN2B/P7/1PP5/1K1R4 b - - 1 1`
(identique au FEN de Branche A, même raison qu'en A.1 : c'est l'étape
A2.1 qui joue le coup. Dérivable par rejeu depuis la racine : 1. Ce4+,
contrôlé.)

```
ÉTAPE A2.1
nature: heritee
coup: 1… Df6
[%csl Rd8][%cal Yh4d8,Gf7f6]
Le Fou : « La dame va en f6, même idée. »

ÉTAPE A2.2
coup: 2. Fxf6+
[%csl Rd8][%cal Gh4f6]
Le Fou : « Même prise, avec échec là encore. Mais regarde plus loin sur
la diagonale… »

ÉTAPE A2.3
coup: —
[%csl Rd8,Rh8][%cal Yf6h8]
Le Fou : « …la tour h8 est au bout. Le roi n'a que c8, et après 2… Rc8
le fou se sert : 3. Fxh8. Une dame ET une tour. La deuxième interposition
est encore pire que la première. »

ÉTAPE A2.4 — réinitialisation.
```

> Le prolongement de la sous-branche A.2 (Fxf6+ attaque aussi la tour
> h8) est **élaboré**, pas hérité : Marc ne le dit pas. Vérifié par
> rejeu.
> Nuance sur les deux placements du cavalier : Df6 est légal dans les
> deux cas, mais si le cavalier est allé en **e4**, il garde f6 et les
> Blancs peuvent aussi prendre du cavalier (Cxf6). Fxf6+ reste le
> meilleur coup dans les deux cas — l'échec change tout. L'équivalence
> e4/e8 énoncée par Marc porte sur la **finalité du chemin**, le mat en
> d6, et elle est exacte sur ce plan : vérifiée par rejeu, Cd6 est mat
> depuis l'une comme depuis l'autre.

### Branche B — « Le roi fuit »

`nature: heritee` sur toute la branche — c'est celle que Marc déroule
en entier, mat et anatomie du mat compris.
Position de branche : `1r1k3r/pbp2q2/1pQ5/3Pp2p/3PN2B/P7/1PP5/1K1R4 b - - 1 1`
(même position que la branche A : les deux sœurs repartent de l'étape 8,
et n'héritent rien l'une de l'autre.)

C'est la branche que Marc suit (1:48–2:13), et celle qui finit en mat.

```
ÉTAPE B1
coup: 1… Rc8
[%csl Rc8][%cal Yh4d8]
Le Fou : « Le roi n'a qu'une seule case, c'est c8. d7 et e8 sont à la
dame, e7 est au fou, et le reste est occupé par ses propres pièces. »

ÉTAPE B2
coup: 2. Cd6#
[%csl Rc8,Gd6][%cal Ge4d6]
Le Fou : « Et le cavalier qui avait ouvert la diagonale vient conclure
lui-même. Échec et mat. Depuis e8 c'était exactement pareil : d6 est à
un saut des deux cases. »

ÉTAPE B3 — anatomie du mat
coup: —
[%csl Rc8,Gd6,Yc7,Yd7,Yd8,Yb8,Yb7][%cal Yc6c7]
Le Fou : « Regarde pourquoi il ne s'échappe pas. Le pion c7 pourrait
prendre le cavalier — mais il est CLOUÉ sur la colonne c par la dame c6 :
s'il bouge, c'est le roi qui est en échec. d7 est à la dame, d8 est au
fou h4. Et b8 et b7 ? Ce sont la tour et le fou noirs eux-mêmes qui
bouchent les deux dernières issues de leur roi. »

ÉTAPE B4 — la fourchette
nature: heritee (2:01, « le cavalier fait des fourchettes, il attaque
plusieurs pièces en même temps » — seul le nom « fourchette royale » est
de nous)
coup: —
[%csl Rc8,Rf7,Gd6][%cal Rd6c8,Rd6f7]
Le Fou : « Et note ce que fait le cavalier en arrivant : il attaque le
roi ET la dame en même temps. Une fourchette royale. Ici c'est déjà mat,
donc la dame n'a plus d'importance — mais c'est le même geste qui, dans
une position moins définitive, t'aurait rapporté la dame. »

ÉTAPE B5 — réinitialisation.
```

---

## Note de transcription

Le transcript de la vidéo est une transcription automatique très
dégradée. Décodages retenus pour cette entrée, tous contraints par la
position et vérifiés par rejeu :

| Transcript | Lecture |
|---|---|
| « il fait chaque roi » | il fait échec au roi |
| « le calife » | le cavalier |
| « hors de 4 » | e4 |
| « en de 8 », « cavalier 8 » | e8 |
| « des 6 » | d6 |
| « la dame vient de 7 » | la dame vient en e7 |
| « ou en abscisse » | ou en f6 |
| « le pion c'est 7 » | le pion c7 |
| « la case des 7 » | d7 |
| « la casse des 8 » | d8 |

En revanche « **qu'a fait Granata** » / « café grenata » (1:31) est un
**nom de joueur** — Nataf — et non une déformation de « cavalier ». Ne
pas le corriger en coup.

Un seul point reste non résolu : à 2:13, « et là la tour et le fou[t] un
joli mat ». Vérification faite, la **tour d1 ne participe pas** au mat —
elle est bloquée par son propre pion d4 et ne défend pas le cavalier, qui
n'a d'ailleurs pas besoin d'être défendu. La seule tour qui compte dans
le tableau final est la **tour noire b8**, qui bouche la fuite de son
propre roi. C'est la lecture retenue dans l'étape B3. À confirmer sur la
vidéo (quelle tour Marc désigne-t-il à l'écran ?).

---

## Crash-test du format — variantes ramifiées

Frictions rencontrées en écrivant la première entrée ramifiée. C'était
le livrable de cette entrée pour la phase 3, au même titre que son
contenu. **Les sept ont été entérinées dans `FORMAT.md` v3
(2026-08-01)** ; cette section garde la trace de ce qui les a fait
apparaître, et l'entrée est conforme à v3.

**1 → v3 « Rejeu obligatoire », clé `verification`.** Le FEN
initialement consigné dans `nataf_decouverte.pgn` était faux sur trois
points (pion f5 fantôme, fou en c8 au lieu de b7). La correction
proposée sur captures déplaçait en outre le pion c7 en d7 : elle ne
passait pas le rejeu, `Rc8` restant illégal — la dame c6 tenait la
colonne c dès lors que c7 était vide, et `Ce8+` permettait même `Rxe8`.
Le pion doit rester en **c7** : c'est lui qui bouche la colonne pour
autoriser Rc8, et c'est lui que Marc décrit comme cloué. **Aucun des
trois FEN n'était distinguable à l'œil** dans un fichier texte, et le
troisième ne cassait qu'un coup sur quatre, à trois demi-coups de
profondeur. D'où la règle : toute démonstration est rejouée avant
consignation, et porte ses invariants. Ceux de cette démonstration sont
en tête de la section « Démonstration ».

**2 → v3 clé `coup:`.** Les étapes 1 à 6 ne jouent aucun coup (position
fixe, annotations cumulatives) ; les étapes 7 et suivantes jouent des
coups. Sans marque, un lecteur qui rejoue rejouerait la position à
chaque annotation. Chaque étape porte désormais `coup:` (`—` si aucun).

**3 → v3 règle de cumul à l'embranchement.** « Chaque étape reprend les
`%cal/%csl` de la précédente » est clair en ligne droite, muet à
l'embranchement. Entériné : une branche repart des annotations de
l'étape qui l'a ouverte ; **deux branches sœurs n'héritent jamais l'une
de l'autre** ; chaque branche se termine par une réinitialisation. Ici :
A.1 et A.2 repartent toutes deux de l'étape A1, et A et B toutes deux de
l'étape 8.

**4 → v3 FEN d'entrée de branche.** Chaque branche porte son FEN, en
plus d'être dérivable par rejeu. Redondance voulue : sans elle, une
branche mal recopiée diverge en silence et la démonstration continue de
« marcher » sur autre chose. Les deux FEN de branche de cette entrée ont
été contrôlés identiques au FEN dérivé après 1. Ce4+.

**5 → v3 : trois couleurs, G redéfini.** R = cible, Y = ligne, G = case
ou coup **à l'étude**. Pas de quatrième couleur : à l'étape 8, les trois
réponses NOIRES sont en vert, et c'est correct — G ne désigne pas le
camp qui joue, il désigne ce qu'on regarde.

**6 → v3 clé `nature:` au grain fin.** Sur la branche A, Marc donne
quatre mots (« attrapée sur échec par le fou ») là où une étape jouable
a besoin d'un coup nommé et d'une conclusion. Une entrée ramifiée
fabrique donc de l'`elaboree` par construction : la source suit une
branche et écarte les autres. La `nature` est désormais portable par une
branche ou par une étape. Ici : branche A `elaboree` (sauf A1), branche
B `heritee` de bout en bout.

**7 → v3 : le lien mort est une amorce.** Les cinq `liens` de cette
entrée (`fourchette`, `clouage`, `double-echec`, `deviation`,
`batterie`) pointent tous vers des entrées **inexistantes** — seule
`mauvais-fou` existe, et elle n'a rien à voir avec ce motif ; la lier
aurait été un lien de complaisance. Entériné : le réseau précède les
nœuds, un lien mort s'affiche non cliquable et ne fait échouer aucune
validation.
