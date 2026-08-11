---
partie: luisjabierr-papu_san-2026-08-11
date: 2026-08-11
joueur: Papu_san (Noirs)
resultat: "0-1 (gain au temps ; les Blancs n'ont jamais joué le coup 16, pendule écoulée avec >14 min)"
statut: matière source vérifiée — non encore formatée en entrée d'encyclopédie
---

# LuisJabierr–Papu_san, 2026-08-11 — l'étreinte à retardement

## Position clé
Blancs au trait, coup 16 (jamais joué).
FEN : `r4rk1/p3np2/2nbb2p/q1p1p1p1/2PpP1P1/3P1P1N/PQ1NB2P/1RB1K2R w K - 2 16`

## Faits vérifiés (chess.js 0.10.3 embarqué — mécanisme, in-app)
- Cavalier d2 **absolument cloué** par la dame a5 sur le roi e1
  (diagonale a5-b4-c3-d2-e1 dégagée sauf le cavalier). → Nb3 illégal.
- Fou c1 : **zéro coup légal** (muré par son propre Cd2 et sa propre Db2).
  → Ba3 illégal. Les deux mineures blanches sont hors-jeu.
- **O-O est légal** : e1/f1/g1 vides et non attaquées, droits intacts.
  C'est l'unique coup qui déclouerait le cavalier.

## Jugement moteur (Stockfish 16, prof. 26 — élaboré, hors-app)
- Position : ≈ **−2,1** (vue Blancs). Meilleure défense = **Qa3**
  (échange de dames pour desserrer l'étau).
- Après **16.O-O** : ≈ −2,5. La bouée est légale mais ne sauve pas.
- Plan noir **16.O-O Rab8 17.Qa3 Rb6** : ≈ −1,85. La batterie …Rb6
  apparaît dans la ligne principale de Stockfish elle-même.

## Ce que la partie enseigne
Une étreinte qui **repose sur un clouage contre un roi non roqué** porte un
compte à rebours : le **roque adverse**. Tant que le roi campe en e1, le
cavalier est gelé et le fou muré ; l'instant où il roque, tout se dénoue.
On presse **avant** O-O, ou on ne presse pas. Ici la pendule a signé avant
la conversion — mais l'échiquier disait déjà +2 pour les Noirs.

Note de provenance : légalité = chess.js (vérité in-app) ; évaluations =
Stockfish (externe, élaboré). Distinction mécanisme / jugement respectée.
