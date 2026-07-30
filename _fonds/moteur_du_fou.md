# Le moteur du Fou — architecture des réflexes et démonstrations

Contrat de conception : comment le Fou choisit ce qu'il dit et comment il
le dit. Le fonds de réflexes (cinq rayons : Histoire, Théorie, Technique,
Pratique, Méthode — cf. `reflexes_methode.md` pour le rayon Méthode) est
la DONNÉE ; ce document décrit le MOTEUR qui l'exploite. Donnée séparée
du code (cf. `PRINCIPES.md`). Le détecteur de mauvais fou
(`fouBadBishopSquares` + `fouBadBishopMsg`) est le premier réflexe câblé
de bout en bout — il sert de modèle au patron « détecter + dire la bonne
chose selon le contexte ».

---

## La fiche d'un réflexe

Champs : identifiant (lettre du rayon + numéro, ex. M1) ; rayon
(Histoire/Théorie/Technique/Pratique/Méthode) ; phase optionnelle et
transversale (ouverture/milieu/finale) ; thème ; TYPE DE DÉCLENCHEUR et
sa CONDITION ; message ; source (vidéo + timecode, pour la fidélité au
fonds Marc).

## Cinq types de déclencheurs

- **structure** : configuration calculable de la position (mauvais fou,
  avant-poste, pion passé, pat imminent, tactique latente). Fonction
  booléenne sur l'échiquier. Seul type câblé aujourd'hui.
- **événement** : un moment du jeu (avant de bouger une pièce → M4
  déprotection ; après une faute repérée par le moteur ; au moment
  d'une promotion).
- **motif** : reconnaissance d'un schéma tactique nommé (mat de Légal,
  découverte, sacrifice de déviation).
- **contexte** : signal non-positionnel — nom d'ouverture (déjà détecté
  via l'encyclopédie ECO), joueur nommé dans le PGN, phase atteinte.
  C'est ce type qui fait passer le Fou de « nomme l'ouverture » à
  « enseigne le plan de l'ouverture » et à « raconte l'histoire du
  joueur/de l'ouverture » (source `personnes.md`).
- **général** : pas de déclenchement automatique fiable (prophylaxie,
  méfiance des principes dogmatiques). Ne s'affiche pas seul → vit sur
  demande (« Idée du prof ») ou dans un exercice d'École construit
  exprès.

## Trois régimes du Fou

- **COMMENTAIRE** (flux : pendant qu'on joue ou navigue) : le Fou dit
  UNE chose, la plus pertinente, pour ne pas noyer. Gouvernance :
  sélection par priorité (sécurité/pièce en prise > tactique disponible
  > faiblesse structurelle > plan d'ouverture > culturel/anecdote),
  anti-répétition (mémoire courte : ne pas re-servir un réflexe
  récent), gating par niveau (chaque réflexe porte une fourchette Elo
  d'utilité).
- **DÉMONSTRATION** (position riche, plusieurs idées contingentes de
  variantes) : le Fou ne choisit plus, il DÉROULE — variante A avec ses
  flèches, retour, variante B, comparaison ; calcul ET positionnement.
  Réutilise et étend la mécanique des démonstrations à étapes (cf.
  `demonstrations/nataf_decouverte.pgn`), les étapes pouvant se
  RAMIFIER en variantes. Le passage commentaire→démonstration se fait
  quand la position dépasse un seuil de richesse (seuil à définir plus
  tard).
- **CONSULTATION** — le Fou comme ENCYCLOPÉDIE VIVANTE. Déclencheur :
  l'utilisateur interroge le Fou (le déclencheur vient de lui, pas du
  jeu). Portée : n'importe quel objet du savoir échiquéen, dans les
  cinq rayons — ouverture, structure, finale, tactique, principe
  stratégique, figure historique, question de jeu pratique, etc. La
  liste des objets n'est pas fermée.
  - Pour chaque objet, le Fou en donne une EXPLICATION COMPLÈTE puis
    la DÉMONTRE sur l'échiquier. « Complète » = ce qu'un excellent
    professeur jugerait nécessaire de dire sur ce sujet précis : sa
    nature, le pourquoi du comment, ses forces et avantages, ses
    faiblesses et écueils, ses plans, son histoire — la liste des
    angles n'est PAS fixée d'avance et ne doit jamais être figée en
    champs obligatoires. Elle dépend de l'objet et de ce que les
    sources en disent.
  - Principe directeur : l'encyclopédie n'est rien d'autre que le
    fonds des cinq rayons rendu interrogeable. Ce que le Fou sait = le
    fonds ; comment on le lui demande = la consultation. Une seule
    mécanique (question → recherche de l'entrée → explication +
    démonstration), cinq rayons de contenu, un nombre indéfini
    d'entrées.
  - Conséquence sur la valeur : la mécanique est simple ; la richesse
    de l'app tient à la QUANTITÉ et à la JUSTESSE des entrées
    arbitrées. Chaque arbitrage déjà fait (réflexes M1-M4, doctrine du
    mauvais fou, fiches repertoire_C, personnes.md) est déjà une
    future entrée de cette encyclopédie.
  - Distinction avec l'onglet École : l'École TESTE (« mets en pause,
    que joues-tu ? »), la consultation RENSEIGNE (« explique-moi »).

## Trois postures (habillent le même réflexe)

Le même réflexe se formule différemment selon la posture : joueur
(prospectif : « avant de jouer, as-tu regardé tous les échecs ? »),
lecteur/analyse (rétrospectif : « ici, un balayage échecs→prises→menaces
trouvait le coup »), élève/École (interrogatif : « mets en pause — quel
échec gagne ? »).

## Statut

Contrat de conception, pas encore implémenté. Le mauvais fou est le seul
réflexe câblé (type structure, régime commentaire). Prochaines briques :
généraliser le patron mauvais-fou à un moteur de sélection ; câbler un
premier réflexe de type contexte (nom d'ouverture → plan) pour sortir le
Fou du simple nommage d'ouverture.
