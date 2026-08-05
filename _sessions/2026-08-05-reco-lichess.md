# Reconnaissance Lichess — ce qu'on en retient pour l'École

**2026-08-05.** Travail de lecture et de synthèse, séparé du chantier
`wip-demo-jouable`. Aucune ligne de `Papu_Chess.html` n'a été touchée.
Livrable : ce document.

---

## Règle de licence — inspiration oui, copie non

**Aucune ligne de code Lichess n'a été rapatriée, et aucune ne doit
l'être.** Ce document décrit des CHOIX DE CONCEPTION dans nos propres
termes. Il ne contient aucun extrait, aucune transposition ligne à ligne,
aucun nom de fonction recopié pour être réimplémenté à l'identique.

Précision factuelle, parce que la prémisse de départ mérite d'être
affinée — les licences ne sont pas les mêmes selon le dépôt :

| Dépôt | Licence | Ce qu'il contient |
|---|---|---|
| `lichess-org/lila` | **AGPL-3.0** | le serveur et l'UI, dont le mode *gamebook* |
| `lichess-org/chessground` | **GPL-3.0** | le plateau (UI seule, aucune règle du jeu) |
| `lichess-org/pgn-viewer` | **GPL-3.0** | le lecteur de PGN à variantes |
| `lichess-org/scalachess` | MIT | modélisation en Scala (permissive) |

Les trois premiers sont **copyleft**. La conséquence opérationnelle est
la même dans les trois cas et ne change pas d'un iota : intégrer leur
code dans `Papu_Chess.html` placerait **tout le fichier** sous copyleft.
Or notre unique dépendance embarquée, chess.js 0.10.3, est en
**BSD-2-Clause** — permissive. C'est ce qui nous permet aujourd'hui de
livrer un fichier HTML unique sans contrainte de diffusion, et c'est un
acquis qu'on ne troque pas contre une commodité d'affichage.

Seul `scalachess` serait juridiquement réutilisable — mais il est en
Scala, côté serveur, et sans objet pour nous.

---

## 1. Modèle d'état de position

### Ce qu'ils font

Le `pgn-viewer` **calcule la position une fois, à l'analyse du PGN, et la
mémorise sur chaque nœud**. Le parseur fait avancer une position de
travail au fil des coups et, à chaque nœud, y dépose un instantané FEN —
celui d'APRÈS le coup. La navigation ne rejoue plus rien : atteindre un
coup, c'est lire le FEN déjà posé sur son nœud.

Chaque nœud porte, en plus du FEN : le demi-coup (`ply`), le coup en SAN
et en UCI, le trait, un booléen « échec » **pré-calculé**, les
commentaires, les formes (flèches et cercles), les NAG, les pendules.

### Ce que nous faisons

Exactement la même chose. `encyResolveTree()` descend l'arbre une fois au
chargement, joue les `coup:` avec chess.js, et écrit `step.fen` sur
chaque étape ; `encyGoto()` fait `new Chess(step.fen)` et rien d'autre.

### Verdict

**Notre choix ne tient pas seulement la route : c'est le leur.** Deux
équipes parties de contraintes très différentes — eux un lecteur de PGN
grand public, nous un lecteur d'étapes pédagogique — ont convergé sur
« calcul une fois à l'ingestion, lecture d'index à la navigation ». C'est
la meilleure validation qu'on pouvait espérer, et elle confirme le
raisonnement qui l'avait motivée : le retour arrière devient exact et
gratuit, il n'y a pas de pile d'annulation à se tromper un jour sur le
roque ou la prise en passant.

Une nuance, mineure et à notre avantage : ils pré-calculent le booléen
« échec » sur le nœud, nous le demandons à chess.js au moment du rendu.
Ils ont raison pour leur usage (leur plateau ignore les règles du jeu, il
faut donc lui dire où est l'échec) ; nous avons chess.js sous la main au
rendu, la question ne se pose pas.

**Rien à reprendre ici.** Un point de vigilance, tout de même : leur
`ply` est un compteur global de demi-coups, qui donne un identifiant
stable à toute position de la ligne principale. Nous n'en avons pas — nos
étapes sont numérotées à la main (`1`, `A1.1`, `B2`). C'est ce qui rend
une renumérotation coûteuse chez nous, et sans effet chez eux. À garder
en tête si l'École grossit, sans rien changer aujourd'hui.

---

## 2. Variantes et arbre

### Ce qu'ils font

Un nœud porte un tableau d'enfants. **Il n'existe pas d'objet
« variante » : une variante EST un enfant de rang supérieur à zéro.** Le
premier enfant est, par convention, la ligne principale. Toute la
machinerie des variantes se réduit donc à « plusieurs enfants sur le même
parent », sans structure dédiée.

L'adresse d'un nœud est un **chemin** : une chaîne de caractères formée
en concaténant des identifiants de deux caractères, un par nœud traversé
depuis la racine. La racine est la chaîne vide. En découle une algèbre
très économique : le parent s'obtient en retirant les deux derniers
caractères ; un nœud est ancêtre d'un autre si son chemin est un préfixe
du sien ; l'ancêtre commun de deux nœuds se lit en comparant les chemins
paire par paire jusqu'à la divergence.

Un drapeau distingue les branches qui ne sont pas la ligne principale
mais doivent être traitées comme telles.

### Ce que nous faisons

Notre arbre a la même forme — un nœud racine, des enfants — mais
**l'adressage est à deux étages** : `encyPath` (le chemin de branches,
une liste de noms `A` → `A.1`) plus `encyStep` (l'index de l'étape dans
le nœud courant). Et nos nœuds sont des **branches nommées** : elles
portent un titre, un libellé, une `nature:`, un FEN d'entrée déclaré.

### Verdict

Ce sont deux modèles pour deux besoins, et le nôtre n'est pas une version
naïve du leur.

**Ce que notre découpage gagne** : chez eux, un nœud est une position et
rien de plus ; chez nous, une branche est une **unité pédagogique** — « la
dame s'interpose », « le roi fuit » — qui a un nom qu'on montre au joueur,
une provenance (`heritee` / `elaboree`) et un FEN d'entrée à contrôler.
Leur modèle ne saurait pas porter ça. Aplatir nos branches en une suite
de nœuds anonymes ferait perdre exactement ce qui fait notre valeur.

**Ce que leur modèle a de mieux** : un nœud = une adresse, une seule.
Chez nous, deux variables doivent rester cohérentes, et c'est
précisément là qu'est né le défaut F10 — l'arrêt sur clôture dépendait de
`encyStep` par rapport à la longueur du nœud courant, pas de la clôture
elle-même.

**L'idée à reprendre — une seule, et elle est petite : le chemin comme
chaîne unique.** Pouvoir écrire `B/2` ou `A.1/3` pour désigner « branche
B, étape 2 ». Ce n'est pas une refonte : c'est une fonction de lecture et
une fonction d'écriture par-dessus l'état existant. Trois usages
immédiats :

1. **ouvrir une démonstration à un endroit précis** — indispensable au
   Top mats, qui devra reprendre la position Nataf après `Ce4+` sans
   refaire dérouler l'entrée-motif ;
2. **écrire un test qui vise une étape** sans compter les clics ;
3. **renvoyer depuis la prose** vers une étape, comme `[[id]]` renvoie
   vers une entrée.

**Ce qui est hors-scope** : toute leur machinerie de MUTATION de l'arbre
— ajouter un coup, promouvoir une variante en ligne principale, fusionner
deux nœuds identiques, supprimer une branche. Elle existe parce que leur
arbre grandit sous les doigts de l'utilisateur. **Le nôtre est en lecture
seule : la vérité est le fichier `.md`.** Importer ces opérations
reviendrait à importer un problème qu'on n'a pas.

**Un endroit où nous sommes en avance sur eux, pour notre usage** : notre
FEN d'entrée de branche déclaré ET dérivé, avec contrôle du désaccord (v3
F4). Ils n'ont pas d'équivalent — et n'en ont pas besoin, puisque leur
arbre est *dérivé* d'un PGN et jamais écrit à la main. Le nôtre est écrit
à la main, dans un fichier texte, par un humain. La redondance est notre
garde-fou contre la divergence silencieuse, et cette reconnaissance
confirme qu'elle est bien à nous d'inventer : personne ne nous la
fournira.

---

## 3. Annotations — flèches et cercles

### Ce qu'ils font

Chessground modélise une annotation comme une **forme** : une case
d'origine, une case de destination *optionnelle*, et un « pinceau ». Sans
destination, c'est un cercle ; avec, une flèche. C'est exactement la
distinction que portent nos `%csl` et `%cal`, et elle est prise du même
côté.

Le **pinceau** est un objet nommé qui porte une couleur, une opacité et
une épaisseur de trait. Quatorze pinceaux par défaut :

- vert, rouge, bleu, jaune — opacité pleine, trait de 10 ;
- leurs quatre variantes **pâles** — opacité 0,4, trait de 15 ;
- violet (0,65), rose (0,5), blanc (1) et blanc pâle (0,6).

Deux collections **séparées** de formes coexistent et se dessinent
identiquement : celles que l'utilisateur trace à la main, et celles que la
machine pose (le meilleur coup d'un moteur, par exemple).

Une forme peut aussi porter une **étiquette de texte** affichée dans le
coin de la case, une **pièce fantôme** posée sur la case d'origine, ou un
SVG libre. Et elle se dessine au choix au-dessus des pièces ou sous
elles.

Le plateau surligne par ailleurs le dernier coup et la case du roi en
échec — deux réglages actifs par défaut. Les pièces s'animent sur 200 ms.

### Verdict

Notre modèle est le bon, et pour l'essentiel nous avons déjà l'équivalent
fonctionnel : `extractVisuals()` lit la même grammaire, le surlignage du
dernier coup et la pulsation du roi en échec existent, l'animation
d'arrivée aussi.

**Trois nuances valent d'être reprises.**

1. **Les variantes pâles d'une même couleur.** C'est la plus utile, et
   elle est compatible avec notre règle « trois couleurs, pas quatre » —
   parce qu'un jaune pâle reste du jaune. Elle donne ce qui nous manque :
   distinguer une ligne **de contexte** (celle qu'on rappelle) d'une ligne
   **active** (celle dont on parle maintenant), sans introduire de
   quatrième sémantique. Notre étape 7, qui empile quatre cercles verts et
   une ligne jaune, y gagnerait immédiatement.

2. **L'étiquette de texte sur une case.** Numéroter un parcours — « 1 »
   sur e4, « 2 » sur d6 — dirait en un coup d'œil ce que notre prose doit
   aujourd'hui expliciter. Utile au Top mats, où l'on montre des séquences
   de mat en plusieurs temps.

3. **La séparation formes-de-l'auteur / formes-du-joueur.** Sans objet
   tant que le lecteur est en lecture seule. **Elle devient nécessaire le
   jour où l'École laisse le joueur dessiner** — sinon son trait et celui
   du Fou se confondent, et le « efface tes flèches » n'a plus de cible
   propre. À poser le jour où on ouvrira le dessin, pas avant.

**Hors-scope** : le tracé à main levée, l'aimantation des flèches sur les
coups légaux, le glisser-déposer, la pièce fantôme, le SVG libre. Ce sont
des raffinements d'un plateau d'analyse interactif ; notre plateau
**énonce**, il ne se laisse pas annoter.

---

## 4. Navigation et pause pédagogique

C'est ici que la reconnaissance rapporte le plus, et pas là où on
l'attendait.

### Le `pgn-viewer` ne sait pas faire de pause

Il est **délibérément passif**. Il expose un demi-coup de départ, des
commandes de navigation, une orientation, l'affichage ou non des flèches
— et c'est tout. Ses auteurs écartent explicitement l'interactivité, les
moteurs et l'exploration : cela relève, disent-ils, de l'échiquier
d'analyse complet. **Il n'y a rien à en tirer pour notre pause « que
ferais-tu ? ».**

### La pause vit ailleurs : le mode *gamebook*

Le vrai équivalent est le mode **leçon interactive** (« gamebook ») des
études Lichess. Son fonctionnement, tel qu'il ressort de la lecture :

**Quatre états de retour** : *à toi de jouer*, *bien*, *raté*, *fin*.

**Comment il décide que l'élève doit jouer** : il compare le trait à la
couleur attribuée à l'élève. Si c'est à lui, on attend son coup ; sinon,
le coup adverse s'exécute **tout seul**, après un court délai, pour lui
laisser voir la position.

**Coup juste** (conforme à la ligne principale) : retour « bien », puis
avance automatique après un délai.

**Coup faux** : retour « raté », et — c'est le point remarquable — **le
commentaire qui explique l'erreur est écrit SUR le coup faux lui-même**.
L'auteur de la leçon rédige la réfutation à l'endroit où l'élève se
trompe, pas dans une note générale.

**L'indice est caché par défaut** et ne se révèle qu'à la demande.
Délibérément : un indice visible d'office n'est plus un indice.

**La fin** est reconnue quand la ligne principale n'a plus de successeur.

Enfin, un nœud peut porter une **dérogation** qui force le mode — « ici,
on joue » ou « ici, on regarde » — indépendamment de ce que la structure
laisserait déduire.

### Ce que ça dit de nos choix

**Notre `cloture:` était bien vue, et pour la bonne raison.** La décision
v5 « une valeur, pas un simple drapeau » — `cloture: pause` dit *pourquoi*
ça s'arrête — est exactement la forme de leur dérogation par nœud. Deux
conceptions indépendantes ont abouti au même objet : une clé portée par
l'étape, dont la valeur nomme le régime.

**Mais notre pause ARRÊTE là où la leur PASSE LA MAIN.** C'est la
différence de fond, et elle est assumée pour l'entrée-motif : la
découverte enseigne le motif, elle ne fait pas jouer. Pour le **Top
mats**, en revanche, c'est la main qu'il faudra passer. Notre clé est
prête à le dire : `cloture: pause` a des frères possibles — une valeur qui
signifierait « rends la main au joueur, attends son coup » — sans changer
la clé ni le format.

**Nos branches SONT déjà ce dont une leçon interactive a besoin.** Leur
idée forte, la réfutation écrite sur le coup faux, nous l'avons déjà sous
une autre forme : la branche A est *littéralement* « pourquoi
l'interposition de la dame perd », écrite là où le joueur se tromperait.
Ce que nous n'avons pas, c'est le **moyen pour le joueur d'y arriver en
jouant** plutôt qu'en cliquant sur un bouton de branche. C'est un
changement d'entrée, pas de matière : la matière est écrite.

**Le contrôle de complétude d'embranchement prend ici tout son sens.**
`encyResolveTree` vérifie déjà que les branches d'un nœud couvrent TOUS
les coups légaux de la position. Écrit pour la rigueur, ce contrôle est
en réalité la **condition d'existence** d'une leçon interactive : si le
joueur peut jouer n'importe quel coup légal, il faut une réponse écrite
pour chacun. Nous avons donc, sans l'avoir cherché, le garde-fou qui
rendra le Top mats sûr.

### Trois idées à reprendre pour l'École

1. **L'indice caché par défaut, révélé à la demande.** Simple, et c'est
   la différence entre un exercice et une démonstration.
2. **La réponse adverse jouée automatiquement, après un court délai.**
   Quand le joueur trouve `Rc8`, c'est au Fou de jouer `Cd6#` — pas au
   joueur de cliquer « suivant ». Le délai n'est pas cosmétique : il
   laisse voir la position avant qu'elle change.
3. **La fin déduite de la structure**, non déclarée : plus de successeur
   sur la ligne suivie, donc c'est fini. Ça évite une clé de plus.

### Ce qui est hors-scope

Le compte de réussite, la répétition espacée, le passage automatique au
chapitre suivant, le retour arrière automatique après un échec. Ce sont
des mécaniques de plateforme d'entraînement ; l'École est une leçon, pas
un entraîneur.

---

## 5. Pourquoi nous n'intégrons PAS Chessground

Quatre raisons, de la plus décisive à la plus pratique.

**1. La licence — et c'est celle qui tranche.** Chessground est en
GPL-3.0. L'inclure dans `Papu_Chess.html` placerait le fichier entier
sous GPL. Notre chess.js est en BSD-2-Clause précisément parce qu'un
fichier unique ne peut pas cloisonner ses dépendances : tout ce qu'on y
verse contamine tout le reste. Ce n'est pas un obstacle qu'on contourne
par un effort d'ingénierie, c'est une décision de projet.

**2. La forme de distribution est incompatible avec la nôtre.**
Chessground se distribue en paquet npm, écrit en TypeScript, compilé avec
pnpm, et livre son habillage en SCSS à compiler. Notre projet est **un
fichier HTML**, sans bundler, sans `node_modules`, sans étape de
construction, servi par un script Python de 7 Ko et par GitHub Pages.
Adopter Chessground, ce n'est pas ajouter une bibliothèque : c'est
adopter une chaîne d'outils, et donc changer la nature du projet.

**3. Ça ne remplacerait même pas ce qui nous coûte.** Chessground le dit
lui-même : **aucune logique d'échecs à l'intérieur**. C'est un plateau,
pas un moteur. Nous garderions chess.js pour la légalité, l'échec et le
mat, c'est-à-dire pour tout le travail que fait `encyResolveTree`. On
échangerait donc notre rendu — qui marche — contre une dépendance lourde,
sans rien gagner sur la partie difficile.

**4. Notre lecteur fait déjà le travail.** Le cœur tient en une trentaine
de lignes : `encyPlayCoup()` joue le coup, `encyResolveTree()` mémorise le
FEN par étape et contrôle, `encyGoto()` instancie et affiche. Et le
plateau a déjà le surlignage du dernier coup, la pulsation du roi en
échec, les flèches et cercles, l'animation d'arrivée. Ce qui nous
manquait n'était pas un plateau : c'était une **règle de langue** (F9),
que nulle bibliothèque n'aurait fournie.

---

## 6. Conclusion — ce qu'on garde, ce qu'on laisse

### Idées à reprendre (pas de code)

| Idée | Où elle sert | Coût |
|---|---|---|
| **Le chemin comme chaîne unique** (`B/2`) pour adresser une étape | ouvrir le Top mats sur une position, tester, renvoyer depuis la prose | petit — deux fonctions par-dessus l'état existant |
| **Les variantes pâles d'une couleur** (contexte / actif) | distinguer la ligne rappelée de la ligne active, sans quatrième couleur | petit — une convention de format, un pinceau |
| **L'étiquette de texte sur une case** (numéroter un parcours) | séquences de mat du Top mats | moyen |
| **L'indice caché, révélé à la demande** | École, exercices | petit |
| **La réponse adverse jouée automatiquement, avec délai** | École, après le coup trouvé | petit |
| **La fin déduite de la structure** plutôt que déclarée | évite une clé de format de plus | nul — c'est une décision |
| **La réfutation écrite sur le coup faux** | on l'a déjà, sous forme de branches — à confirmer comme doctrine | nul |

### Choix qui sortent confirmés, sans rien changer

- **FEN mémorisé par étape, calculé une fois au chargement.** C'est leur
  choix aussi. Notre conception du 2026-08-05 tient.
- **La `cloture:` à valeur** plutôt qu'un drapeau : même forme que leur
  dérogation par nœud.
- **Le contrôle de complétude d'embranchement** : écrit pour la rigueur,
  il se révèle être la condition d'existence d'une leçon interactive.
- **Le FEN d'entrée de branche redondant** : sans équivalent chez eux,
  parce que leur arbre est dérivé et le nôtre écrit à la main. À nous de
  le garder.

### Hors-scope pour nous

- Toute mutation d'arbre (ajouter, promouvoir, fusionner, supprimer) :
  notre arbre est en lecture seule, la vérité est le `.md`.
- Le dessin à main levée, l'aimantation des flèches, le glisser-déposer.
- Le compte de réussite, la répétition espacée, l'enchaînement de
  chapitres.
- Chessground lui-même, pour les quatre raisons du §5.

### Le point le plus important de cette reconnaissance

Nous cherchions ce qui manquait à notre lecteur, et la réponse est :
**presque rien sur le plan technique**. Le modèle d'état est le leur,
l'arbre est adapté à notre usage, les annotations sont du même modèle.
Ce que le Top mats demandera n'est pas une meilleure mécanique, c'est un
**changement de régime** : cesser d'interdire au joueur de jouer, pour
une étape, sur un coup attendu. Le verrou actuel de lecture seule est
délibéré et doit le rester par défaut ; l'École sera l'exception qui le
lève, une étape à la fois. C'est une conception à écrire, et elle sera
courte.

---

## Sources consultées (lecture seule)

- `lichess-org/pgn-viewer` — README, `src/config.ts`, `src/game.ts`,
  `src/path.ts`, `src/pgn.ts`, `src/interfaces.ts`
- `lichess-org/chessground` — README, `src/draw.ts`, `src/state.ts`
- `lichess-org/lila` — `ui/lib/src/tree/tree.ts`,
  `ui/lib/src/tree/path.ts`,
  `ui/analyse/src/study/gamebook/gamebookPlayCtrl.ts`,
  `ui/analyse/src/study/gamebook/interfaces.ts`
- Licences vérifiées via l'API GitHub (voir tableau en tête)
