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
