# Journal d'avancement — Papu Chess

Mis à jour en fin de session. Une nouvelle conversation commence par
"relis PRINCIPES.md et JOURNAL.md".

## Fait récemment
- Halo rouge d'échec (fait de position) + primitive cercle du Fou
  (voix) : câblés.
- Récolement transcripts Marc Quenehen : 2 chaînes, ~880 vidéos
  valides, 9 échecs irrécupérables. Dans _doctrine/ et Marc Quenehen/.
- 9 index de contenu (A–I) construits. G stérile (fermée), C traité
  (fiches d'ouverture), H → doctrine couleur.
- doctrine_couleur_synthese.md : synthèse de la doctrine signature de
  Marc (axiome, loi arithmétique, loi de conservation, mauvais fou,
  verrou, échange). En grande partie calculable.
- Détecteur de MAUVAIS FOU câblé (analyse seulement) : 3 critères
  (≥2 pions gêneurs amis sur la couleur du fou, mobilité ≤4 cases,
  gêneurs fixés). Cercle violet + phrase du Fou. NON ENCORE VALIDÉ
  sur position réelle.
- personnes.md : 9 fiches biographiques (format PEOPLE), local.

## À valider
- Détecteur de mauvais fou : tester sur une française d'avance fermée
  (fou c8 muré) → doit détecter ; sur un fou sorti devant sa chaîne
  → doit se taire. Caler les seuils.
- Vérifier que le mode Éteint coupe AUSSI les cercles en analyse
  (le gate mauvais fou doit tester fouMode !== 'off', pas seulement
  playMode).

## Prochains chantiers (ordre indicatif)
- Schéma de données d'un EXERCICE (position FEN, type, consigne,
  réponses, explication, source). À figer avant de peupler.
- Peupler les exercices depuis les "mettez en pause" du corpus Marc
  (déjà repérés dans la doctrine couleur).
- Suite de la doctrine couleur calculable : comptage de couleur,
  détection du verrou.
- Catégories d'index encore à arbitrer : A, E, F, I.
- Fiches personnes + repertoire_C à insérer dans OPS/PEOPLE.
- Sous-doctrine "fous de couleurs opposées" (repérée, non traitée).
