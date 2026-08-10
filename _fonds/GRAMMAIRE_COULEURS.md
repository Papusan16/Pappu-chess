# Grammaire des couleurs de l'échiquier

Document de conception, décidé avec Flavien. Il fixe le sens des
couleurs sur le plateau avant l'implémentation ; il ne décrit pas l'état
actuel de `Papu_Chess.html`. Les valeurs d'opacité sont des points de
départ à confirmer à l'œil, sur le vrai plateau.

---

## Principe fondateur

**Le FOND dit ce que la case EST.** C'est un fait échiquéen, calculé sur
la position. Il survit au mode Éteint.

**Le CERCLE dit ce que le Fou MONTRE.** C'est une voix intentionnelle,
un choix de commentaire. Il s'efface en mode Éteint.

Deux langages qui ne parlent jamais de la même chose — donc qui ne
peuvent pas se contredire. C'est l'extension de la distinction
fait / voix déjà posée dans le projet : le halo d'échec survit à
l'Éteint, les annotations violettes non.

---

## Les fonds — l'état de la case

Principe de rendu : **teinter, pas repeindre**. La case garde sa couleur
d'origine, le fond la colore. Fondu rapide à l'apparition comme à la
disparition.

| État | Fond | Opacité de départ |
|---|---|---|
| neutre | aucun | — |
| roi désigné, pas encore en échec | bleu doux | ~34 % |
| case libre pertinente (fuite, respiration) | vert doux | ~32 % |
| case menacée / tenue par l'adversaire | orangé doux | ~34 % |
| roi en échec | **aucun fond ajouté** | — |

**Le roi en échec ne reçoit pas de fond.** Le halo pulsé rouge existant
(`#e23b3b`, contour interne pulsé + lueur externe) tient déjà ce rôle.
Le doubler d'un fond dirait deux fois la même chose et affaiblirait les
deux signaux.

**Transition désigné → en échec.** Le fond bleu s'efface à l'instant où
le halo s'allume. C'est l'« embrasement », version halo : un seul signal
prend la case, sans chevauchement.

**Règle d'arbitrage — une case n'a qu'UN fond.** Si deux faits se
disputent la case, l'ordre est :

1. halo d'échec
2. menace
3. libre
4. désigné

Si le conflit oppose un fait et un avertissement du Fou : le fait reste
au fond, l'avertissement passe au cercle. Les deux canaux ne se
disputent jamais la même case, puisqu'ils ne disent pas la même chose.

---

## Les cercles — la voix du Fou

S'effacent en mode Éteint.

**La couleur dit le CAMP.**

- teal — moi
- magenta `#D6409F` — l'adversaire

**Le violet `#8b5cf6` reste réservé à la signature du Fou** — « le Fou
parle ». Ne jamais le réaffecter à un camp.

**Le style dit le RÔLE.**

- trait plein — pièce agissante
- pointillé — trajectoire, ligne de mire
- trait épais — motif (fourchette, clouage…)

Deux informations, deux canaux : la couleur et le style. Jamais la même
variable pour deux sens — c'est ce qui évite les collisions quand un
cercle doit dire à la fois « à qui » et « quoi ».

---

## Coexistence avec l'existant

Relevé du 2026-08-07, cf. `_sessions/2026-08-07.md`.

**Fonds déjà présents** : sélection en vert 40 %, dernier coup joué en or
28 / 45 %.

À vérifier à l'œil : le vert « case libre » ne doit pas se confondre avec
le vert de sélection. Si les deux se ressemblent trop en usage, ajuster
l'un des deux à l'implémentation.

**Sept tokens échiquier existants**, qui ne basculent pas entre thème
clair et thème sombre. La grammaire des couleurs échiquéennes reste donc
fixe à travers les thèmes, comme la barre d'éval.

---

## Points ouverts pour l'implémentation

À trancher sur le vrai plateau, pas sur le papier :

- les opacités exactes des trois fonds doux, et la lisibilité des pièces
  par-dessus ;
- la cohabitation du vert « case libre » et du vert de sélection.

**Point à reprendre avec Flavien.** La session du 2026-08-07 avait
retenu `#971187` pour le camp adverse (teinte 334° OKLCH), avec un
décalage du teal de 195° vers 216° (`#0e8fa8`) pour tenir l'écart avec le
vert. Le présent document fixe le magenta à `#D6409F`. Les deux valeurs
ne sont pas interchangeables : le choix du 07 venait d'un calcul de
séparation en vision déficiente. Il faut décider laquelle des deux fait
foi avant de câbler quoi que ce soit.

---

## Implémentation (2026-08-09)

Ce que le code fait réellement, à date, sur `wip-fonds-couleurs`
(commits `b5861bb`, `9caddd8`, `da24c51`) — cette section acte l'état du
code, elle ne remplace pas la conception ci-dessus.

**Rendu.** Les trois fonds sont des classes CSS posées sur la
`<div class="sq">`, sur le modèle exact de `.in-check` — jamais le layer
SVG des cercles/flèches. Un fait d'échiquier est un état de case, pas une
annotation dessinée. Valeurs retenues, fixes à travers les thèmes clair
et sombre (comme les sept tokens échiquier existants) :

- `.bg-menacee` — orangé, `rgba(224,108,58,.34)`
- `.bg-libre` — vert, `rgba(16,150,110,.32)`
- `.bg-designe` — bleu, `rgba(59,130,246,.34)`

**Notation.** Tag `[%bg ...]`, sur la même ligne que `%csl`/`%cal`, deux
formats cohabitant dans la même liste séparée par virgules :

- **piloté** — lettre dédiée (jamais R/G/B/Y des cercles) + case :
  `O`=menacée, `V`=libre, `D`=désigné. Ex. `[%bg Oe5,Vd4,De4]`.
- **calculé** — mot-clé + `:` + case. Un seul mot-clé à ce jour :
  `menace`. Ex. `[%bg menace:c6]` — chess.js vérifie si la case est
  réellement attaquée par l'adversaire du camp au trait ; orangé si oui,
  rien sinon (pas de fond « refusé » visible, juste une absence).

**Détection automatique de la menace.** Repose sur chess.js étendu :
méthode `attacked(color, square)` exposée le 2026-08-09 dans la
librairie vendored (0.10.3) — elle existait déjà en interne, utilisée
par `in_check()` et le roque, seulement pas accessible au reste du code.
Une ligne ajoutée, aucun calcul modifié. Choisie plutôt que
`moves({verbose:true})` parce que cette dernière ne détecte pas une case
VIDE tenue uniquement par un pion en diagonale (elle ne génère un coup de
pion vers une diagonale que si elle est occupée par l'adversaire, ou en
prise en passant) — un faux négatif silencieux que `attacked()` ne fait
pas.

**Rythme : une désignation vaut pour une étape.** `fouBackgrounds` est
recalculé à chaque étape/coup affiché (`identify()`/`encyIdentify()`),
sans persistance de l'étape précédente — comme les cercles et flèches du
Fou. Ce n'est pas un oubli à corriger : c'est le choix de rythme
pédagogique déjà en place pour la voix du Fou, étendu au fait de la
case.

**Ce qui reste piloté, pas calculé.** Le vert « case libre » (`V`) et le
roi désigné (`D`) restent des choix de jugement pédagogique — quelle
case mérite d'être montrée comme « libre » ou quel roi mérite d'être
« désigné » n'est pas (encore) un fait calculable de la même façon que
la menace. Seule « menace » est automatisée aujourd'hui.

**Point tranché : cohabitation des deux verts.** Vérifiée à l'écran
(Chromium) : le vert « case libre » (émeraude soutenu, `16,150,110`) et
le vert de sélection existant (menthe pâle, `--case-selection:
rgba(127,201,127,.4)`) sont jugés distinguables l'un de l'autre à l'œil.
Le point ouvert soulevé plus haut dans ce document est résolu.
