# Mauvais fou — définition refondue (proposition, non codée, non validée)

Document de travail exporté pour partage/relecture externe. Rien de ce
qui suit n'est appliqué à `Papu_Chess.html` ni committé — c'est la
définition en cours de discussion avant implémentation.

## Résultat — verdicts sur les positions de test

| Position | A (cases sûres) | B (gêneurs fixés durablement) | C (pions fixés sur la couleur, N=3) | Développement (seuil=3) | **Verdict final** |
|---|---|---|---|---|---|
| coup 7 — fou f8 | 2 | non | 0 | `g6` puis rien, ou `g6+Bg7` → 4 cases sûres | **non détecté** |
| coup 12 — fou f8 | 0 | non | 0 | `g6` puis `Bg7` → 4 cases sûres | **non détecté** |
| coup 14 — fou f8 | 2 | non | 1 | aucun pion poussable (g7 bloqué par son propre cavalier en g6) | **non détecté** |
| coup 15 — fou f8 | 2 | non | 1 | aucun pion poussable | **non détecté** |
| Française fermée — fou c8 | 0 | **oui** | **3** | `b6` (fou reste) → 2 seulement ; `b6+Bb7` → 2 seulement | **MAUVAIS FOU DÉTECTÉ** |

Cas le plus parlant : **coup 12**, le fou f8 a déjà 0 case sûre
*actuellement* (A=0) — il aurait pu être signalé à tort avec la seule
définition A+B+C. Le critère de développement le sauve explicitement :
`g6` puis `Bg7` amène le fou sur la grande diagonale avec 4 cases sûres
(`f8,h6,f6,e5`). Pour la Française, aucun des deux plans testés (pousser
`b7-b6`, avec ou sans relocalisation du fou) ne dépasse 2 cases sûres —
pas d'issue court terme, verrouillage confirmé.

## Comment le critère de développement est calculé

Pour chaque pion ami qui est le **premier obstacle immédiat** (distance
1) sur une des diagonales du fou :

1. **Motif extension** : simuler la poussée de ce pion (1 ou 2 cases,
   chess.js donne la légalité), fou immobile, remesurer sa mobilité sûre
   sur place.
2. **Motif fianchetto** : même poussée, puis simuler le fou se
   relocaliser sur la case tout juste vacée, remesurer sa mobilité sûre
   *depuis cette nouvelle case*.
3. Garder le meilleur des deux résultats. Si le meilleur ≥ seuil
   (proposé 3, comme N) → potentiel de développement intact → **le fou
   n'est pas signalé**, quels que soient A/B/C.

## Définition complète (pseudocode)

```
function isBadBishop(bishopSq):
    # A — mobilité sûre nulle (gate dur)
    safe = legalMoves(bishop) filtered by SEE_1ply >= 0
    if len(safe) > 0: return false

    # B — étouffement par PIONS fixés durablement (pas pièce de passage)
    pawnBlockers = first-obstacle-per-diagonal where (type==pawn AND color==ami)
    if len(pawnBlockers) < 2: return false
    if NOT all(pawnBlockers, fixed_by(occupied_by_pawn OR held_by_enemy_pawn)): return false

    # C — comptage de couleur (doctrine Marc)
    sameColorFixedPawns = count(pions amis fixés sur la couleur du fou)
    if sameColorFixedPawns < N: return false          # N à calibrer, proposé 3

    # D — potentiel de développement court terme
    best = 0
    for each pawnBlocker at distance 1:
        for each legal push of that pawn (1 ou 2 cases):
            simulate push
            best = max(best, safeMobility(bishop, même case))          # extension
            if bishop can move onto vacated square:
                simulate relocation
                best = max(best, safeMobility(bishop, case libérée))    # fianchetto
    if best >= DEV_THRESHOLD: return false             # seuil à calibrer, proposé 3 aussi

    return true   # mauvais fou confirmé : A + B + C + pas d'échappatoire à court terme
```

## Sûr vs approximatif

**Sûr :**
- Légalité des poussées de pion (chess.js, vérité terrain)
- Calcul de la mobilité sûre avant/après (réutilise exactement la même
  brique SEE déjà validée pour A)
- Le motif fianchetto (relocalisation) est une simulation déterministe,
  pas une heuristique

**Approximatif, assumé :**
- Le plan est joué « tout seul », **sans modéliser la réplique adverse**
  entre les deux demi-coups (l'adversaire pourrait par exemple
  réoccuper la case juste libérée, ou attaquer le pion qui avance) —
  même niveau de simplification que B accepte déjà pour « fixé », donc
  cohérent, mais c'est une hypothèse, pas une preuve.

**Risqué, à calibrer :**
- Le seuil « nettement meilleure » (proposé 3, comme N) — aucune source
  doctrinale, choix d'ingénierie
- Le choix de ne tester QUE le pion immédiatement adjacent au fou (pas
  de plans plus indirects, ex. pousser un pion à distance 2 deux fois,
  ou un échange de pièce qui dégagerait la diagonale) — couverture
  volontairement restreinte ; le risque résiduel penche vers des faux
  positifs sur des développements plus subtils non détectés, pas vers
  de nouveaux faux négatifs.

## Rappel du reste de la définition (sessions précédentes)

- **A — mobilité sûre** : coups légaux du fou (chess.js) filtrés par
  SEE 1 coup (même profondeur que `fouHangingSquares`, réflexe M1) :
  une case n'est « sûre » que si le fou n'y est pas capturable
  gratuitement.
- **B — étouffement durable par des pions** : sur chaque diagonale, le
  premier obstacle doit être un pion ami ; ce pion doit lui-même être
  « fixé » (case d'avance occupée par un pion — ami ou ennemi — ou
  tenue par un pion adverse). Une pièce mobile de passage (cavalier,
  dame…) sur la case d'avance NE compte PAS comme fixation.
- **C — comptage de couleur (doctrine Marc, sourcée dans
  `_doctrine/Mauvais Fou.txt`)** : nombre de pions amis fixés sur des
  cases de la même couleur que le fou. Pas de seuil chiffré chez Marc
  (vérifié par recherche exhaustive dans le fonds — voir
  `RESTE_A_FAIRE.md`) ; N=3 est une proposition d'ingénierie, à valider.

## Statut

Rien n'est codé ni committé. En attente de validation sur :
1. Le seuil de développement (3 ?) — même valeur que N, ou indépendant ?
2. Le seuil N du comptage de couleur (3 ?)
3. Feu vert global sur la définition avant implémentation dans
   `Papu_Chess.html`.
