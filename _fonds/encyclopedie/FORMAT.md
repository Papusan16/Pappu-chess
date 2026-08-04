# Format d'une entrée d'encyclopédie

**Version 4** — 2026-08-04. Entérine ce que la phase 4 a mis EN SERVICE
sans l'avoir encore écrit ici : deux clés d'en-tête (`remplace`,
`onglet`), la syntaxe de lien `[[id]]`, la règle de rendu d'un lien-amorce,
la règle « démo non parsable ⇒ la prose s'affiche quand même », et les
conventions de prose que le lecteur d'étapes lit réellement — restées
implicites depuis la phase 3. Les nouveautés portent une marque `[v4]`.
Principe de cette version : **le format rattrape le code**. Aucune clé
inventée ici ; tout ce qui suit tourne déjà dans `Papu_Chess.html`.
Historique : v1 = format posé (phase 1) ; v2 = crash-test linéaire de
l'entrée pilote `mauvais-fou` (phase 2) ; v3 = crash-test ramifié ;
**v4 = mise en conformité avec la porte unique (overlay 📚)**.

Clé de voûte du régime CONSULTATION (cf. `_fonds/moteur_du_fou.md`). Le
lecteur d'étapes le LIRA, l'arbitrage le REMPLIRA. Une entrée = un objet
du savoir échiquéen, expliqué puis démontré.

---

## Principe directeur : enveloppe stable, contenu ouvert

Peu de structure obligatoire, beaucoup de liberté à l'intérieur. Les
attributs d'en-tête sont STABLES (la machine doit retrouver l'entrée) ;
l'EXPLICATION est LIBRE. Conformément à `moteur_du_fou.md` : la liste des
angles n'est jamais figée en champs obligatoires — c'est l'arbitrage qui
décide de la découpe, selon l'objet et ce que les sources en disent.
Conséquence assumée : aucune entrée ne ressemblera exactement à une
autre, et l'affichage doit tolérer cette hétérogénéité.

## Fichier

Un fichier par entrée, dans `_fonds/encyclopedie/`, nommé d'après
l'identifiant (`caro-kann.md`, `avant-poste.md`, `morphy.md`). Format :
Markdown avec en-tête **YAML front-matter** (attributs machine-lisibles
en tête, explication en prose Markdown ensuite). Un fichier par entrée
pour faciliter l'écriture à la main, la relecture, le diff par entrée, et
un service par API plus tard.

Syntaxe de l'en-tête (entérinée) : un bloc **YAML délimité par `---`**,
en tout début de fichier, avant le premier titre Markdown. Toutes les
entrées s'y conforment (sinon deux entrées auraient des en-têtes de forme
différente, illisibles par la machine). Exemple d'en-tête complet :

```yaml
---
id: mauvais-fou
nom: Le mauvais fou
rayons: [Technique, Méthode]
phase: milieu
alias:
  - mauvais fou
  - fou de la couleur de ses pions
sources:
  - nature: heritee
    auteur: Marc Quenehen
    video: "Europe Échecs — mini-stratégie « Le mauvais fou »"
    fichier: _doctrine/Mauvais Fou.txt
    timecodes:
      - "1:20–1:32 — définition"
  - nature: elaboree
    auteur: Fonds (arbitrage — Flavien)
    fichier: _fonds/mauvais_fou_definition_proposee.md
liens:
  - bon-fou
  - francaise-avance
---
```

## En-tête (attributs stables)

- **id** : identifiant unique, minuscule, sans espace.
- **nom** : libellé affiché (« Défense Caro-Kann »).
- **rayons** : un ou PLUSIEURS parmi Histoire / Théorie / Technique /
  Pratique / Méthode (un objet peut relever de deux rayons).
- **phase** (optionnel, transversal) : ouverture / milieu / finale.
- **alias** : liste de formes sous lesquelles l'utilisateur peut
  interroger l'entrée (« caro kann », « défense caro-kann »,
  « 1.e4 c6 »). Sert à la recherche de la consultation.
- **sources** : LISTE — multi-sources par conception (cf.
  `PRINCIPES.md`), aucune entrée ne suppose une source unique. Chaque
  source porte une **nature** parmi trois, plus l'auteur, et selon la
  nature une vidéo + timecode ou un fichier :
  - `heritee` — Marc Quenehen ou Julien Song, le socle pédagogique du
    Fou (vidéo + timecode).
  - `externe` — autre matériel pédagogique (cours, livre, article)
    utilisé comme appui.
  - `elaboree` — élaboration interne du fonds, arbitrée par Flavien
    (ex. les critères A/B/C/D du mauvais fou, le seuil N=3 sans source
    doctrinale).

  Une entrée peut mêler les trois natures. Cette distinction protège la
  règle « inspiration, pas imitation » (cf. `PRINCIPES.md`) en séparant
  nettement ce qui vient de Marc/Julien de ce qui vient de l'arbitrage
  propre au projet.
- **liens** : liste d'id d'autres entrées (la Caro-Kann renvoie à
  `mauvais-fou`, `francaise`, `caro`). C'est ce qui fait de
  l'encyclopédie un RÉSEAU et non une liste : le Fou peut dire « ça
  rejoint ce qu'on a vu sur… ».

  **[v3] Un lien vers une entrée inexistante est une AMORCE assumée, pas
  une erreur.** Le réseau PRÉCÈDE les nœuds : une entrée sait de quoi
  elle est voisine avant que le voisin soit écrit, et cette liste est
  précisément ce qui dit à l'arbitrage quoi rédiger ensuite. Interdire
  le lien mort obligerait soit à n'écrire que des liens vers l'existant
  — donc à laisser le savoir non déclaré —, soit à des liens de
  complaisance vers la seule entrée disponible. Les deux sont pires.
  **Conséquence pour l'affichage** : un lien dont la cible n'existe pas
  se rend NON CLIQUABLE (et non masqué, ni signalé comme erreur) — il
  reste visible comme promesse. Aucune validation ne doit échouer sur
  un lien mort.

- **[v4] remplace** (optionnel) : liste d'ids de **fiches courtes en dur**
  de `Papu_Chess.html` (`ENC.*`, `OPS`, `PEOPLE`) que cette entrée PÉRIME.
  Quand l'entrée se charge, la fiche nommée cède sa place dans la liste ;
  si l'entrée est indisponible (fichier absent, illisible), la fiche
  revient d'elle-même.

  C'est la **clause de cohabitation rendue exécutable**, et elle va dans
  ce sens-là exprès : **c'est le fichier neuf qui déclare ce qu'il
  annule**, jamais l'inverse. Aucune retouche du bloc de données de
  l'application, et l'effacement reste réversible.

  Deux règles d'usage :
  1. **Rien ne s'efface qui n'ait été absorbé.** Avant d'écrire
     `remplace:`, vérifier que TOUT ce que disait la fiche courte
     (`short`, `full`, `signal`, `ex`) se retrouve dans l'entrée. Une
     migration ne doit jamais perdre de texte.
  2. Un id qui ne correspond à aucune fiche en dur n'efface rien et ne
     casse rien — mais `generer_index.py` le signale.

- **[v4] onglet** (optionnel) : où le joueur va CHERCHER cette entrée dans
  l'overlay. Vocabulaire **fermé** : `tactics`, `strategy`, `openings`,
  `endgames`, `method`, `history`, `practice`. Une valeur hors liste est
  ignorée, pas obéie.

  **Ce n'est pas une seconde classification.** Le modèle a deux niveaux :
  - le **rayon** (`rayons:`) est la classification de FOND, portée par
    l'entrée, lue par le moteur ;
  - l'**onglet** est une vue de NAVIGATION, dérivée par l'application à
    partir du premier rayon et de la phase :

    | premier rayon | phase | onglet |
    |---|---|---|
    | Histoire | — | history |
    | Pratique | — | practice |
    | Méthode | — | method |
    | Théorie | ouverture | openings |
    | Théorie | milieu / finale / absente | strategy |
    | Technique | finale | endgames |
    | Technique | ouverture / milieu / absente | tactics |

  `onglet:` est une **DÉROGATION à cette table**, à n'écrire que
  lorsqu'elle se trompe. Elle ne décrit rien de l'objet, elle range — et
  **le moteur n'a pas le droit de la lire**. Le partage
  Tactiques/Stratégie est le seul que les rayons ne tranchent pas
  (`echec-a-la-decouverte` et `mauvais-fou` portent le même
  `[Technique, Méthode]` / `milieu`, l'une est tactique, l'autre
  stratégique) : c'est là qu'elle sert. Le jour où beaucoup d'entrées la
  portent, c'est la table qui est à revoir — pas un dérapage silencieux.

  Cas où elle est nécessaire, et pas seulement confortable : quand
  l'entrée **périme une fiche vivant dans un autre onglet** que celui où
  la table la range, le joueur la perdrait de vue.
  `generer_index.py` le détecte et nomme la clé à écrire.

## Explication (libre)

Une suite de SECTIONS LIBREMENT TITRÉES, autant qu'il en faut, dans
l'ordre qui convient à l'objet. Chaque section = un titre + du texte.
Exemples d'agencements possibles, à titre PUREMENT INDICATIF et NON
NORMATIF : une ouverture pourra avoir « l'idée », « les plans », « le
piège classique » ; une finale « la règle », « la méthode », « le cas
limite » ; une figure « qui c'était », « son apport », « sa partie
célèbre ». Ces exemples ne sont PAS des champs à reproduire.

### [v4] Lier depuis la prose : la syntaxe `[[id]]`

Dans le texte, **`[[id]]`** renvoie à une autre entrée ou à une fiche en
dur. Variante avec libellé : **`[[id|texte affiché]]`**. La syntaxe était
déjà employée dans les entrées avant d'être écrite ici ; elle est
entérinée, pas inventée.

Résolution, dans cet ordre : **entrée riche** (y compris atteinte par l'id
de la fiche qu'elle périme) → **fiche en dur** → **amorce**. Une entrée
riche prime toujours sur la fiche qu'elle remplace, sinon un lien
ramènerait au contenu périmé.

**Rendu d'une amorce** (cible pas encore écrite) : **visible, grisée,
NON CLIQUABLE**, sans handler — mêmes règles que pour le champ `liens`
ci-dessus, appliquées au grain du mot. Ni masquée, ni soulignée en rouge,
ni comptée comme erreur.

Deux compléments à connaître :

- **Auto-liage.** Les noms cités en toutes lettres deviennent cliquables
  d'eux-mêmes quand une cible existe (le nom ou un alias d'une entrée, le
  nom d'une fiche). Une seule occurrence par section, jamais vers l'entrée
  courante, jamais dans les titres. **Il ne révèle que ce qui existe** :
  un nom sans entrée reste du texte nu, et deviendra cliquable tout seul
  le jour où l'entrée sera écrite.
- **Quand écrire `[[id]]` explicitement** : quand la forme est trop
  courte ou trop générique pour être auto-liée sans faux positifs
  (« batterie », « échec », « centre » — un texte d'échecs les emploie à
  tout bout de champ), ou quand on veut l'amorce VISIBLE dès maintenant,
  pour dire « ce nom mérite une entrée ».

## Démonstration(s)

Une liste (souvent une, parfois plusieurs) de séquences jouables. Chaque
séquence :

- un **rôle** parmi `exemple` (l'objet est présent — on le montre) ou
  `contre-exemple` (l'objet n'est PAS là — on montre ce qui n'en est
  pas un). Montrer ce qu'une notion n'est PAS est un geste pédagogique
  de premier ordre (cf. le fou f8 développable, qui n'est pas un mauvais
  fou) ;
- une position de départ (FEN, ou coups depuis la position initiale) ;
- une suite d'ÉTAPES annotées, chacune avec ses annotations `%cal`/`%csl`
  cumulatives et le texte que le Fou dit (même patron que
  `demonstrations/nataf_decouverte.pgn`) ;
- une clé **`verification`** — voir « Rejeu obligatoire » ci-dessous ;
- possibilité qu'une étape RAMIFIE vers des variantes NOMMÉES, chaque
  variante redevenant elle-même une suite d'étapes → structure
  RÉCURSIVE, extensible à n'importe quelle profondeur. C'est ce que le
  lecteur ramifié (phase 3) doit savoir lire.

### [v3] Rejeu obligatoire : la clé `verification`

**Aucune démonstration n'est consignée sans avoir été REJOUÉE.** Ce
n'est pas une recommandation de prudence, c'est une règle : sur la seule
position Nataf, TROIS FEN successifs se sont révélés faux — un pion
fantôme, une pièce sur la mauvaise case, puis un pion glissé d'une
colonne — et **aucun des trois ne se voyait à l'œil** dans un fichier
texte. Le dernier était même plausible : il ne cassait qu'un coup sur
quatre, à trois demi-coups de profondeur. Une démonstration fausse est
pire qu'une démonstration absente, parce qu'elle enseigne.

Chaque démonstration porte donc une clé `verification` : la liste des
INVARIANTS qui doivent tenir au rejeu. On y écrit ce qui, si ça cédait,
ferait s'effondrer la démonstration — pas la liste des coups.

```yaml
verification:
  outil: "chess.js 0.10.3 (celui embarqué dans Papu_Chess.html)"
  date: 2026-08-01
  invariants:
    - "Ce4+ est légal et donne échec"
    - "après Ce4+, les Noirs n'ont que trois coups légaux : Rc8, Df6, De7"
    - "Rc8 est le SEUL coup de roi"
    - "Cd6 est mat"
    - "depuis e8 aussi : Ce8+ Rc8 Cd6 est mat"
```

Trois genres d'invariants méritent presque toujours d'y figurer : la
**légalité** du coup clé, l'**unicité** (« seule case », « seule
défense » — c'est ce qui fait tenir un raisonnement de forçage), et la
**terminaison** (mat, gain de matériel). Chaque fois qu'une étape dit au
lecteur « il n'a que ça », un invariant doit le garantir.

### [v3] La clé `coup` : deux régimes d'étape

Une étape relève de l'un de deux régimes, et le lecteur doit savoir
lequel sans le deviner :

- **étape d'annotation** — la position ne bouge PAS, seules les
  annotations changent, cumulativement. C'est le régime de la mise en
  place : on montre une batterie, une structure, une faiblesse, avant
  que rien ne soit joué ;
- **étape de coup** — un coup est joué, la position change.

Chaque étape porte donc une clé **`coup:`**, avec le coup en notation
algébrique, ou **`—`** si l'étape ne joue rien. Sans elle, un lecteur
qui rejoue la partie rejouerait la position à chaque annotation, et un
lecteur qui ne rejoue pas manquerait les coups.

### [v3] Cumul des annotations : la règle à l'embranchement

En ligne droite, la règle est déjà posée : chaque étape REPREND les
`%cal`/`%csl` de la précédente et y ajoute, jusqu'à une étape de
réinitialisation explicite. À l'embranchement, elle est ambiguë. Elle se
lit désormais ainsi :

1. une branche repart des annotations de **l'étape qui l'a ouverte**
   (l'étape de ramification), et cumule à partir de là ;
2. **deux branches sœurs n'héritent JAMAIS l'une de l'autre.** Ce sont
   des alternatives, pas une suite : la branche B ne s'ajoute pas à la
   branche A, elle la remplace. Le lecteur qui passe d'une sœur à
   l'autre doit revenir à l'état de l'étape de ramification ;
3. chaque branche se termine par une **réinitialisation**, pour que la
   sortie de branche soit propre quel que soit le chemin pris.

La règle vaut à toute profondeur : deux sous-branches sont sœurs entre
elles exactement comme deux branches.

### [v3] Position d'entrée de branche : redondance assumée

Toute branche porte un **FEN d'entrée explicite**, EN PLUS d'être
dérivable en rejouant les coups depuis la racine. C'est une redondance,
et elle est voulue : elle est là contre la **divergence silencieuse**.
Une branche mal recopiée, ou un coup mal noté en amont, produit sans
elle une position fausse que rien ne signale — la démonstration
continue de « marcher », sur autre chose. Avec les deux, le désaccord
entre le FEN annoncé et le FEN dérivé est détectable mécaniquement, et
c'est une erreur à faire remonter.

Bénéfice second : chaque branche devient atteignable et vérifiable
isolément, sans rejouer la ligne principale.

### [v3] Convention de couleur : trois couleurs, pas quatre

- **R** rouge = la **cible** (le roi visé, la pièce à gagner, la case
  faible) ;
- **Y** jaune = la **ligne d'attaque** (diagonale, colonne, rangée qui
  porte la menace) ;
- **G** vert = la **case ou le coup À L'ÉTUDE**.

Pas de quatrième couleur pour l'adversaire. **G désigne le coup examiné,
QUEL QU'EN SOIT LE CAMP** — y compris une réponse adverse, y compris un
coup qu'on va réfuter. Ce n'est pas « le coup de notre camp », c'est
« ce qu'on est en train de regarder ». Trois couleurs restent lisibles
sur un échiquier ; quatre commencent à demander une légende, et la
distinction ami/ennemi est déjà portée par les pièces elles-mêmes.

### [v3] La clé `nature` au grain fin

En en-tête, la `nature` (`heritee` / `externe` / `elaboree`) est portée
par la SOURCE. C'est insuffisant dès qu'une démonstration ramifie.

Raison structurelle, pas accidentelle : **la source s'arrête avant le
fonds.** Un pédagogue en vidéo suit une branche jusqu'au bout et écarte
les autres d'une phrase — sur `echec-a-la-decouverte`, Marc consacre
quatre mots à toute une branche. Une entrée ramifiée doit donc combler
les branches délaissées par élaboration interne. Une entrée à branches
PRODUIT de l'`elaboree` par construction, et il faut pouvoir dire
lesquelles.

Une clé **`nature:`** peut donc être portée par une **branche** (elle
vaut alors pour toutes ses étapes, sauf redéfinition) ou par une
**étape** isolée. Absente, elle est héritée du parent, et à la racine de
la nature dominante des sources. C'est ce qui permet au Fou de dire
honnêtement « ça, c'est Marc » et « ça, c'est nous qui l'avons poussé
plus loin » — la règle « inspiration, pas imitation » de `PRINCIPES.md`
appliquée au grain de l'étape.

### [v4] Conventions de prose que le lecteur lit réellement

Restées implicites depuis la phase 3, alors que le lecteur en dépend
littéralement. Une entrée qui s'en écarte reste lisible, mais ses
démonstrations ne se déroulent pas (c'est le cas de `mauvais-fou`,
écrite en v2). Elles sont donc **normatives pour la partie démonstration**
— et elles seules ; l'explication reste libre.

- **Section de démonstration** : un titre de niveau 2,
  `## Démonstration — <titre>`. La position de départ se déclare dans le
  corps par une ligne `**FEN** : ` suivie du FEN entre accents graves.
  Les invariants vont dans un bloc de code ```yaml``` (clé
  `verification:`, cf. v3).
- **Branche** : un titre de niveau 3 ou 4,
  `### Branche A — « La dame s'interpose »`, ou
  `#### Sous-branche A.1 — « en e7 »`. Le NIVEAU du titre fait
  l'imbrication : une sous-branche est un cran plus bas que sa branche.
  Le FEN d'entrée obligatoire (v3) se déclare par une ligne
  `Position de branche : ` suivie du FEN entre accents graves.
- **Étapes** : dans un **bloc de code** (délimité par trois accents
  graves), un paragraphe par étape, séparés par une ligne vide. Chaque
  paragraphe commence par `ÉTAPE <id>`, éventuellement suivi de
  `— <libellé>`, puis, dans cet ordre, les lignes facultatives :
  `nature: …`, `coup: …` (ou `coup: —`, cf. v3), la ligne d'annotations
  `[%csl …][%cal …]`, et enfin ce que dit le Fou, sous la forme
  `Le Fou : « … »`, sur autant de lignes qu'il faut.
- Une étape dont le libellé contient **« réinitialisation »** est traitée
  comme une remise à zéro des annotations : elle ne porte pas de `coup:`.

Deux conséquences à garder en tête en écrivant :

1. Ce qui n'est pas dans un bloc de code n'est **jamais** lu comme une
   étape — la prose autour d'une démonstration (justification d'un FEN,
   note de transcription) ne risque donc rien.
2. Le titre d'une branche doit commencer par `Branche` ou
   `Sous-branche` : c'est à ça qu'elle se reconnaît.

### [v4] Dégradation : une démonstration illisible n'emporte pas la prose

Règle d'affichage, non négociable : **si le lecteur ne sait pas lire une
démonstration, l'entrée s'affiche quand même.** La prose est rendue
normalement, et la démonstration concernée est remplacée par une mention
disant qu'elle n'est pas jouable en l'état. Idem à l'échelle de l'entrée :
manifeste absent, fichier introuvable, Markdown illisible → la **fiche
courte en dur reprend sa place**, sans écran vide ni message d'erreur
technique.

Formulé autrement : le format peut avancer plus vite que le lecteur, et le
lecteur plus vite que les entrées. **Aucun des trois ne doit pouvoir
casser l'affichage des deux autres.**

## Cohabitation avec l'existant

Le format nouveau COHABITE avec les structures existantes (fiches OPS
dans `Papu_Chess.html`, `repertoire_C.md`, `personnes.md`, doctrine du
mauvais fou). Migration PROGRESSIVE au fil de l'eau, pas de migration en
bloc : la phase 1 ne doit pas se transformer en chantier de migration
avant que le format ait été éprouvé par l'entrée pilote (phase 2).

**[v4] La cohabitation est désormais MÉCANIQUE**, et non plus seulement
une intention : l'overlay 📚 est la porte unique, il sert l'entrée riche
quand elle existe et la fiche courte sinon. La migration se fait **une
entrée à la fois**, par la clé `remplace:` — jamais en lot.

Le manifeste `INDEX.json`, régénéré par `generer_index.py` depuis les
front-matter, n'est qu'un **cache d'affichage** : il dit quelles entrées
existent, sans être la vérité (le fichier `.md` l'est). Un manifeste
périmé fait au pire apparaître un doublon dans la liste ; il ne fait
jamais perdre un contenu. À régénérer après toute création d'entrée ou
toute modification de `remplace:` / `onglet:`.
