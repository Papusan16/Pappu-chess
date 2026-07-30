# Format d'une entrée d'encyclopédie

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

## Explication (libre)

Une suite de SECTIONS LIBREMENT TITRÉES, autant qu'il en faut, dans
l'ordre qui convient à l'objet. Chaque section = un titre + du texte.
Exemples d'agencements possibles, à titre PUREMENT INDICATIF et NON
NORMATIF : une ouverture pourra avoir « l'idée », « les plans », « le
piège classique » ; une finale « la règle », « la méthode », « le cas
limite » ; une figure « qui c'était », « son apport », « sa partie
célèbre ». Ces exemples ne sont PAS des champs à reproduire.

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
- possibilité qu'une étape RAMIFIE vers des variantes NOMMÉES, chaque
  variante redevenant elle-même une suite d'étapes → structure
  RÉCURSIVE, extensible à n'importe quelle profondeur. C'est ce que le
  lecteur ramifié (phase 3) doit savoir lire.

## Cohabitation avec l'existant

Le format nouveau COHABITE avec les structures existantes (fiches OPS
dans `Papu_Chess.html`, `repertoire_C.md`, `personnes.md`, doctrine du
mauvais fou). Migration PROGRESSIVE au fil de l'eau, pas de migration en
bloc : la phase 1 ne doit pas se transformer en chantier de migration
avant que le format ait été éprouvé par l'entrée pilote (phase 2).
