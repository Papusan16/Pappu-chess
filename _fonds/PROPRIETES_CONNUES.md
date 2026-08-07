# Propriétés connues

Les comportements de l'application qui **surprennent sans être des
pannes** : ce qu'elle fait est ce qu'elle doit faire, compte tenu de son
architecture — mais rien, à l'écran, ne le dit.

**Pourquoi ce fichier existe.** Ces constats vivaient dans
`RESTE_A_FAIRE.md`, où ils ne pouvaient qu'y pourrir : ce ne sont pas des
tâches, ils ne seront jamais « faits », donc jamais fermés. Pire, mêlés à
des chantiers, ils se lisent comme des bugs en attente de correction.

Le rôle de ce fichier est de **couper court à la troisième enquête** :
quand un comportement surprend, on regarde ici **avant** de rouvrir le
code. S'il y figure, la panne est déjà comprise — inutile de la
rechercher une fois de plus.

**Forme d'une entrée** : ce qu'on observe, la **cause** dans
l'architecture, le **contournement** immédiat. Et, si la propriété appelle
un jour une action, le renvoi vers l'item de `RESTE_A_FAIRE.md` qui la
porte — la propriété décrit, elle ne planifie pas.

> **Une propriété n'est pas un acquittement.** Elle dit « c'est expliqué »,
> jamais « c'est bien ainsi ». Plusieurs mériteront d'être corrigées ; ce
> qu'elles ne méritent pas, c'est d'être rediagnostiquées.

---

## 1. Les cercles structurels restent muets sur une position posée seule

**Ce qu'on observe.** On charge une position (FEN nu, ou PGN à en-tête
`[SetUp "1"]/[FEN ...]` sans le moindre coup), on attend un cercle
d'avant-poste, de pion passé ou de mauvais fou — rien ne s'affiche. La
position s'y prête pourtant de façon évidente.

**Cause.** Le détecteur de mauvais fou et ses voisins
(`fouOutpostSquares`, `fouPassedPawns`, `fouHangingSquares`) ne lisent pas
la position : ils **rejouent `fullMoves[0..mi]`**, tableau rempli par
`syncFull()` / `game.history()`. Avec `fullMoves` vide — zéro coup importé
—, `mi` n'a pas de sens et la fonction retourne `[]`. Le second point
d'appel (panneau coach, ligne ~3670) est de surcroît gaté par `cursor>0`,
et `cursor` vaut lui aussi 0 sans coup.

C'est une propriété de l'architecture, pas un défaut localisé :
**`mi`/`cursor` sont la seule notion de « position courante »** que
l'application possède. Une position sans historique n'a, pour elle,
pas de présent.

**Contournement.** Fournir **au moins un coup à naviguer** — un PGN avec
historique, même minimal — et avancer d'un coup. Les cercles structurels
apparaissent alors normalement.

---

## 2. Les quatre détecteurs rejouent depuis la position de départ standard

**Ce qu'on observe.** Rien, tant qu'on teste sur une partie normale. Sur
un PGN à en-tête `[SetUp "1"]/[FEN ...]`, les cercles structurels
désignent des cases qui ne correspondent pas à la position affichée.

**Cause.** Ces quatre fonctions rejouent **toujours** depuis
`new Chess()` — la position de départ standard —, **jamais** depuis
`new Chess(startFen)`. Les mêmes `{from,to}` sont donc rejoués depuis la
mauvaise base, et l'analyse porte sur une position fantôme.

Contrairement à la propriété 1, celle-ci est un **bug latent** : sans
conséquence tant que le départ est standard, faux dès qu'il ne l'est
plus. Repéré en marge, jamais déclenché en usage réel — l'application
n'a pas encore de démonstration posée sur FEN non standard.

**Contournement.** Aucun à l'exécution. En attendant la correction :
**ne pas se fier aux cercles structurels sur une démonstration à FEN de
départ non standard.** La propriété 1 masque d'ailleurs souvent
celle-ci — sans coup, rien ne s'affiche du tout.

**Action associée.** Correction portée par `RESTE_A_FAIRE.md`, chantier 4
(*dès que* : l'analyse structurelle doit couvrir une démonstration posée
sur FEN non standard).

---

## 3. Les flèches de conseil du Fou sont là au coup 0 d'une partie importée

**Ce qu'on observe.** On importe une partie ; **avant même d'avancer d'un
coup**, le Fou trace ses flèches de conseil. Elles semblent commenter une
partie qu'on n'a pas commencé à lire.

**Cause.** `pgnMode` est actif dès l'import, sans être gaté sur
`curseur > 0` : la position de départ est traitée comme une position de
jeu ordinaire, et le Fou y conseille comme partout ailleurs.

**Contournement.** Avancer d'un coup : l'affichage redevient cohérent.
La gêne est jugée négligeable — les flèches sont justes, elles sont
seulement prématurées.

**Action associée.** Masquage éventuel porté par `RESTE_A_FAIRE.md`,
chantier 6.
