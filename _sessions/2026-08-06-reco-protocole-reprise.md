# Reconnaissance — protocoles de reprise et mémoire d'agent

*2026-08-06. Document de reconnaissance, séparé des chantiers de code.
`Papu_Chess.html` n'est pas touché.*

---

## Règle de cette reconnaissance

**Inspiration des IDÉES uniquement. Aucune copie de code ni de fichier.**
Rien de ce qui suit n'a été récupéré, adapté ou transposé depuis un
dépôt : ce document décrit des mécanismes observés et en tire des
recommandations écrites dans nos termes.

**Notre projet reste un mono-fichier HTML sans build** — pas de
`package.json`, pas de bundler, pas de suite de tests, pas de CI. Toute
solution qui suppose une chaîne d'outillage est hors-scope par
construction, et ce critère tranche plusieurs des propositions ci-dessous.

### Licences relevées

Vérifiées par l'API GitHub (`gh api repos/<dépôt>`), pas d'après les
README, qui mentionnent parfois une licence qu'ils ne portent pas.

| Dépôt | Licence exacte | Contaminante ? |
|---|---|---|
| `hudrazine/claude-code-memory-bank` | **Unlicense** (The Unlicense — domaine public) | Non |
| `REMvisual/claude-handoff` | **MIT** | Non |
| `centminmod/my-claude-code-setup` | **MIT** | Non |
| `CodyLiska/obsidian-llm-memory` | **MIT** | Non |

Aucun n'est GPL ni AGPL : la contamination redoutée ne se présente pas.
**La règle « inspiration seule » s'applique quand même** — elle ne
dépendait pas de la licence, et une licence permissive n'est pas une
invitation à copier ce qu'on peut concevoir soi-même.

**Correction de nomenclature** : `CodyLiska/claude-obsidian-memory`
n'existe pas (404 confirmé par l'API). Le dépôt visé est
`CodyLiska/obsidian-llm-memory`, même auteur, MIT, dernière poussée
2026-05-23. C'est celui-ci qui a été lu.

---

## 1. CLAUDE.md natif — notre angle mort

### Ce que fait réellement Claude Code

La documentation à jour (`code.claude.com/docs/en/memory`) est sans
ambiguïté : **Claude Code lit `CLAUDE.md` automatiquement au début de
chaque session**, sans qu'on ait rien à taper. Le fichier est cherché à
la racine du projet (`./CLAUDE.md` ou `./.claude/CLAUDE.md`), puis en
remontant l'arborescence ; tout ce qui est trouvé est **concaténé** en
contexte, du plus général au plus spécifique.

Quatre points comptent pour nous :

- **Le chargement est intégral, pas paresseux.** Un `CLAUDE.md` de 300
  lignes coûte 300 lignes à chaque session. La doc recommande de viser
  **moins de 200 lignes** et précise que les fichiers plus longs
  « consomment plus de contexte et réduisent l'adhérence ».
- **La syntaxe d'import `@chemin` ne fait pas d'économie.** Elle est
  explicite : « Splitting into `@path` imports helps organization but
  doesn't reduce context, since imported files load at launch. » Importer
  `@_fonds/RESTE_A_FAIRE.md` (300 lignes) reviendrait à le coller en tête
  de chaque session. Pour citer un chemin **sans** l'importer, il faut
  l'entourer de backticks.
- **Le `CLAUDE.md` de racine survit à la compaction.** Après un
  `/compact`, il est relu depuis le disque et réinjecté. C'est
  exactement la panne que la Partie 1 d'aujourd'hui nommait : la
  conversation qui meurt sans clôture propre. Un protocole écrit là
  survit à ce que `REPRISE.md` seul ne survit pas.
- **Ce n'est pas une couche d'exécution.** La doc le dit crûment :
  « Settings rules are enforced by the client regardless of what Claude
  decides to do. CLAUDE.md instructions shape Claude's behavior but are
  not a hard enforcement layer. » Notre digue est donc **au bon endroit**
  dans `.claude/settings.json` et n'a rien à faire dans un `CLAUDE.md`.

### Notre situation

Il n'y a **aucun `CLAUDE.md` dans le dépôt** — vérifié, le fichier est
absent de la racine comme de `.claude/`. Conséquence directe : tout notre
protocole de reprise repose sur un mot que Flavien tape (« reprise »), et
ce mot s'adresse à **Claude-conversation**. Claude Code, lui, démarre
chaque session sans rien : ni `REPRISE.md`, ni `PRINCIPES.md`, ni la
notion qu'un plan de route existe. Il découvre le protocole seulement si
on le lui montre, session après session.

C'est l'asymétrie que la reconnaissance met en évidence : **la
conversation a un rituel, Code n'en a aucun**, et c'est Code qui touche
les fichiers.

### Recommandation

**Oui, créer un `CLAUDE.md` à la racine, court, qui pointe sans
importer.** Cible : trente à quarante lignes. Il doit contenir ce que
Code doit savoir avant tout geste, et rien d'autre :

1. **Ce qu'est le projet en deux phrases** — mono-fichier HTML autonome,
   sans build ; le fonds est de la donnée séparée du code.
2. **L'ordre de lecture au démarrage** — « lire `REPRISE.md` avant toute
   autre réponse ; il désigne la suite ». Les chemins **entre backticks**,
   jamais en `@import` : sinon `REPRISE.md` (92 lignes) et
   `RESTE_A_FAIRE.md` (300 lignes) entrent en contexte à chaque session,
   ce qui est précisément ce qu'on veut éviter.
3. **Les non-négociables** — `Papu_Chess.html` est la source de vérité et
   se livre complet ; jamais de merge sur `main` ; le diff se montre
   toujours ; toute réponse substantielle se consigne dans `_sessions/`.
4. **Les deux mots d'amorce** — ce que « reprise » et « consigne »
   déclenchent, pour que Code les honore aussi et pas seulement la
   conversation.

Ce fichier ne duplique pas `REPRISE.md` : il l'**amorce**. `REPRISE.md`
reste le document que l'on ouvre ; `CLAUDE.md` est ce qui garantit qu'on
l'ouvre.

Une réserve, à porter au dossier : le `CLAUDE.md` devra être ajouté à la
branche `noyau-protocole` ou à un successeur, pas à `wip-demo-jouable`,
pour rester cohérent avec la désolidarisation faite aujourd'hui.

### Ce qu'il faut savoir de la mémoire automatique native

La doc décrit un second mécanisme, l'**auto memory** : Claude écrit
lui-même des notes dans `~/.claude/projects/<projet>/memory/`, avec un
`MEMORY.md` index dont **les 200 premières lignes** sont chargées à
chaque session, les fichiers de sujet restant à la demande.

C'est bien conçu — et **inutilisable comme mémoire du projet chez nous**,
pour une raison dirimante : c'est **local à la machine**. « Files are not
shared across machines or cloud environments. » Cela ne voyage pas avec
le dépôt, cela ne se pousse pas, cela ne se relit pas depuis une autre
session sur une autre machine. Notre contrat de mémoire dit « le DÉPÔT
est la mémoire du projet » : l'auto memory est le contre-exemple exact et
ne doit surtout pas être ce sur quoi on compte. Elle reste utile comme
commodité privée ; elle n'est jamais la trace.

---

## 2. Structure des fichiers de mémoire

### Comment ils découpent

**`hudrazine/claude-code-memory-bank`** (Unlicense) reprend la
descendance du Memory Bank de Cline : six fichiers dans `memory-bank/`,
hiérarchisés. `projectbrief.md` (le socle) alimente `productContext.md`,
`systemPatterns.md` et `techContext.md`, qui alimentent à leur tour
`activeContext.md` et `progress.md`. La distinction structurante est
entre **ce qui ne bouge pas** (brief, patterns, stack) et **ce qui bouge
à chaque séance** (contexte actif, progression).

**`centminmod/my-claude-code-setup`** (MIT, 2 542 étoiles, le plus vivant
du lot) fait plus net avec un `CLAUDE.md` orchestrateur d'une centaine de
lignes et quatre satellites nommés par leur fonction :
`CLAUDE-patterns.md`, `CLAUDE-decisions.md` (des ADR horodatées),
`CLAUDE-troubleshooting.md`, `CLAUDE-activeContext.md`.

**`CodyLiska/obsidian-llm-memory`** (MIT) éclate encore : `projects/`,
`lessons-learned.md`, `decisions-log.md`, `stack-notes/`, `synthesis/`,
`conventions.md`, `recurring-tasks.md`, reliés par des wikilinks.

**`REMvisual/claude-handoff`** (MIT) ne découpe pas par catégorie mais
par **séance** : un fichier `HANDOFF_[tâche]_[date].md` par passation,
avec des sections fixes (The Goal, Where We Are, What We Tried, Key
Decisions, Evidence & Data, User Feedback, Where We're Going, Quick
Start).

Cinq axes reviennent partout : **invariants** (conventions, principes),
**décisions et leurs raisons**, **état courant**, **progression /
prochaines étapes**, **pannes et leçons**.

### Notre correspondance

| Axe | Chez nous | État |
|---|---|---|
| Invariants | `PRINCIPES.md` | Couvert |
| Décisions et raisons | `PRINCIPES.md` + `_sessions/` + `JOURNAL.md` | Couvert, réparti |
| État courant | `REPRISE.md` § 3 | Couvert |
| Progression | `_fonds/RESTE_A_FAIRE.md` | Couvert, et mieux qu'eux (cf. § 5) |
| Pannes et leçons | **nulle part de désigné** | **Manque** |

Sur quatre axes sur cinq, nous sommes couverts avec **trois fichiers là
où ils en ont six ou sept**, et je ne recommande pas de nous aligner :
`projectbrief.md` et `productContext.md` répondent à « de quoi parle ce
projet ? », question qui ne se pose pas à deux personnes dont l'une l'a
conçu ; `techContext.md` serait vide, puisque notre pile tient en une
phrase (HTML autonome, Stockfish WASM, pas de build). Notre simplicité
est un choix juste, pas une lacune.

### Le manque réel

**Il n'y a pas de place pour les propriétés connues de l'architecture** —
ce que `centminmod` appelle `CLAUDE-troubleshooting.md` et `CodyLiska`
`lessons-learned.md`. Et le symptôme est déjà visible dans nos fichiers :
`_fonds/RESTE_A_FAIRE.md` héberge aujourd'hui deux entrées qui ne sont
**pas des choses à faire**.

La première dit que le détecteur de mauvais fou (et
`fouOutpostSquares`/`fouPassedPawns`/`fouHangingSquares`) ne se déclenche
jamais sur une position FEN statique, et conclut elle-même que « ce n'est
pas un bug isolé mais une propriété actuelle de l'architecture ». La
seconde décrit le bug latent `startFen`. Ce sont des **constats de
fonctionnement** : la première n'appelle aucune action, la seconde est
une action mais dont la valeur principale est descriptive — savoir
pourquoi les cercles structurels se taisent évite de rechercher trois
fois la même panne.

Elles sont dans le plan de route faute d'ailleurs. Résultat : un fichier
qui se déclare « chantiers en suspens » contient un item qui ne sera
jamais fermé, et un lecteur qui cherche « pourquoi rien ne s'affiche »
n'a aucune raison d'aller chercher là.

**Recommandation, mesurée** : ouvrir `_fonds/PROPRIETES_CONNUES.md` — les
comportements attendus mais surprenants, avec leur cause et leur
contournement. Y déplacer ces deux entrées. C'est **un** fichier, pas
quatre, et il se justifie par un manque constaté chez nous, pas par
symétrie avec un dépôt externe.

---

## 3. Rituel de mise à jour

### Comment ils déclenchent

Trois mécanismes, par fiabilité croissante :

- **Un mot en langage naturel.** `CodyLiska` : l'utilisateur dit
  « wrap up this session » et Claude écrit les correctifs dans
  `lessons-learned.md`, les décisions dans `decisions-log.md`, met à jour
  `session-state.md`. C'est notre « consigne », au mot près.
- **Une slash-command.** `hudrazine` : `/workflow:update-memory`, dans
  une famille `/workflow:understand`, `/workflow:plan`,
  `/workflow:execute`. `centminmod` : `/update-memory-bank`.
  `REMvisual` : `/handoff` et `/handoffplan`.
- **Un hook.** `REMvisual` ship un `precompact-handoff.sh` qui s'exécute
  **avant la compaction du contexte**, décrit comme un filet de sécurité.
  `CodyLiska` fait de même avec `pre-compact.sh`, plus un `PostToolUse`
  qui resynchronise à chaque écriture.

### Ce que « consigne » vaut

Notre mot fonctionne — la journée d'aujourd'hui en est la preuve : quatre
parties, quatre consignations, sans qu'il faille le redemander. Mais il a
la fragilité que la Partie 1 a nommée ce matin : **il suppose que
quelqu'un soit encore là pour le taper, ou que la conversation atteigne
sa fin**. Une conversation qui meurt sur une limite atteinte n'entend
aucun mot.

La documentation officielle tranche exactement ce point : « If the
instruction is something that must run at a specific point, such as
before every commit or after each file edit, write it as a hook instead.
Hooks execute as shell commands at fixed lifecycle events and apply
regardless of what Claude decides. » Un mot est une intention ; un hook
est un fait.

### Recommandation, en trois marches

**Marche 1 — la moins chère, à faire.** Inscrire « consigne » dans le
`CLAUDE.md` recommandé au § 1, comme instruction permanente. Coût : trois
lignes. Gain : Code honore le mot dès la première session, sans qu'on le
lui rappelle, et le rappel survit à la compaction.

**Marche 2 — une slash-command `/consigne`, à faire ensuite.** Un mot
dans un fichier reste de la persuasion ; une commande de projet charge
des instructions explicites au moment où on l'invoque. Utile surtout
parce qu'elle peut porter la **procédure** — quelle catégorie va où,
avec les deux portes obligatoires pour un chantier — plutôt que de
compter sur la mémoire du protocole. C'est le seul emprunt franc que je
recommande aux quatre dépôts.

**Marche 3 — un hook `PreCompact`, à peser, pas à faire tout de suite.**
C'est la vraie trouvaille de `REMvisual` et la seule réponse mécanique à
la mort brutale de conversation. Mais deux réserves honnêtes. D'abord il
ne couvre pas tout : il se déclenche à la compaction, pas sur une coupure
réseau ni sur une réponse qui ne charge jamais — c'est un filet plus
large que le nôtre, pas un filet complet. Ensuite il introduit un script
shell à maintenir dans un dépôt qui n'a aucune chaîne d'outillage, et le
protocole que nous avons écrit ce matin — consigner **au fil de l'eau** —
attaque déjà le problème par l'autre bout, en réduisant ce qu'une mort
brutale peut emporter. **Poser cette marche comme chantier parqué avec
ses deux portes** plutôt que de l'implémenter maintenant : *pas avant*
qu'une consignation ait réellement été perdue ; *dès que* ce cas se
produit une première fois.

---

## 4. Chargement à la demande

### Comment ils s'y prennent

`centminmod` est le plus explicite et le plus proche de notre besoin :
son `CLAUDE.md` fait une centaine de lignes et les satellites sont
**lus à la demande, pas auto-chargés** — le README le pose comme
principe, « progressive disclosure ». Il n'utilise délibérément **pas**
les `@imports`, précisément parce qu'ils ne font pas d'économie.

`CodyLiska` chiffre : environ 3 000 tokens d'index au démarrage, les
journaux complets et les notes de pile ne se chargeant que sur
déclencheur.

`hudrazine` fait l'inverse : il importe son fichier de règles depuis
`CLAUDE.md`, donc tout entre en contexte au lancement. C'est le modèle le
moins économe des trois, et c'est aussi le dépôt le moins entretenu
(dernière poussée juillet 2025).

Le mécanisme natif suit le même principe que `centminmod` : `MEMORY.md`
plafonné à 200 lignes chargées, fichiers de sujet lus à la demande.

### Comment garder `REPRISE.md` court

Nos volumes actuels : `REPRISE.md` 92 lignes, `PRINCIPES.md` 77,
`_fonds/RESTE_A_FAIRE.md` 300, `JOURNAL.md` 289. Trois règles suffisent.

**a. Ne jamais importer, toujours pointer.** Les chemins dans
`CLAUDE.md` et `REPRISE.md` restent entre backticks. Un `@import` de
`RESTE_A_FAIRE.md` coûterait 300 lignes à chaque session pour une
information dont on n'a besoin qu'à la reprise.

**b. Plafonner explicitement.** `CLAUDE.md` sous 50 lignes,
`REPRISE.md` sous 100. Le second est à 92 : il est **déjà à la limite**,
et c'est la section 3 qui l'a fait grossir de 20 lignes aujourd'hui.

**c. La section 3 doit pointer, pas recopier.** C'est le point le plus
concret de tout ce document. Notre section « Où on en est » recopie du
texte ce que git détient déjà — nombre de commits, SHA, branches — et
elle admet elle-même sa faiblesse en tête, par la règle « GIT FAIT FOI :
cette section n'est qu'un pointeur de confort ». L'instinct est le bon ;
la mise en œuvre le contredit encore, puisque nous rafraîchissons ce
texte à chaque push et qu'il est déjà faux entre deux pushs.

**Recommandation** : réduire la section 3 à ce que git ne dit pas — quel
chantier est en cours, ce qu'il attend, quel décalage connu subsiste — et
remplacer les chiffres par la commande qui les donne :

```
git log --oneline main..HEAD && git ls-remote origin refs/heads/main
```

On y gagne trois fois : la section cesse de pouvoir mentir, elle cesse
d'être un travail de tenue à jour, et elle rétrécit d'environ vingt
lignes, ce qui remet `REPRISE.md` sous son plafond.

---

## 5. Notre démarque

### Ce qui n'existe chez aucun des quatre

**La discipline des DEUX PORTES.** Les quatre dépôts savent enregistrer
ce qui est en attente : `progress.md` chez `hudrazine`, « Where We're
Going » chez `REMvisual`, `CLAUDE-activeContext.md` chez `centminmod`.
Tous produisent des listes ordonnées de prochaines étapes. **Aucun
n'exige qu'un item mis en sommeil déclare ce qui le réveille.** Ils
notent l'ordre, parfois la dépendance ; jamais le signal. Notre règle —
un « pas avant » seul est une écriture morte, il dit quand ne pas
commencer et jamais quand commencer — n'a d'équivalent nulle part dans ce
que j'ai lu.

**Le signal de réveil posé AU SITE DE LA DÉPENDANCE.** C'est la partie la
plus singulière. Le cousin le plus proche est `CodyLiska`, dont les
wikilinks (proposés par un script `propose-wikilinks.py`) relient les
entrées de journal aux fiches de projet. Mais c'est un dispositif de
**navigation** : le lien est écrit pour qui lit déjà la note, et il va du
dépendant vers la dépendance — le sens naturel, celui qui n'aide pas.
Notre pointeur va **en sens inverse** et se plante dans un fichier qu'on
ouvrira pour une tout autre raison. La note « FICHES DATÉES = matière de
l'accueil éditorialisé » est dans `_fonds/encyclopedie/FORMAT.md`, à la
définition du rayon Histoire : elle attend celui qui écrira une fiche
datée sans penser une seconde à l'accueil. Aucun des quatre ne fait ça.

**Le marqueur `(à compléter)`.** Quand une seule des deux portes est
établie, nous l'écrivons comme manquante au lieu d'en inventer une.
Six items du plan de route le portent. C'est un dispositif d'honnêteté
épistémique — distinguer ce qu'on sait de ce qu'on a comblé — que je ne
retrouve dans aucun des formats consultés, qui tendent à produire des
sections toujours remplies.

**La digue en couche d'exécution.** Nos règles `deny` sont dans
`.claude/settings.json`, donc appliquées par le client quoi que Claude
décide. Les quatre dépôts mettent leurs garde-fous dans de la prose de
`CLAUDE.md` — c'est-à-dire dans de la persuasion. La documentation
officielle valide notre placement.

### Ce qui vaut d'être repris

1. **Un `CLAUDE.md` de racine, court et pointeur** (§ 1). C'est le seul
   manque grave : notre protocole ne s'amorce pas tout seul côté Code.
   Rapport valeur/coût le plus élevé de toute cette reconnaissance.
2. **Une slash-command `/consigne`** (§ 3, marche 2), pour que le rituel
   porte sa procédure au lieu de dépendre de la mémoire du protocole.
3. **Un fichier des propriétés connues** (§ 2), qui répare un désordre
   déjà présent dans notre plan de route.
4. **La discipline « pointer, ne jamais importer »** de `centminmod`
   (§ 4), à écrire comme règle, et la section 3 de `REPRISE.md` à réduire
   à ce que git ne dit pas.

### Ce qui est de la sur-ingénierie hors-scope

- **Le memory bank à six fichiers** de `hudrazine`. `techContext.md`
  serait vide — nous n'avons pas de pile à documenter —, `projectbrief.md`
  et `productContext.md` répondent à une question que deux personnes qui
  ont conçu le projet ne se posent pas. Six fichiers à tenir cohérents
  pour un gain nul.
- **Le triptyque `/workflow:understand|plan|execute`.** Une cérémonie de
  processus, faite pour des équipes où l'agent doit prouver qu'il a
  compris avant d'agir. À deux, avec un arbitrage humain à chaque palier,
  c'est du protocole pour du protocole.
- **Le coffre Obsidian de `CodyLiska`**, avec ses scripts Python, ses
  hooks `PostToolUse` de resynchronisation et son `CLAUDE-source.md`
  généré. C'est un **second système à maintenir**, alors que notre dépôt
  *est déjà* la mémoire — c'est littéralement notre contrat de mémoire.
  Ajouter un coffre externe le contredirait.
- **Les fichiers `HANDOFF_[tâche]_[date].md` chaînés** de `REMvisual`.
  Nous avons déjà `_sessions/` par jour, poussé et relu depuis le dépôt.
  Une passation par tâche avec numéros de séquence dupliquerait la trace
  au lieu de l'enrichir. En revanche l'idée du **prompt de reprise prêt à
  coller** rejoint une convention que nous avons déjà : les prompts
  complets et prêts à coller, par défaut.
- **L'auto memory native comme mémoire de projet** (§ 1). Elle est locale
  à la machine et ne voyage pas : s'y fier romprait le contrat.

---

## En un paragraphe

Nous sommes en avance sur les quatre dépôts là où ça compte — la
discipline des deux portes et le réveil planté au site de la dépendance
n'ont d'équivalent nulle part —, et nous sommes plus simples qu'eux à
raison, trois fichiers valant leurs six ou sept pour un projet
mono-fichier mené à deux. Le manque est ailleurs, et il est net : **notre
protocole ne s'amorce pas tout seul.** Il attend qu'un humain tape un
mot, dans une conversation qui peut mourir avant de l'entendre, alors que
Claude Code lit un `CLAUDE.md` à chaque démarrage sans qu'on demande
rien, et le relit même après compaction. Créer ce fichier — court,
pointeur, sans imports — est le seul geste vraiment nécessaire ; le
reste, propriétés connues, `/consigne`, réduction de la section 3, est du
rangement utile mais second.
