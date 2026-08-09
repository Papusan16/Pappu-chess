# Reconnaissance — les coachs d'échecs open-source, et ce qu'ils font de nos notions

*Document de reconnaissance et de synthèse. 2026-08-09. Branche `reco-coachs`.*

---

## Règle de travail, rappelée en tête

**Inspiration des IDÉES, oui. Copie de code, non.** Rien de ce qui suit n'a été
recopié dans Papu-Chess, et rien ne doit l'être. Ce document décrit des
**méthodes** et des **partis pris de conception** ; là où une technique est
nommée, elle l'est comme on nomme une ouverture — un savoir-faire public, pas un
extrait de source.

**Papu-Chess est un mono-fichier HTML sans build.** `Papu_Chess.html` fait
907 913 octets et embarque **chess.js 0.10.3** (licence BSD, mention conservée
en tête du fichier) ainsi que toute la logique de l'application. Une
précision de fait, parce qu'elle pèse sur tout le reste du document :
**Stockfish n'est pas dans le fichier**. Il est chargé en Web Worker depuis
`engine/stockfish-18-lite-single.js` posé à côté du HTML. C'est heureux : le
moteur est sous **GPL-3.0**, et le tenir comme programme séparé qu'on
interroge en UCI est exactement ce qui garde la question de licence propre.
Notre « mono-fichier » est donc, plus exactement, **un fichier d'application +
un moteur en side-car**.

### Licences relevées, dépôt par dépôt

Relevé le 2026-08-09 via l'API GitHub (champ `license.spdx_id`), et par
lecture du fichier `LICENSE` quand le champ était ambigu.

| Dépôt | Licence | Statut pour nous |
|---|---|---|
| `Bist0uille/chess_mentor` | **MIT** (fichier `LICENSE`) | Libre — idées reprenables, code non recopié quand même |
| `Iamsdt/chess` | **AUCUNE LICENCE** | **Le plus fermé de tous.** Tous droits réservés |
| `stefan-kp/chess_tutor` | **GPL-3.0** | **Contaminant** — inspiration seule |
| `KeeghanM/chess-training-app` | **AGPL-3.0** | **Contaminant** — inspiration seule |
| `czbar/ChessForge` | **MIT** | Libre |
| `daxaur/tabia` | **MIT** | Libre |
| `gilbertbrandow/woodpecker` | **MIT** | Libre |
| `Amayyas/ChessTrainer` | **AUCUNE LICENCE** | Tous droits réservés |

Trois remarques que ce tableau ne dit pas tout seul.

**Première.** L'API GitHub classe `chess_mentor` en `NOASSERTION` / « Other »,
mais son fichier `LICENSE` est un **texte MIT standard**, « Copyright (c) 2026
Bist0uille ». L'écart vient probablement d'un détail de formatage que le
détecteur de GitHub n'a pas reconnu. C'est le fichier qui fait foi : **MIT**.

**Deuxième, et c'est la plus importante.** L'absence de licence n'est pas une
permission, c'est **l'inverse**. Un dépôt public sans licence reste sous droit
d'auteur plein : lisible, mais ni réutilisable ni dérivable. `Iamsdt/chess`, le
projet le plus proche du nôtre par l'ambition, est **plus fermé que les deux
projets GPL/AGPL de la liste**. On peut le lire pour comprendre, jamais s'en
servir.

**Troisième.** `chess_mentor` embarque **Lozza** (`static/lozza.js`, moteur JS
pur, **GPL-3.0**) — son auteur le signale lui-même dans son README. Même
configuration que la nôtre : une application librement licenciée qui parle à un
moteur GPL. La séparation moteur/application n'est pas une coquetterie de
juriste, c'est la pratique commune du domaine.

---

## 1. Positionnement — ce qui reste à nous, et ce qu'un autre fait déjà mieux

Le paysage est encombré, mais il l'est **d'une seule idée**, répétée : prendre
Stockfish, lui demander le meilleur coup, mesurer l'écart avec le coup joué, et
faire raconter cet écart par un LLM. `Iamsdt/chess` le fait, `stefan-kp` le
fait, `Amayyas` le fait. Les trois sont, à la structure près, le même logiciel.
Leur différenciation se joue sur l'emballage — modes de jeu, classement en
ligne, choix du modèle — pas sur la façon de comprendre une position.

### Ce qu'aucun d'eux ne fait

**Le Fou comme personnage, et un seul.** C'est la démarque la plus nette, et
elle est structurelle, pas cosmétique. Partout ailleurs, le coach est **une
fonction** : un texte produit à la demande sur la position courante, jetable,
sans mémoire ni doctrine. `stefan-kp` va jusqu'à proposer un **choix de
personnalités** (les captures d'écran du dépôt montrent un « professional
coach » parmi d'autres) — c'est-à-dire l'aveu que la voix est un paramètre
d'affichage. Chez nous la voix est **antérieure** au logiciel : elle vient de la
tradition Quenehen/Song, elle a une doctrine écrite (`_doctrine/`,
`doctrine_couleur.txt`), des principes qui la contraignent (`PRINCIPES.md`), et
le code n'a pas le droit de lui faire dire ce que la doctrine ne dit pas. Aucun
de ces projets n'a d'équivalent, et pour une raison simple : **ils n'ont pas de
source**. Ils ont un modèle de langage.

**L'encyclopédie-porte.** Chez les autres, le contenu pédagogique est soit
absent (tout est généré), soit un **catalogue plat**. `Iamsdt/chess` a
`public/tutorial/*.json` — une trentaine de fichiers, un par thème
(`discovered-attack.json`, `back-rank-mate.json`, `deflection.json`,
`interference.json`…). C'est une bibliothèque de leçons, pas un réseau : rien ne
relie `discovered-attack` à `double-attack`, et une entrée ne s'ouvre pas sur
une autre. Notre encyclopédie a des `liens`, des `alias`, des `remplace`, et
surtout la règle entérinée que **le réseau précède les nœuds** — un lien mort
s'affiche non cliquable et ne fait échouer aucune validation. C'est ce qui fait
d'une entrée une *porte* et non une *fiche*.

**Le miroir motif ↔ mat.** Personne ne fait ça, et personne n'en a l'occasion.
Le principe — la même matière servant deux fois, une fois côté motif
(`echec-a-la-decouverte`, qui s'arrête sur `cloture: pause` et ne joue pas le
mat) et une fois côté conclusion (`top-mats-nataf`, à écrire) — suppose que le
contenu soit **écrit et versionné**, donc rejouable à l'identique dans deux
contextes. Un contenu généré à la volée ne peut pas se mettre en miroir avec
lui-même : il n'est jamais deux fois le même. Notre discipline de canonicité est
la condition de possibilité du miroir.

**Le mono-fichier.** `daxaur/tabia` est le seul à partager notre exigence
d'autonomie — « browser-local, no account, no server », et il la tient. Mais il
la tient à un coût qu'on ne paierait pas : il **renonce au moteur**. Son
`src/eval.js` s'annonce lui-même « engine-free » et calcule une évaluation
heuristique (matériel + mobilité + développement + centre + sécurité du roi)
pour faire bouger la barre « honnêtement et instantanément ». C'est un choix
défendable pour un entraîneur d'ouvertures, intenable pour un précepteur qui
doit certifier qu'un mat est un mat. **Nous sommes seuls à tenir les deux bouts :
autonomie du fichier ET vérité du moteur.**

### Là où nous faisons la même chose qu'un autre — et où il fait mieux

Il faut le dire nettement, parce que c'est le vrai enseignement de cette
reconnaissance.

**`Bist0uille/chess_mentor` a eu notre idée, et l'a poussée plus loin que nous
sur un point précis.** Son pitch — « apprend à RAISONNER », « signaux faibles »,
« le pourquoi de chaque coup », « indices progressifs » — c'est notre programme
mot pour mot. Et son architecture pose une frontière que nous n'avons pas
formalisée aussi clairement :

> les détecteurs déterministes sont la **vérité-terrain**, le LLM n'a le droit
> que de **narrer** ce qu'ils ont établi.

Cette phrase est en tête de son `signal_detectors.py`, et elle est tenue
jusqu'au bout : un **garde-fou rejette tout texte du modèle citant un coup
absent des lignes vérifiées par le moteur**, avec repli sur un compte rendu
déterministe. C'est plus rigoureux que « on demande au modèle d'être prudent ».
C'est une **contrainte vérifiée à l'exécution**, pas une consigne de prompt.

Nous appliquons de fait le même principe — le Fou ne dit que ce que le code a
établi — mais nous le tenons par **discipline d'écriture**, parce que nos textes
sont rédigés à la main et versionnés. Tant que le Fou ne parle pas par LLM, la
différence est théorique. Le jour où une phrase sera générée, il faudra ce
garde-fou, et `chess_mentor` montre exactement où le poser : **entre le
détecteur et la phrase, pas dans le prompt.**

Deux réserves qui nous rendent la main. `chess_mentor` **n'est pas autonome** :
FastAPI, base SQLite de puzzles Lichess pré-analysée hors ligne par Stockfish,
narration par appel à Claude, déploiement Vercel. Il lui faut un serveur, une
clé d'API et un réseau. Et ses puzzles viennent de Lichess : il **explique des
positions**, il ne transmet pas une doctrine. Le Fou n'a pas de base de
puzzles — il a une bibliothèque et un point de vue.

**Sur l'entraînement structuré, `czbar/ChessForge` nous dépasse largement**, et
c'est sans appel : 25 étoiles, MIT, une application C#/WPF mature bâtie sur des
*workbooks* PGN avec mode entraînement, détection de bourdes, barre et courbe
d'évaluation, évaluation de parties en lot. Là où nous avons un lecteur d'étapes
qui vient d'être validé à l'écran, il a un atelier complet. Ce n'est pas notre
axe — nous ne construisons pas un outil de travail pour joueur avancé, nous
construisons un précepteur — mais il ne faut pas se raconter qu'on fait mieux.

---

## 2. Comment ces projets déterminent une notion échiquéenne

C'est le cœur de la reconnaissance. La question posée était : heuristiques
codées à la main *(a)*, interrogation du moteur *(b)*, ou délégation à un LLM
*(c)* ? La réponse d'ensemble est nette et un peu contre-intuitive :

> **Personne ne délègue la nomination d'une notion à un LLM.** Aucun des projets
> examinés ne demande au modèle « quelle notion vois-tu ici ». Tous nomment la
> notion par du code, et n'utilisent le modèle que pour **mettre en mots** une
> notion déjà nommée. La méthode (c) pure n'existe dans aucun de ces dépôts.

C'est la confirmation la plus utile de tout ce travail : **notre parti pris —
détecter par le code, faire parler le Fou ensuite — est le parti pris commun des
gens sérieux du domaine.** Nous ne sommes pas en retard sur une mode LLM ; nous
sommes sur la ligne que tout le monde tient.

Le vrai clivage est ailleurs : entre *(a)* et *(b)*, et surtout **sur la
localisation du calcul**.

### `chess_mentor` — heuristiques pures *(a)*, côté serveur, en Python

Le cas le plus instructif, parce que le plus explicite. `app/signal_detectors.py`
est un module de ~200 lignes qui produit des objets `Signal` typés — un
identifiant machine (`hanging`, `king_box`, `back_rank`, `alignment`, `checks`,
`double_attack`), une **sévérité de 1 à 3**, la liste des **cases concernées**,
et une phrase courte en français. Quatre familles de détecteurs :

- **Pièce non défendue / sous-défendue.** Pour chaque pièce adverse, il compare
  l'ensemble des attaquants et l'ensemble des défenseurs. Sans défenseur → signal
  fort. Avec défenseurs, il regarde si **son attaquant le moins cher vaut moins
  que la cible** *et* s'il y a plus d'attaquants que de défenseurs → « sous-défendu ».
  C'est un SEE du pauvre, à un demi-coup, exactement de la profondeur de notre
  réflexe M1.
- **Sécurité du roi.** Cases de fuite = cases adjacentes au roi adverse, non
  occupées par une pièce amie **et non contrôlées par nous**. Zéro fuite → sévérité
  3 ; une seule → sévérité 2, avec la case nommée. Plus une détection de dernier
  rang (roi sur sa rangée de départ, mur de pions devant).
- **Alignements.** Pour chaque pièce adverse alignée avec son roi sur une ligne
  **dégagée**, il émet un signal « clouage ou enfilade potentiels », en nommant la
  nature de la ligne (colonne, rangée, diagonale). Sévérité 1, et il **n'en garde
  que deux** — « on garde les plus parlants ».
- **Coups forçants.** Il parcourt tous les coups légaux, retient ceux qui donnent
  échec, et pour la double attaque : il **joue le coup**, regarde ce que la pièce
  déplacée attaque depuis sa case d'arrivée, compte les cibles de valeur ≥ 3 ou le
  roi, et si elles sont deux ou plus, c'est une fourchette. Il **dépile** ensuite.

Tout cela repose sur les primitives de `python-chess` : `board.attackers(color,
square)` qui rend **l'ensemble** des attaquants (donc le compte est gratuit),
`board.is_attacked_by(color, square)`, `board.attacks(square)`, et pour les
alignements `chess.ray()` et `chess.between()`. **Aucun appel au moteur** dans ce
module, aucun appel réseau. Du calcul pur sur la position.

Le moteur intervient **ailleurs et en amont** : `scripts/analyze_db.py` passe
Stockfish en multi-PV 4 profondeur 16 sur toute la base de puzzles, **hors
ligne**, et stocke candidats, évaluations et lignes de réfutation dans une
colonne SQLite. À l'exécution, plus aucun calcul moteur côté serveur : on lit la
base. Le moteur sert alors à **renforcer** un indice — « c'est le SEUL coup qui
gagne », quand Stockfish le certifie. Et un second moteur, Lozza, tourne **dans
le navigateur** pour la barre d'évaluation et pour réfuter les mauvais essais du
joueur, « 100 % côté client : aucun coût serveur, aucun token ».

Architecture, donc : **heuristiques déterministes pour nommer, moteur pré-calculé
pour certifier, moteur client pour réfuter, LLM pour narrer sous garde-fou.**
Quatre couches, chacune à sa place. C'est le dépôt le mieux pensé du lot.

### `Iamsdt/chess` — heuristiques *(a)* côté client + moteur *(b)*, LLM narrateur

Le plus proche de nous par les contraintes : tout tourne dans le navigateur,
Stockfish 18 lite en WASM (`public/stockfish-18-lite-single.wasm`, ~7,3 Mo —
exactement notre moteur, au fichier près).

La détermination des notions est **hybride et scindée en deux fichiers**.
`src/lib/analyzer.js` fait le **moteur pur** *(b)* : il rejoue la partie, demande
à Stockfish une évaluation à chaque coup, normalise le score du point de vue des
Blancs, et classe le coup joué par **centipions perdus** contre le meilleur coup
— une échelle à six crans, de « Brilliant » (≤ 15 cp) à « Blunder » (> 300 cp).
C'est de la qualité de coup, pas de la notion.

Les **notions**, elles, sont dans `src/lib/intelligence.js`, en heuristiques
main *(a)* : `findHangingPieces`, `detectFork`, `detectPinsAndSkewers`,
`getAttackedSquares`, `isSquareAttackedBy`. Et c'est là qu'il faut regarder de
près, parce que **la façon dont il s'y prend est précisément le piège qui nous
guette**.

chess.js n'expose pas de primitive « cette case est-elle attaquée ». Le projet
la reconstruit donc à la main : pour savoir si une case est attaquée par une
couleur, il balaie les 64 cases, et pour chaque pièce de cette couleur il demande
`moves({square, verbose:true})` puis regarde si la case cible figure parmi les
destinations. **Ça ne peut pas marcher, et pour deux raisons cumulées.**

D'abord, **chess.js ne génère les coups que du camp au trait**. Interroger
`moves({square})` sur une pièce du camp qui n'est pas au trait rend une liste
**vide**. Le projet appelle sa fonction pour les deux couleurs sur le même objet
de jeu : l'une des deux interrogations est donc systématiquement muette.

Ensuite, et c'est plus profond : **une pièce qui en défend une autre n'a pas de
coup légal vers elle.** On ne capture pas sa propre pièce, donc la génération de
coups ne produira jamais ce lien. Chercher les défenseurs par `moves()` est une
impasse de principe, pas un réglage à ajuster. Le commentaire du fichier
mentionne d'ailleurs un « captures of own pieces hack » — mais le code visible ne
le met pas en œuvre.

Conséquence : leur `findHangingPieces` teste « attaquée ? » puis « défendue ? »
avec la même fonction défaillante, et la seconde question répond toujours non.
**Toute pièce attaquée y est déclarée en prise.** Sur un coach qui doit dire au
joueur « ta pièce est en prise », c'est un défaut qui parle beaucoup au joueur, et
souvent à tort.

Je le rapporte sans sévérité : c'est un projet à 16 étoiles fait pour apprendre,
et l'erreur est exactement celle que la documentation de chess.js invite à
commettre. **Mais elle est notre meilleur avertissement**, et elle commande toute
la section 3.

### `stefan-kp/chess_tutor` — heuristiques *(a)* filtrées par le moteur *(b)*

GPL-3.0 : idées seulement, et je m'en suis tenu aux **documents de conception**
du dépôt (`TACTIC_RECOGNITION_ANALYSIS.md`, `docs/tactic-detection-requirements.md`),
qui sont explicites et se lisent comme un compte rendu d'ingénierie honnête.

Son module `tacticDetection.ts` couvre clouage, fourchette, enfilade, échec,
pièce en prise, gain de matériel — en **heuristiques chess.js**, mais avec une
idée que les autres n'ont pas : la détection est **déclenchée et cadrée par le
moteur**. La fonction reçoit la position, le coup du joueur, **le meilleur coup
UCI de Stockfish** et la **perte en centipions**, et cherche la tactique **que le
joueur a manquée**. La notion n'est pas cherchée dans l'absolu ; elle est cherchée
*là où le moteur dit qu'il y avait quelque chose à voir*. Le document insiste sur
le caractère **conservateur** de la détection — vérifier qu'une pièce capturée ne
peut pas être reprise avant de crier au gain — et compte cette prudence parmi les
points forts.

Le document est aussi remarquable par ce qu'il avoue : le module **n'est pas
branché sur le LLM temps réel** (les tactiques détectées ne sont utilisées qu'en
analyse d'après-partie), il n'a **aucun test**, et un seuil de 200 cp y est jugé
« arbitraire ». C'est un rapport d'auto-évaluation qui refuse de se déclarer
prêt. La discipline nous est familière.

### Les autres

**`daxaur/tabia`** (MIT) : heuristiques *(a)* pures et assumées, **sans moteur du
tout**. Son `eval.js` additionne matériel, développement des pièces mineures
hors case de départ, pions au centre, roi ayant quitté sa case, et une
**différence de mobilité** obtenue en comptant `moves().length` pour chaque camp.
Son « coach » (`coach.js`) n'est pas un analyseur : c'est un jeu de **messages à
trous, configurables par l'utilisateur et stockés dans le navigateur**. La voix
y est littéralement une préférence.

**`KeeghanM/chess-training-app`** (AGPL-3.0, contaminant, survolé de loin) : son
`tactics-finder` est un outil Python **hors ligne** qui moissonne des positions
tactiques à partir d'évaluations Stockfish — méthode *(b)*, en traitement par
lot, avec un type `Evaluation` qui sait comparer proprement un mat et un score en
centipions. La notion n'y est pas nommée en direct : elle est **extraite en
amont** et servie ensuite en répétition espacée.

**`czbar/ChessForge`** (MIT, C#) : moteur *(b)* de bout en bout — détection de
bourdes, barre et courbe d'évaluation, évaluation de parties en lot. Pas de
détecteur de notion positionnelle repéré ; l'intelligence y est dans
l'organisation du travail (workbooks PGN, mode entraînement), pas dans la
reconnaissance de motifs.

### Récapitulatif

| Projet | Méthode | Où ça calcule | Nomme la notion |
|---|---|---|---|
| `chess_mentor` | **(a)** + (b) en amont | serveur Python ; moteur client pour réfuter | le code, toujours |
| `Iamsdt/chess` | **(a)** + (b) | 100 % client | le code (mais défaillant sur les défenseurs) |
| `stefan-kp` | **(a)** cadrée par **(b)** | client, moteur local ou distant | le code |
| `tabia` | **(a)** seule | 100 % client, aucun moteur | pas de notion, des messages |
| `KeeghanM` | **(b)** | hors ligne, par lot | extraction en amont |
| `ChessForge` | **(b)** | client lourd | pas de notion positionnelle |
| **Papu-Chess** | **(a)** doctrinale + (b) | 100 % client, moteur en side-car | le code, sous doctrine écrite |

---

## 3. Ce que ça implique pour la grammaire de couleurs

Rappel de la cible : le **fond** d'une case doit encoder un état échiquéen
**déterminé automatiquement** — menacée (orangé), libre (vert), désignée (bleu),
échec. Contrainte : mono-fichier, chess.js + Stockfish côté client, pas de
serveur.

### La méthode : heuristiques déterministes, côté client, sans moteur

La réponse est sans hésitation : **méthode (a), calcul local, à chaque
changement de position.** Trois raisons.

**Le moteur ne sait pas répondre à la question.** Stockfish rend un score et une
ligne principale. Il ne rend pas « e5 est attaquée deux fois et défendue deux
fois ». Cette information existe dans ses entrailles mais n'est pas exposée en
UCI. Passer par le moteur pour colorer une case, ce serait déduire un fait
géométrique d'un jugement stratégique — un détour qui ne rend même pas la bonne
information.

**Le coût est incompatible avec un fond de case.** Un fond se recalcule à chaque
demi-coup, à chaque survol, à chaque étape d'une démonstration. Une interrogation
moteur coûte des dizaines à des centaines de millisecondes ; un balayage de 64
cases en chess.js coûte moins d'une milliseconde. `chess_mentor` a tranché
pareil, et son argument est le bon : ses détecteurs sont **la vérité-terrain**
justement parce qu'ils sont **immédiats et déterministes**.

**Et surtout : la même position doit donner la même couleur, toujours.** Un fond
de case est un élément de **langue**, au même titre que `R = cible` ou
`Y = ligne` dans FORMAT. Un moteur ne garantit pas la reproductibilité (la
profondeur atteinte dépend de la charge machine), un LLM encore moins. Si le
même diagramme se colore différemment d'une session à l'autre, la grammaire
ne veut plus rien dire. **Le déterminisme n'est pas ici une optimisation, c'est
une condition de sens.**

Le moteur garde son rôle — certifier, réfuter, évaluer. Il n'a pas à colorer.

### chess.js expose-t-il de quoi savoir qu'une case est attaquée ?

**Notre chess.js, non.** Vérifié en extrayant le module du mono-fichier et en
listant son API publique :

```
BISHOP BLACK FLAGS KING KNIGHT PAWN QUEEN ROOK SQUARES WHITE ascii board clear
fen game_over get header history in_check in_checkmate in_draw in_stalemate
in_threefold_repetition insufficient_material load load_pgn move moves perft
pgn put remove reset square_color turn undo validate_fen
```

Ni `attackers`, ni `isAttacked`. La 0.10.3 possède bien une fonction interne
`attacked(color, square)` — elle est à la ligne 744 du fichier — mais elle est
**enfermée dans le closure** et n'est jamais rendue publique : nos huit
occurrences de `attacked(` sont toutes internes à chess.js, appelées pour la
légalité du roque et de l'échec. Elle rend d'ailleurs un **booléen**, pas un
compte : elle ne suffirait pas à dire « attaquée deux fois ».

**Les chess.js modernes, oui.** La branche 1.x expose
`attackers(square, [color])` qui rend **la liste des cases** d'où part une
attaque — donc le compte gratuitement — et `isAttacked(square, color)` qui rend
un booléen. C'est exactement la primitive de `python-chess` dont `chess_mentor`
tire tous ses détecteurs. **Migrer chess.js serait la solution propre**, et c'est
la première chose à mettre en balance : un remplacement de bibliothèque dans un
mono-fichier, avec une API qui a changé (`in_check` → `isCheck`, etc.), contre
une trentaine de lignes à écrire nous-mêmes. Ce n'est pas une décision à prendre
dans un document de reconnaissance ; c'est une décision à prendre en sachant
qu'elle existe.

### L'idée à reprendre, sans appel externe

Elle est chez `tabia` et chez nous, et elle consiste à **fabriquer la question
dans la FEN plutôt qu'à la poser à la bibliothèque**.

Puisque chess.js ne génère que les coups du camp au trait, on **récrit le champ
de trait dans la FEN** avant d'interroger, et on lit les captures qui visent la
case. Papu-Chess le fait déjà — `safeMobility` fait exactement ça pour forcer le
trait et interroger un fou (`parts[1]=color`). Ça donne les **attaquants**.

Pour les **défenseurs**, la génération de coups est structurellement aveugle : on
ne capture pas sa propre pièce. Le contournement est de **substituer un leurre
adverse** sur la case, puis de compter les captures qui la visent. Vérifié sur
notre chess.js : sur une position où le pion e5 est attaqué par `pd6` et `nc6` et
défendu par `d4` et `Nf3`, la méthode naïve trouve **2 attaquants et 0
défenseurs** ; la méthode par substitution trouve **2 et 2**. C'est le compte
juste, et il coûte deux constructions d'objet `Chess` par case.

**C'est là que se joue la différence avec `Iamsdt/chess` :** eux se sont arrêtés
au constat que « chess.js n'expose pas isAttacked » et ont bâti dessus un
détecteur qui déclare toute pièce attaquée en prise. La grammaire de couleurs ne
peut pas se permettre ça — « menacée » est précisément la couleur qui doit
distinguer *attaquée* de *attaquée et mal défendue*.

### Une trouvaille non prévue, sur notre propre code

Le banc d'essai a mis au jour un défaut réel dans `safeMobility`
(`Papu_Chess.html:3599`). **Je ne l'ai pas corrigé — la consigne était de ne pas
toucher au fichier.** Je le consigne ici.

`safeMobility` force le trait en récrivant `parts[1]`, **mais laisse le champ de
prise en passant intact**. Or une FEN dont le champ *en passant* est renseigné
devient illégale dès qu'on change le trait — la case de prise ne correspond plus
à la dernière poussée. Et chess.js 0.10.3 ne se contente pas de refuser : son
`load()` **vide l'échiquier avant de valider**, si bien qu'une FEN invalide ne
lève rien du tout et laisse un **échiquier vide** sur lequel `moves()` rend
sereinement zéro coup.

Démontré sur une copie fidèle de la fonction. Les Blancs jouent e2-e4 (champ
*en passant* = `e3`), le trait passe aux Noirs ; on interroge un fou blanc en g2,
sain et mobile sur la grande diagonale :

```
  safeMobility ACTUELLE (ep laissé en place) : 0
  safeMobility + ep neutralisé               : 2

  critère A du mauvais fou = « mobilité sûre NULLE » :
   → version actuelle  : A SATISFAIT (le fou est candidat « mauvais fou »)
   → version corrigée  : A NON satisfait (le fou est sain, ce qui est correct)
```

Portée exacte, sans dramatiser. Le critère A est une **porte** :
`if(safeCount>0) continue;`. Le défaut ne peut donc qu'**ajouter** des candidats,
jamais en retirer — aucun vrai mauvais fou n'est manqué. Et le signalement
demande encore B, C et D. Mais il rend le critère A **muet dès que l'adversaire
vient de pousser un pion de deux cases**, ce qui arrive à chaque ouverture, et
c'est très exactement la sorte de faux positif que la doctrine du mauvais fou
s'est donné tant de mal à écarter.

Le correctif tient en une affectation — neutraliser le champ *en passant* en même
temps que le trait, comme `tabia` le fait dans son `flipTurn` avec le commentaire
« drop en-passant so the position stays legal after the swap ». **C'est l'idée la
plus directement utile de toute cette reconnaissance**, et elle vient du projet le
plus modeste de la liste.

Deux conséquences pour la grammaire de couleurs, à retenir avant d'écrire la
première ligne :

1. **Toute FEN forcée doit neutraliser le champ *en passant*.** À poser comme
   règle du helper d'interrogation, une fois, pour que la question ne se
   repose jamais.
2. **Ne jamais faire confiance à un `new Chess(fen)` silencieux.** Sur FEN
   invalide, on n'obtient pas une erreur, on obtient un échiquier vide — donc
   « aucune menace », donc **une case peinte en vert alors qu'elle est brûlante**.
   Pour une grammaire où le fond dit le fait, c'est le mode de défaillance le
   plus dangereux qui soit : il ment dans le sens rassurant. Le helper doit
   vérifier que la position s'est bien chargée avant de conclure quoi que ce soit.

---

## 4. Pédagogie — ce qui éclaire le Fou, l'École et Top mats

**Voix : personnage unique contre personnalités.** Le paysage se partage en
trois. `stefan-kp` propose un **choix de personnalités** de coach ; `tabia` va
plus loin et rend les messages **éditables par l'utilisateur**, stockés dans le
navigateur ; `chess_mentor` et `Iamsdt` n'ont pas de personnage du tout, juste un
registre de langue. Aucun n'a de voix qui **précède** le logiciel. Ce n'est pas
une négligence : une voix n'a de tenue que si elle a une source, et leur source
est un modèle de langage, c'est-à-dire personne. Le Fou tient parce qu'il vient
de quelque part. **Conclusion pour nous : la voix unique n'est pas une limitation
à assumer, c'est le seul actif que personne ne peut copier.**

**Gestion de l'erreur.** Trois régimes, du plus pauvre au plus riche. Le plus
répandu — `Iamsdt`, `analyzer.js` — est **l'étiquette** : on classe le coup en
six crans selon les centipions perdus, avec emoji et couleur. C'est un verdict,
et ça n'apprend rien : le joueur sait qu'il a mal joué, pas pourquoi.
`stefan-kp` fait mieux en cherchant **la tactique manquée** là où le moteur
signale la perte — l'erreur devient une occasion de nommer un motif. Mais le
régime le plus intéressant est celui de `chess_mentor` : le moteur client
**réfute ton essai en le jouant** — « après ton coup, l'adversaire joue … et tu
es perdant ». L'erreur n'est ni notée ni nommée : **elle est jouée jusqu'à ce
qu'elle fasse mal**. Pour l'École, c'est la piste la plus proche de ce que fait
un précepteur devant un échiquier, et notre lecteur d'étapes — qui sait déjà
rejouer une ligne — en est techniquement très près.

**Indices progressifs.** `chess_mentor` a la mécanique la plus aboutie et vaut
d'être décrite précisément. Quatre indices, **dérivés de la solution** par un
annotateur déterministe (`explain.py`) qui analyse la ligne coup par coup —
échec, capture, sacrifice, coup forcé, interposition, motif — et n'appelle
**aucun LLM** pour ça : « tout est vérifié sur l'échiquier — aucune invention
possible ». Les signaux détectés portent une **sévérité de 1 à 3** qui sert à les
ordonner, du plus discret au plus fort. Et il **limite volontairement** ce qu'il
montre : deux alignements au maximum, « on garde les plus parlants ».

Cette dernière discipline est celle qui nous concerne le plus directement, et
pas seulement pour les indices. **Une grammaire de couleurs qui colore tout ne
dit rien.** Si les huit cases menacées d'une position s'allument en orangé, le
fond cesse d'être un signe et redevient du décor. `chess_mentor` a résolu le
problème en donnant à chaque signal une sévérité et en n'affichant que le haut du
tri. La question « combien de cases a-t-on le droit de colorer à la fois »
mérite d'être posée avant l'implémentation, et non après — elle est de même
nature que la règle F5 qui interdit une quatrième couleur.

**Structure des exercices.** `chess_mentor` déroule *signaux → indices 1→3 →
solution → raisonnement du GM*, ce dernier étage étant explicitement un
**raisonnement**, pas une réponse : *ce que je regarde d'abord → les candidats et
pourquoi les écarter → le plan*. C'est très exactement la forme dont Top mats a
besoin, et elle valide au passage notre `cloture: pause` : **s'arrêter sur une
question est une étape pédagogique, pas une troncature.** `KeeghanM` apporte
l'idée orthogonale de la **répétition espacée sur les positions ratées** —
pertinente pour l'École quand elle aura un historique, hors sujet tant qu'elle
n'en a pas.

**Ce qu'aucun ne fait, et qui reste notre terrain.** Aucun de ces projets
n'enseigne une **doctrine**. Ils enseignent des motifs — fourchette, clouage,
dernier rang — c'est-à-dire ce que le code sait détecter. Personne n'essaie de
transmettre une manière de voir, comme la doctrine des couleurs de Marc. C'est
plus difficile, moins démontrable, et c'est précisément pour ça que ça vaut la
peine : **un motif se détecte, une doctrine se transmet.** La grammaire de
couleurs est le premier endroit où notre application tentera de faire dire à la
machine quelque chose d'une doctrine plutôt que d'un motif. Rien de ce que j'ai
lu ne nous aidera à le faire — mais rien non plus ne l'a tenté.

---

## Annexe — méthode et traçabilité

**Consulté en lecture seule**, le 2026-08-09, via l'API GitHub authentifiée et
`github.com/topics/chess-trainer` : `Bist0uille/chess_mentor` (README,
`signal_detectors.py`, `explain.py`, `LICENSE`, arborescence),
`Iamsdt/chess` (`intelligence.js`, `analyzer.js`, arborescence),
`stefan-kp/chess_tutor` (`TACTIC_RECOGNITION_ANALYSIS.md`, arborescence — **GPL,
documents de conception uniquement**), `daxaur/tabia` (`eval.js`, `coach.js`),
`KeeghanM/chess-training-app` (`evaluation.py` — **AGPL, survol**),
`czbar/ChessForge` (arborescence), plus le relevé de licence de
`gilbertbrandow/woodpecker` et `Amayyas/ChessTrainer`.

**Le coach français** demandé en priorité est **`Bist0uille/chess_mentor`**,
identifié par sa description au topic `chess-trainer` : « ♟️ Coach d'échecs qui
apprend à RAISONNER : repère les signaux faibles d'une position et explique le
pourquoi de chaque coup (indices progressifs, moteur dans le navigateur).
FastAPI + données Lichess + narration Claude. » 0 étoile, MIT, dernier envoi
2026-07-02. C'est le dépôt le plus proche de notre intention et le mieux
architecturé du lot.

**Banc d'essai.** Trois sondes jetables, écrites dans un scratchpad hors projet
et **non versionnées**, servant à vérifier par l'exécution plutôt que par la
lecture : extraction du chess.js embarqué pour lister son API publique réelle ;
comptage attaquants/défenseurs par forçage du trait et par substitution d'un
leurre ; reproduction du faux positif de `safeMobility` sur une copie fidèle de
la fonction. `Papu_Chess.html` n'a **pas** été modifié, ni lu autrement qu'en
lecture.

**Reste ouvert, pour décision.** Trois points que ce document pose sans
trancher : (1) migrer vers un chess.js 1.x pour disposer de `attackers()`, ou
écrire nos propres helpers sur la 0.10.3 ; (2) corriger le champ *en passant*
dans `safeMobility` — défaut réel, démontré, non corrigé ici ; (3) fixer une
règle de parcimonie pour le fond de case, c'est-à-dire combien de cases la
grammaire s'autorise à colorer simultanément.
