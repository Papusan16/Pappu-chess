# La démonstration JOUABLE — conception

**2026-08-05.** Document de conception, à valider avant toute ligne de
code. Cible : que le lecteur d'encyclopédie sache faire évoluer la
POSITION d'étape en étape, et non plus seulement empiler des annotations
sur une position figée.

Ce document tranche quatre points : le FORMAT (comment une étape déclare
un coup joué), le LECTEUR (comment la position est tenue et la
navigation gardée cohérente), la COMPATIBILITÉ (ce qui ne doit pas
bouger), et la CIBLE DE VALIDATION (l'arrêt net après Ce4+).

---

## 0. Constat préalable : le moteur joue DÉJÀ les coups

Avant de concevoir la capacité, il fallait vérifier ce qui existe. Le
brief pose que le lecteur « sait seulement empiler des annotations sur
une position FIXE ». **Ce n'est pas ce que fait le code.** La clé
`coup:` de FORMAT v3 n'est pas seulement lue : elle est **jouée**.

Preuve, obtenue en extrayant le lecteur de `Papu_Chess.html` (chess.js
inliné, `extractVisuals()`, `encyParseEntry()`, `encyResolveTree()`) et
en le faisant tourner hors navigateur sur le fichier réel
`_fonds/encyclopedie/echec-a-la-decouverte.md` :

```
demos: 1 | fenRoot: 1r1k3r/pbp2q2/1pQ2N2/3Pp2p/3P3B/P7/1PP5/1K1R4 w - - 0 1
vérification : ok=true — 16 contrôles, 0 anomalie

NODE RACINE   entryFen = …/1pQ2N2/…            (cavalier en f6)
  ÉTAPE 1  coup=—        fen inchangé
  ÉTAPE 2  coup=—        fen inchangé
  ÉTAPE 3  coup=—        fen inchangé
  ÉTAPE 4  coup=—        fen inchangé
  ÉTAPE 5  coup=—        fen inchangé
  ÉTAPE 6  coup=1. Ce4+  move = f6→e4   fen = …/1pQ5/3Pp2p/3PN2B/…
  ÉTAPE 7  coup=—        cloture=pause   fen = position APRÈS Ce4+
    NODE A    entryFen = position après Ce4+
      ÉTAPE A1   coup=—
        NODE A.1  ÉTAPE A1.1 coup=1… De7   move = f7→e7
                  ÉTAPE A1.2 coup=2. Fxe7+ move = h4→e7
        NODE A.2  ÉTAPE A2.1 coup=1… Df6   move = f7→f6
                  ÉTAPE A2.2 coup=2. Fxf6+ move = h4→f6
    NODE B    ÉTAPE B1 coup=1… Rc8  move = d8→c8
              ÉTAPE B2 coup=2. Cd6# move = e4→d6
```

À l'étape 6, le cavalier **se déplace réellement** de f6 à e4, et le roi
noir **est réellement en échec** : `render()` pose la classe `in-check`
(pulsation rouge) sur le roi dont c'est le trait quand `game.in_check()`
est vrai (ligne 3270). Les onze coups de la démonstration sont joués,
légaux, et le « + » de Ce4+ comme le « # » de Cd6# sont **contrôlés
mécaniquement** au chargement.

**Conséquence pour ce chantier : il ne s'agit pas de construire une
capacité, mais d'en achever une.** C'est une bonne nouvelle — le travail
restant est plus court et plus sûr que prévu — mais ça change ce qu'il
faut concevoir. Le reste de ce document part de là.

### Alors d'où vient le décalage de l'étape 4 ?

Le symptôme rapporté est exact : à l'étape 4, le Fou dit « l'adversaire
doit **d'abord parer cet échec** » alors que le cavalier est encore en
f6 et qu'aucun échec n'existe. Mais la cause n'est pas le moteur : les
étapes 1 à 5 sont des étapes d'ANNOTATION (`coup: —`), et **le coup
n'est joué qu'à l'étape 6**. Le texte de l'étape 4 parle à l'accompli
d'un coup que sa propre étape n'a pas joué.

C'est un **défaut de rédaction**, pas d'exécution. Et c'est précisément
la classe de défaut qu'aucun contrôle actuel n'attrape : `verification`
vérifie la légalité, l'échec, le mat, les FEN de branche, la complétude
d'un embranchement — mais **rien ne vérifie que les mots de l'étape
décrivent la position de l'étape**. Le lecteur a raison, le texte a tort,
et le lecteur n'a aucun moyen de le dire.

---

## 1. Ce qui manque réellement

Cinq manques, du plus structurant au plus cosmétique.

**A. Le temps du verbe n'est pas gouverné.** Rien, dans FORMAT, ne dit
qu'une étape d'annotation parle au conditionnel et une étape de coup à
l'accompli. C'est la cause directe du décalage de l'étape 4, et ça se
reproduira à chaque nouvelle démonstration tant que ce n'est pas écrit.

**B. Les annotations d'une étape jouée portent sur la position d'APRÈS
le coup, et personne ne l'a jamais écrit.** `encyResolveTree()` calcule
`step.fen` après le coup, puis `encyIdentify()` dessine `step.anno` sur
cette position. Donc une flèche `Gf6e4` posée sur l'étape qui JOUE Ce4+
partirait d'une case **vide** — la pièce n'y est plus. Le fichier actuel
s'en tire parce que ses flèches de trajet vivent à l'étape 3 (annotation)
et pas à l'étape 6 (coup). C'est de la chance, pas une règle.

**C. `cloture:` n'arrête pas la navigation.** Elle masque les boutons de
branche (`encyRenderBranches` sort si `etape.cloture`), rien de plus.
L'arrêt observé aujourd'hui à l'étape 7 vient de ce qu'elle est la
**dernière étape** de son nœud : `navNext()` teste
`encyStep < n.steps.length-1` et bloque. Si une clôture était posée
ailleurs qu'en fin de nœud, la flèche « suivant » continuerait de
dérouler. **L'arrêt net marche par coïncidence.**

**D. Rien à l'écran ne DIT qu'un coup vient d'être joué.** Le panneau
affiche le titre, le libellé d'étape et le texte du Fou. Le coup lui-même
(« 1. Ce4+ ») n'apparaît nulle part. Les cases de départ et d'arrivée
sont bien surlignées (`lastFrom`/`lastTo` sont alimentés depuis
`step.from`/`step.to`), mais la position **saute** : `encyGoto()` appelle
`render(false)`, sans animation.

**E. `coup:` n'accepte que le SAN.** `encyFrSan()` convertit R/D/T/F/C →
K/Q/R/B/N, `encyStripMoveNum()` retire le numéro et une parenthèse
finale, puis `chess.js` reçoit le coup en mode `sloppy`. C'est solide,
mais un coup ambigu ou mal disambiguïsé échoue en bloc, et il n'existe
aucune façon de désigner un coup par ses cases.

---

## 2. FORMAT — comment une étape déclare un coup joué

### 2.1 La syntaxe ne change pas : `coup:` suffit

**Décision : on n'invente aucune clé pour le coup joué.** `coup: Ce4+`
joue le coup ; `coup: —` n'en joue aucun. C'est déjà le contrat de
FORMAT v3, il est implémenté, et il est correct. Ajouter une clé
`joue:` ou un drapeau `type: coup` dupliquerait une information que la
valeur de `coup:` porte déjà — et créerait la possibilité qu'ils se
contredisent.

Formes acceptées, entérinées telles qu'elles tournent :

| Écriture | Lue comme |
|---|---|
| `coup: —` | aucun coup, étape d'annotation |
| `coup: Ce4+` | SAN français |
| `coup: Ne4+` | SAN anglais |
| `coup: 1. Ce4+` | le numéro est retiré |
| `coup: 1… De7` | le numéro noir est retiré |
| `coup: 2. Fxe7+ (la prise)` | la parenthèse finale est retirée |

### 2.2 Une tolérance à ajouter : la notation par cases

**Proposition : accepter aussi `coup: f6-e4`** (cases source-destination,
tiret ou `→`), avec promotion optionnelle `e7-e8=D`.

Pourquoi l'ajouter alors que le SAN marche : parce que le SAN est le seul
endroit du format où une erreur de rédaction produit un échec **total**
et pas une approximation. `Cd6#` mal disambiguïsé, un `x` oublié sur une
prise, un `+` de trop — et l'étape entière devient illégale. La notation
par cases est sans ambiguïté par construction. Elle n'est pas la forme
recommandée (le SAN reste plus lisible pour un humain, et c'est lui qui
figure dans les sources) : c'est une **issue de secours**, à écrire quand
le SAN résiste.

Coût d'implémentation : quelques lignes dans `encyStripMoveNum` /
`encyFrSan` — détecter le motif `^([a-h][1-8])[-→]([a-h][1-8])(=[RDTFC])?$`
et passer `{from, to, promotion}` à `chess.js` au lieu d'une chaîne SAN.
`chess.js` accepte déjà cet objet.

### 2.3 Mélanger annotées et jouées : OUI, et c'est le régime normal

**Décision : une démonstration n'a PAS de type. Le régime est porté par
l'ÉTAPE, jamais par la démonstration.**

Trois raisons de trancher ainsi.

1. **C'est déjà le cas, et ça marche.** `encyParseDemoTree()` concatène
   les étapes de tous les blocs de code d'un même niveau dans
   `root.steps`. Les blocs « Mise en place » (étapes 1–5, annotations) et
   « Le coup » (étapes 6–7) forment déjà **une seule liste linéaire de
   sept étapes** dans le même nœud. Les titres `###` qui ne commencent
   pas par `Branche`/`Sous-branche` sont de simples intertitres de
   rédaction, sans effet sur l'arbre. Le mélange est donc acquis, il n'y
   a rien à construire.

2. **L'unité pédagogique est l'étape, pas la démonstration.** Une
   démonstration qui enseigne un motif a presque toujours besoin des
   deux : on montre la batterie sur la position immobile (annotations),
   PUIS on joue le coup qui la libère. Typer la démonstration
   obligerait à couper en deux ce qui est un seul geste d'enseignement.

3. **Un type de démonstration serait une contrainte sans usage.** Aucune
   décision du lecteur ne dépendrait de lui : il lit `coup:` étape par
   étape de toute façon.

**Corollaire à écrire dans FORMAT** : une étape d'annotation qui suit une
étape de coup est parfaitement légitime — elle commente la position
nouvelle. C'est exactement ce que fait l'étape 7 (elle ne joue rien et
parle de la position d'après Ce4+), et c'est le patron à recommander pour
poser une question au joueur.

### 2.4 Règle F8 — les annotations d'une étape jouée décrivent l'APRÈS

À écrire noir sur blanc dans FORMAT :

> **Les `%cal`/`%csl` d'une étape sont lus sur la position que cette
> étape AFFICHE.** Pour une étape d'annotation, c'est la position
> courante ; pour une étape de coup, c'est la position **après** le coup.
> Une flèche qui part de la case que la pièce vient de quitter part donc
> d'une case vide.
>
> Conséquence de rédaction : pour montrer le TRAJET d'un coup, on le
> montre à l'étape d'annotation qui **précède**, pas à l'étape qui le
> joue. Pour montrer ce que le coup a produit, on l'annote sur l'étape
> qui le joue.

Et une **vérification mécanique** qui l'accompagne, à ajouter aux
contrôles de `encyResolveTree()` :

> Sur une étape qui joue un coup, aucune flèche `%cal` ne doit **partir
> de la case de départ du coup** (`step.from`). Sinon : anomalie
> « Étape X : flèche partant de f6, case vidée par le coup de cette
> étape. »

C'est un contrôle **sans faux positif** : la case est vide par
construction (sauf roque, cas à exclure du test). Il n'interdit pas les
cercles sur cases vides, qui sont légitimes (marquer une case de fuite,
comme `Gc8`, `Ge7` à l'étape 7).

### 2.5 Règle F9 — le temps du verbe suit la position

C'est le correctif de fond du décalage constaté. À écrire dans FORMAT,
section « Conventions de prose », en tant que règle **normative pour les
démonstrations** :

> **Une étape parle au temps de sa position.**
>
> - Étape d'ANNOTATION (`coup: —`) : le coup n'est pas joué. Le Fou en
>   parle au **conditionnel ou au futur** — « en plaçant son cavalier en
>   e4, Nataf ouvrira la diagonale », « si le cavalier s'écarte, l'échec
>   partira du fou ». Jamais à l'accompli.
> - Étape de COUP : le coup est joué, la position le montre. Le Fou parle
>   au **présent ou au passé composé** — « le cavalier s'écarte, et
>   l'échec part du fou », « les Noirs doivent maintenant parer ».
>
> Un texte à l'accompli sur une étape d'annotation est une **erreur de
> format**, au même titre qu'un FEN faux : il enseigne quelque chose que
> l'échiquier contredit.

Cette règle ne peut pas être vérifiée mécaniquement (c'est de la langue),
mais elle donne le critère de relecture, et elle nomme le défaut.
Elle vaut aussi pour la clé `cloture:` : la question posée au joueur doit
porter sur la position **affichée**, pas sur une position à venir.

### 2.6 Règle F10 — `cloture:` est un arrêt, pas un masque

> **`cloture:` arrête la démonstration à cette étape.** Le lecteur, sur
> une étape de clôture : ne propose aucune branche, **et ne permet pas
> d'avancer** — la flèche « suivant » et le saut « fin » sont désactivés,
> quelle que soit la place de l'étape dans son nœud. Le retour en arrière
> reste entièrement disponible.
>
> Ce qui suit une clôture reste de la MATIÈRE : lu, rejoué, vérifié au
> chargement (règle v5 inchangée), simplement non atteignable ici.

Ça transforme une coïncidence en garantie, et ça rend `cloture:`
utilisable ailleurs qu'en dernière position.

### 2.7 Ce qui ne change PAS

Explicitement, pour éviter toute dérive :

- La **réinitialisation** (`— réinitialisation`) remet à zéro les
  **annotations seulement**, jamais la position. Une étape de
  réinitialisation ne porte pas de `coup:` et laisse l'échiquier là où il
  est. C'est le comportement actuel ; il est correct et il est désormais
  écrit.
- Les **FEN d'entrée de branche** (v3 F4) restent obligatoires et
  redondants. Ils sont ce qui rend la démonstration jouable **vérifiable**
  au lieu de simplement fonctionnelle.
- Le **cumul** des annotations reste une convention de rédaction : chaque
  étape réécrit sa ligne `%csl`/`%cal` en entier. Le lecteur ne cumule
  pas, il remplace. Rien à changer.
- La **présentation** (v6, premier bloc de citation) reste hors du
  compteur d'étapes.

**Version de format visée : FORMAT v7 — « la démonstration jouée ».**
Les règles F8, F9, F10 et la tolérance `f6-e4` y sont ajoutées. Le
chapeau de `FORMAT.md` annonce encore « Version 5 » alors que le fichier
porte déjà une section `[v6]` : à corriger dans le même geste.

---

## 3. LECTEUR — tenir la position et garder la navigation cohérente

### 3.1 La question posée : rejeu depuis la racine, ou FEN mémorisés ?

**Réponse : les deux, à deux moments différents.** Ce n'est pas un
compromis, c'est la bonne architecture, et c'est déjà celle du code.

- **Au CHARGEMENT — rejeu depuis la racine, une fois.**
  `encyResolveTree(root, fenRoot)` descend l'arbre en profondeur. Pour
  chaque nœud, il part du FEN d'entrée, joue les `coup:` de ses étapes
  dans l'ordre avec `chess.js`, et **écrit `step.fen` sur chaque étape**
  (ainsi que `step.from`, `step.to`, `step.legal`, `step.giveCheck`,
  `step.isMate`). Le rejeu est l'AUTORITÉ : c'est lui qui produit la
  vérité, et c'est pendant qu'il tourne que tous les contrôles se font.

- **À la NAVIGATION — lecture d'index, rien d'autre.** `encyGoto()` fait
  `game = new Chess(step.fen)`. Aucun coup n'est joué au moment de
  naviguer, aucun `undo()`, aucune pile.

### 3.2 Pourquoi c'est le bon choix

**La navigation arrière est exacte et gratuite.** Revenir de l'étape 7 à
l'étape 6, ou de l'étape 6 à l'étape 5, c'est instancier un FEN déjà
calculé. Il n'y a pas d'état à défaire, donc pas d'état à défaire
*mal*. Un lecteur à pile d'annulation aurait à gérer le roque, la prise
en passant, le compteur de demi-coups — et se serait trompé un jour.
Ici la question ne se pose pas : `1r1k3r/…/1pQ2N2/…` reste
`1r1k3r/…/1pQ2N2/…`, indéfiniment.

**Le saut de branche est gratuit lui aussi.** Passer de la branche A à la
branche B, ou remonter à l'embranchement (`encyBackToFork()`), c'est
changer `encyPath` et `encyStep`, puis relire un FEN. Deux branches
sœurs n'ont **aucun état partagé à réconcilier** — ce qui est
exactement ce que demande la règle v3 « deux branches sœurs n'héritent
jamais l'une de l'autre ».

**La vérification est concentrée en un point.** Tout ce qui peut être
faux l'est au chargement, avant que le joueur ne voie quoi que ce soit :
16 contrôles sur l'entrée Nataf, 0 anomalie. Un rejeu paresseux, à la
demande, disperserait les échecs dans le temps et ferait apparaître une
erreur au milieu d'une démonstration.

**La divergence silencieuse reste détectable.** `resolveNode()` compare
le FEN **déclaré** d'une branche au FEN **dérivé** par rejeu et signale
l'écart. C'est ce qui a permis d'attraper les trois FEN faux de la
position Nataf, et c'est la raison d'être de la redondance de v3 F4.

Le coût — recalculer tout l'arbre au chargement — est nul à cette
échelle : onze coups.

### 3.3 Ce qu'il faut modifier dans le lecteur

Les cinq manques du §1, traduits en interventions. Toutes sont locales.

| # | Intervention | Où | Ampleur |
|---|---|---|---|
| 1 | `cloture:` bloque `navNext()` et `navEnd()` | `navNext`, `navEnd`, `updateNav` (l.3697–3765) | ~6 lignes |
| 2 | Contrôle « flèche partant de la case vidée » | `resolveNode()` dans `encyResolveTree` | ~8 lignes |
| 3 | Afficher le coup joué dans le panneau | `encyIdentify()` | ~4 lignes |
| 4 | Animer le déplacement | `encyGoto()` : `render(true)` sous condition | ~3 lignes |
| 5 | Tolérer `coup: f6-e4` | `encyStripMoveNum` / point d'appel de `.move()` | ~10 lignes |

Détail sur les deux qui méritent une décision.

**(1) L'arrêt de navigation.** `updateNav()` calcule déjà
`aLaFin = (encyStep >= n.steps.length-1)` pour griser les flèches. Il
suffit d'y adjoindre la clôture :

> `aLaFin = (encyStep >= n.steps.length-1) || !!n.steps[encyStep].cloture`

et de poser la même garde dans `navNext()` et `navEnd()`. La flèche
« suivant » se grise **d'elle-même**, ce qui rend l'arrêt lisible sans
message : le joueur voit qu'il n'y a plus rien devant. Le retour arrière
reste actif, donc la démonstration se rejoue.

**(4) L'animation.** Décision : **animer, mais seulement quand l'étape
joue un coup**. Sur une étape d'annotation, la position ne change pas —
animer n'aurait rien à animer. Sur une étape de coup, la pièce qui glisse
de f6 à e4 est précisément ce qui distingue une démonstration jouée d'une
suite de diagrammes, et c'est ce que le brief demande à voir. Le retour en
arrière, lui, **ne s'anime pas** : reculer n'est pas un coup, et une
animation inversée suggérerait qu'on « dé-joue ». À vérifier à
l'implémentation : la fonction `render(animate)` existe déjà et est
utilisée ailleurs dans l'application.

### 3.4 Ce qui ne bouge pas dans le lecteur

- `extractVisuals()` — inchangée. Elle lit `%cal`/`%csl`, point.
- `encyParseDemoTree()` / `encyParseStep()` — inchangées hors la
  tolérance `f6-e4`.
- Le modèle d'état (`encyPath`, `encyStep`, `encyMode`) — inchangé.
- `encyClose()`, la boucle liste → entrée → démonstration → entrée —
  inchangée.
- Le verrou de lecture seule (l.3293 : en `encyMode`, on ne joue pas à la
  main sur l'échiquier) — inchangé, et il devient **plus** important : une
  démonstration jouée pourrait donner l'envie de jouer soi-même. Ce sera
  un autre chantier, avec sa propre conception.

---

## 4. COMPATIBILITÉ — ce qui continue de marcher à l'identique

**Confirmé, par exécution du lecteur sur les trois entrées existantes.**

| Entrée | Démonstrations trouvées | Étapes | État |
|---|---|---|---|
| `echec-a-la-decouverte` | 1 | 21 | jouable, 16 contrôles, 0 anomalie |
| `mauvais-fou` | 1 section | **0** | non jouable — dégrade en prose |
| `nataf` | 0 | — | prose seule |

Deux remarques qui comptent.

**`mauvais-fou` n'est pas une démo annotée, c'est une démo non
jouable.** Sa section « Démonstration » n'a ni `**FEN** :` ni bloc
d'étapes au format v4 (elle est écrite en v2). `encyDemoPlayable()`
renvoie faux, et l'entrée affiche la mention prévue par la règle de
dégradation v4 : « Démonstration non jouable en l'état […] Le texte de
l'entrée reste consultable. » **Aucune des interventions du §3.3 ne la
touche** : elles portent toutes sur des étapes résolues, et elle n'en a
aucune. Elle continuera d'afficher exactement ce qu'elle affiche
aujourd'hui.

**Les étapes annotées ne sont modifiées par aucune intervention.** Les
cinq interventions se déclenchent sur `step.cloture` (1), sur une étape
qui joue un coup (2, 3, 4), ou sur le parsing d'une valeur de `coup:` non
vide (5). Une étape `coup: —` sans clôture les traverse toutes sans
effet. La mise en place actuelle de `echec-a-la-decouverte` — étapes 1 à
5 — se comporte donc à l'identique.

**La règle de dégradation reste la protection de dernier rang** : si une
démonstration devient illisible pour une raison quelconque, la prose de
l'entrée s'affiche quand même, et une entrée en échec rend la main à la
fiche courte en dur. Rien de ce qui est proposé ici ne la contourne.

**Deux contrôles de non-régression à passer après implémentation**, avant
toute validation à l'écran : relancer le lecteur hors navigateur sur les
trois entrées et retrouver exactement le tableau ci-dessus (21 étapes,
16 contrôles, 0 anomalie) ; puis relancer `generer_index.py` et vérifier
que `INDEX.json` est inchangé.

---

## 5. CIBLE DE VALIDATION — Ce4+ joué, puis arrêt net

### 5.1 Ce que le mécanisme permet déjà

L'arrêt demandé — jouer réellement Ce4+, puis s'arrêter sur la pause
« que ferais-tu ? », sans jouer ni Rc8 ni Cd6# — est **structurellement
acquis**, et voici par quoi :

1. **Le coup est joué** à l'étape 6 (`coup: 1. Ce4+`). Le cavalier passe
   de f6 à e4 : `step.from='f6'`, `step.to='e4'`, cases surlignées.
2. **L'échec est réel** : le FEN de l'étape 6 met les Noirs au trait sous
   échec, `game.in_check()` est vrai, le roi d8 reçoit la pulsation
   rouge. Ce n'est pas une flèche qui figure un échec — c'en est un.
3. **L'étape 7 hérite de cette position** (`coup: —`, même FEN) et pose la
   question sur la position **où le coup a été joué**. Le Fou dit « les
   Noirs n'ont plus que trois coups » devant un échiquier où c'est vrai.
4. **`cloture: pause` coupe les branches** : `encyRenderBranches()` sort
   sans rien afficher. Ni A ni B ne sont proposées.
5. **Les branches restent de la matière** : A, A.1, A.2 et B sont
   parsées, rejouées et vérifiées au chargement (elles comptent dans les
   16 contrôles), mais ne sont pas atteignables. Elles resserviront
   telles quelles au Top mats.

### 5.2 Ce qu'il reste à faire pour que la cible soit tenue

Deux choses, une par intervention et une par rédaction.

**(a) Rendre l'arrêt garanti et non plus coïncidentiel** — intervention 1
du §3.3. Aujourd'hui la flèche « suivant » est grisée à l'étape 7 parce
que c'est la dernière étape du nœud racine, pas parce que c'est une
clôture. Après l'intervention, elle sera grisée **parce que c'est une
clôture**, et le resterait si une étape 8 était ajoutée au-dessous.

**(b) Réécrire la mise en place pour que les mots suivent la position** —
application de la règle F9 (§2.5). C'est là que se corrige le décalage
rapporté. Deux options, à trancher par toi :

> **Option 1 — mettre les étapes 1 à 4 au conditionnel.** On garde cinq
> étapes d'annotation qui construisent le raisonnement sur la position
> immobile (batterie, masque, destinations candidates e4/e8, coup
> gratuit), toutes au futur : « en s'écartant, le cavalier **ouvrira** la
> diagonale », « l'adversaire **devra** d'abord parer cet échec, il
> **n'aura** pas le temps de s'occuper du cavalier ». Puis l'étape 6 joue,
> et l'étape 7 pose la question.
>
> Coût : quatre reformulations. Bénéfice : la mise en place garde sa
> valeur pédagogique — on voit le motif AVANT de le jouer, ce qui est
> exactement le geste de méthode que l'entrée enseigne (« on ne cherche
> pas un beau coup, on cherche d'abord la ligne éteinte »).

> **Option 2 — déplacer le propos du « coup gratuit » après le coup.**
> On supprime l'étape 4 de la mise en place, et son contenu passe en
> étape d'annotation **après** l'étape 6 : le Fou constate le coup gratuit
> devant l'échec réel. La mise en place tombe à quatre étapes.
>
> Coût : renumérotation. Bénéfice : la phrase la plus concernée par le
> décalage est dite au moment exact où l'échiquier la démontre.

**Ma recommandation : l'option 1, éventuellement complétée par
l'option 2.** L'option 1 seule suffit à supprimer le décalage et respecte
l'ordre d'exposition de l'entrée (constater la batterie, puis la jouer).
L'option 2 renforce le moment de bascule mais renumérote, et une
renumérotation est précisément ce qui a déjà cassé une référence dans
cette entrée (l'ancienne étape 8 devenue 7, cf. FORMAT v5).

Dans les deux cas, **le contenu doctrinal ne bouge pas** : mêmes idées,
mêmes sources, mêmes timecodes, mêmes annotations. Seul le temps des
verbes change. La règle de rigueur de source s'applique telle quelle.

### 5.3 Le critère de réussite, à l'écran

Sur `serveur_echecs.py`, ouvrir « L'échec à la découverte », dérouler la
démonstration et vérifier, dans l'ordre :

1. étapes 1 à 5 : le cavalier **reste en f6**, aucun texte ne parle d'un
   échec existant ;
2. étape 6 : le cavalier **glisse de f6 à e4**, f6 et e4 sont surlignées,
   le roi d8 **pulse en rouge** ;
3. étape 7 : la position ne bouge plus, le Fou pose la question, **aucun
   bouton de branche** n'apparaît, la flèche « suivant » est **grisée** ;
4. retour arrière depuis l'étape 7 jusqu'à l'étape 1 : le cavalier
   **revient en f6**, l'échec disparaît, chaque étape retrouve ses
   annotations ;
5. bandeau de vérification : **0 anomalie**, et le nombre de contrôles a
   augmenté (les nouveaux contrôles de flèche du §2.4 s'ajoutent aux 16) ;
6. ouvrir `mauvais-fou` : mention « non jouable en l'état », prose
   intacte.

---

## 6. Suites — ce que ce document NE fait pas

Ce document est une conception. Restent, dans l'ordre, et chacun après
feu vert :

1. **Écrire FORMAT v7** — règles F8, F9, F10, tolérance `f6-e4`, et
   correction du chapeau resté en « Version 5 ».
2. **Implémenter** les cinq interventions du §3.3 dans `Papu_Chess.html`.
3. **Réécrire la mise en place** de `echec-a-la-decouverte` selon
   l'option retenue au §5.2.
4. **Contrôles de non-régression** hors navigateur (§4) et
   `generer_index.py`.
5. **Validation à l'écran** sur `serveur_echecs.py`, selon les six points
   du §5.3.

Rien de tout cela n'est engagé à ce stade.
