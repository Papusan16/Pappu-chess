# Personnes — fiches au format PEOPLE de Papu_Chess.html

## 0. Format `PEOPLE` observé (13 entrées existantes)

Objet JS `PEOPLE={...}` (même ligne minifiée que `OPS`, ligne 2462). Schéma exact de chaque
entrée (mêmes clés, dans cet ordre, pour les 13 entrées existantes) :

```json
{
  "name": "Richard Réti",
  "life": "1889 – 1929",
  "country": "Tchécoslovaquie",
  "role": "Grand maître, théoricien hypermoderne",
  "bio": "Figure de proue de l'école hypermoderne des années 1920, Réti montra qu'on pouvait contrôler le centre sans y placer ses pions. Son ouverture (1.Cf3 suivi de c4 et fianchetto) porte son nom. Il battit Capablanca avec en 1924, mettant fin à huit ans d'invincibilité du Cubain — un coup de tonnerre.",
  "openings": ["Début Réti"]
}
```

- `openings` : tableau de **chaînes de texte libres** (noms d'ouvertures), pas d'ids vers `OPS`.
  Le lien avec `OPS` se fait dans l'autre sens : chaque entrée `OPS` porte un champ `"person": "<clé
  PEOPLE>"` qui pointe vers cet objet (ex. `OPS["reti"].person === "reti"` → `PEOPLE["reti"]`).
- **Un lien `OPS` n'est pas obligatoire** : l'entrée `PEOPLE["alekhine"]` existe (Alexandre Alekhine,
  1892–1946, 4e champion du monde) avec `"openings": ["Défense Alekhine"]`, alors qu'**aucune entrée
  `OPS` de type "défense Alekhine" n'existe** dans le tableau actuel (12 entrées `OPS`, aucune avec
  `person: "alekhine"`). Donc le schéma tolère très bien une fiche `PEOPLE` orpheline, sans ouverture
  `OPS` correspondante. C'est le précédent que je suis pour Kasparian / Denker / Andruet ci-dessous.
- `country: "—"` existe aussi (entrée `scholar`, qui n'est pas une vraie personne mais un piège
  nommé) — autre signe que le champ tolère l'absence d'info plutôt que de forcer une valeur.
- Les 12 clés `PEOPLE` liées à une ouverture `OPS` : ruylopez, italian, sicilian, french, caro, pirc,
  scandinavian, queensgambit, indian, reti, english, scholar. Plus `alekhine`, orpheline (13e).

Ce fichier est un brouillon de travail, pas encore inséré dans `Papu_Chess.html`.

---

## 1. William Davies Evans

**Lien OPS** : ⚠️ aucun. Il n'existe **aucune entrée `gambit-evans` (ou similaire) dans `OPS`**
actuellement (12 entrées vérifiées, aucune ne mentionne Evans). Fiche orpheline pour l'instant,
comme `alekhine`.

Source : `Gambit Evans  variante agressive de l'ouverture italienne/transcript.txt` — 0:02–1:02

```json
{
  "name": "William Davies Evans",
  "life": "né en 1790",
  "country": "Pays de Galles",
  "role": "Capitaine de marine",
  "bio": "Gallois né en 1790, engagé très tôt dans la marine, capitaine à 30 ans. Particularité : il a appris les échecs tard, vers 27-28 ans, auprès d'un officier de marine. Il a aussi inventé un système de lanternes à trois couleurs évitant les collisions nocturnes de navires, invention récompensée par le gouvernement anglais et par les tsars de Russie (qui lui offrent des objets en or, dont une montre). Il meurt malgré tout dans la pauvreté ; juste avant sa mort, des joueurs d'échecs de l'époque se cotisent pour l'aider.",
  "openings": ["Gambit Evans"]
}
```

*Fidélité à la source* : le transcript dit qu'Evans a appris "auprès d'un officier de marine", pas
qu'il était lui-même officier de marine marchande ayant appris à bord d'un bateau — nuance déjà
signalée dans `figures_racontees.md`.

---

## 2. Genrikh Kasparian

**Lien OPS** : ⚠️ aucun — la vidéo source (`Brillant et Mat !`) analyse une position de composition,
pas une ouverture nommée. Fiche orpheline, comme `alekhine`.

Source : `Brillant et Mat !/transcript.txt` — 0:01–0:31

```json
{
  "name": "Genrikh Kasparian",
  "life": "1917 – v. 1989-90",
  "country": "Arménie",
  "role": "Joueur et compositeur d'échecs",
  "bio": "Joueur d'échecs arménien du 20e siècle, né en 1917, décédé vers 1989-90. Présenté comme un possible « joueur d'échecs le plus ingénieux de l'histoire ». Surtout connu comme excellent compositeur, créateur de problèmes et de positions très astucieuses.",
  "openings": []
}
```

---

## 3. Arnold Denker

**Lien OPS** : ⚠️ aucun. Fiche orpheline.

Source : `De la Boxe aux Echecs ! 🥊♟️/transcript.txt` — 0:01–1:49

```json
{
  "name": "Arnold Denker",
  "life": "né en 1914",
  "country": "États-Unis (Bronx, New York)",
  "role": "Joueur d'échecs, ancien boxeur",
  "bio": "Né en 1914 dans le Bronx, à New York. Jeune boxeur prometteur à l'origine. Il découvre les échecs par ses camarades d'études, qui jouaient des parties à la cafétéria avec de petits paris d'argent ; il perdait faute de niveau. Il va alors emprunter à la bibliothèque de son école un livre d'Emmanuel Lasker (champion du monde de l'époque), intitulé « Sens commun aux échecs ». Après cette lecture, il commence à gagner. Les échecs ne le quitteront plus : six fois champion du club Marshall (l'un des deux plus grands clubs d'échecs des États-Unis), double champion des États-Unis en 1944 et 1946, puis organisateur et financeur d'événements. Il devient le troisième joueur de l'histoire à recevoir le titre de « doyen des échecs américains » de la fédération américaine.",
  "openings": []
}
```

*Note transcription* : le nom "Denker" est mal retranscrit à plusieurs endroits de la même vidéo
("wenger", "de tencate"/"tira" en tout début, puis "enker" à 1:41 où le son se rapproche enfin de
"Denker") — même phénomène de sous-comptage phonétique déjà documenté pour Caro-Kann.

---

## 4. Judit Polgár

**Lien OPS** : ⚠️ aucun.

Source : `Judit Polgar ou la vraie Beth Harmon des échecs !/transcript.txt` — 0:02–0:58

```json
{
  "name": "Judit Polgár",
  "life": "née en 1976",
  "country": "Hongrie",
  "role": "Championne d'échecs",
  "bio": "Championne d'échecs hongroise née en 1976, dont la trajectoire et l'ascension vers les sommets rappellent le personnage d'Elizabeth Harmon dans « Le Jeu de la Dame ». Fille d'un père pédagogue, atypique pour l'époque, qui voulait que ses filles excellent dans plusieurs domaines : échecs, mais aussi mathématiques et plusieurs langues (russe, allemand, espéranto). Elle entre dans le top 10 mondial et bat, à 15 ans, le record de précocité pour le titre de grand maître international — record que détenait Bobby Fischer depuis 33 ans. Dans son ascension, elle rencontre une hostilité liée à son sexe : le jeu des femmes était méprisé à l'époque, avec des commentaires négatifs de plusieurs anciens champions, dont Kasparov.",
  "openings": []
}
```

---

## 5. Napoléon Marache

**Lien OPS** : ⚠️ aucun.

Source : `Magnifique Mat de Morphy ! 🤩/transcript.txt` — 0:56–1:29

```json
{
  "name": "Napoléon Marache",
  "life": "né trois jours après la défaite de Waterloo",
  "country": "France (Meaux) / États-Unis",
  "role": "Joueur et auteur d'échecs",
  "bio": "Né à Meaux (France) trois jours après la défaite de Waterloo — d'où son prénom, choisi par ses parents. Émigre aux États-Unis à 12 ans, où il devient un bon joueur. Il remporte un tournoi à New York face aux meilleurs joueurs des États-Unis, et écrit l'un des premiers livres d'échecs du continent américain, couplé à des règles et stratégies de backgammon. Il affrontera ensuite Paul Morphy.",
  "openings": []
}
```

---

## 6. Gilles Andruet

**Lien OPS** : ⚠️ aucun.

Source : `Météore dans le monde des échecs/transcript.txt` — 0:01–1:21

```json
{
  "name": "Gilles Andruet",
  "life": "1958 – (décédé quelques années après 1990)",
  "country": "France",
  "role": "Joueur d'échecs, champion de France",
  "bio": "Joueur d'échecs français né en 1958, au destin présenté comme tragique. Champion de France en 1988, décrit comme un joueur brillant à la personnalité originale, atypique, parfois perturbatrice et agaçante — plusieurs altercations avec d'autres joueurs professionnels. En 1989, en passe de devenir champion de France une deuxième fois, il quitte le tournoi après une altercation avec Jean-Luc Seret (autre ancien champion de France). La partie présentée dans la vidéo, jouée en 1990 contre Philippe Guyot, l'a été peu de temps avant sa mort, survenue quelques années plus tard (cause non précisée dans la source). Il s'était mis à jouer au casino : sa mémoire phénoménale lui permettait de compter les cartes au blackjack, ce qui lui a valu d'être interdit de blackjack par les casinos ; il s'est alors tourné vers la roulette, où cette capacité ne lui permettait plus de gagner.",
  "openings": []
}
```

*Fidélité à la source* : la cause du décès n'est pas donnée dans le transcript — volontairement non
complétée.

---

## 7. Blackburne / Steinitz — l'anecdote des parties à handicap

**Lien OPS** : ⚠️ aucun (pas d'ouverture "Blackburne" dans `OPS`). Concerne deux figures à la fois —
le schéma `PEOPLE` étant une fiche par personne, deux fiches distinctes ci-dessous, reliées par
la même anecdote.

Source : `LA MORT NOIRE — quand BLACKBURNE FRAPPE sans pitié/transcript.txt` — bio 0:02–1:00,
anecdote Steinitz 11:39–14:03

```json
{
  "name": "Joseph Henry Blackburne",
  "life": "fin du 19e siècle",
  "country": "Angleterre",
  "role": "Joueur d'échecs, surnommé « la Mort Noire »",
  "bio": "Joueur de la fin du 19e siècle, l'un des derniers représentants dignes de l'ère romantique de l'attaque à tout-va. Longue barbe noire, style très agressif, d'où son surnom « la Peste Noire » ou « la Mort Noire ». Connu pour des schémas de mat originaux et spectaculaires. Il jouait énormément de parties, contre le tout-venant comme contre les meilleurs joueurs, parfois pour de petites sommes d'argent, et donnait souvent des parties à handicap (avec des pièces en moins) à des joueurs plus faibles — il les gagnait presque toutes.",
  "openings": []
}
```

```json
{
  "name": "Wilhelm Steinitz",
  "life": "contemporain de Blackburne",
  "country": "—",
  "role": "Premier champion du monde officiel",
  "bio": "Premier champion du monde officiel, contemporain de Blackburne. Raconte, en interview, une anecdote : à Londres, un joueur amateur l'aborde dans un lieu dédié aux échecs pour lui demander comment mieux se défendre contre la défense des deux cavaliers. Ne comprenant pas bien la demande, Steinitz propose à l'amateur de s'asseoir et lui montre une variante où l'on sacrifie un cavalier sur f7. L'amateur, gêné, précise alors que ce n'est pas ça qu'il demandait : il a l'habitude de jouer contre Blackburne, qui lui offre toujours deux cavaliers en partie à handicap, et il perd toujours — il voulait savoir comment mieux se défendre dans CE cas précis. Steinitz avoue que cette possibilité ne lui avait pas traversé l'esprit.",
  "openings": []
}
```

---

## 8. Amos Burn / Frank Marshall — l'anecdote de la pipe

**Lien OPS** : ⚠️ aucun.

Source : `LA PIPE DE BURN — le CALME AVANT LA TEMPÊTE./transcript.txt` — 0:01–6:44 (récit complet,
entrelacé avec les coups de la partie)

```json
{
  "name": "Amos Burn",
  "life": "52 ans au moment de la partie (donc né v. 1848)",
  "country": "—",
  "role": "Joueur d'échecs, adversaire de Frank Marshall",
  "bio": "Adversaire de Frank Marshall dans une partie de 1900 (Marshall a 33 ans, Burn en a 52). Décrit par Marshall comme un joueur plutôt défensif, très solide, aimant les structures de pions fermées et le jeu positionnel. Il aimait jouer de longues heures en fumant sa pipe (autorisé à l'époque). Pendant la partie, Marshall raconte le rituel de Burn avec sa pipe — la chercher, la nettoyer, la remplir de tabac, chercher ses allumettes — en parallèle des coups joués, jusqu'à ce que Burn parvienne enfin à l'allumer... juste au moment où Marshall joue un coup gagnant (sacrifice de tour en h8, menant à un mat forcé). Burn assiste au mat avec humour ; les deux joueurs se serrent la main, la pipe s'éteint.",
  "openings": []
}
```

```json
{
  "name": "Frank Marshall",
  "life": "33 ans au moment de la partie",
  "country": "—",
  "role": "Joueur d'échecs, théoricien des ouvertures",
  "bio": "Joueur d'échecs ayant contribué à la théorie des ouvertures, connu notamment pour le gambit Marshall dans la partie espagnole. C'est lui qui raconte l'anecdote de la pipe d'Amos Burn (voir fiche Burn), lors d'une partie jouée en 1900 où il avait 33 ans.",
  "openings": ["Gambit Marshall (Partie espagnole)"]
}
```

*Note* : `"openings": ["Gambit Marshall (Partie espagnole)"]` reprend uniquement la mention faite par
Marc dans le transcript ("le célèbre gambit Marshall dans la partie espagnole") — il n'y a pas
d'entrée `OPS` dédiée au gambit Marshall (l'entrée `OPS["espagnole"]` existante ne le mentionne pas).

---

## 9. Paul Keres — l'anecdote du tennis

**Lien OPS** : ⚠️ aucun.

Source : `KERES — LE ROI SANS COURONNE/transcript.txt` — 0:02–0:49

```json
{
  "name": "Paul Keres",
  "life": "actif en 1935",
  "country": "Estonie",
  "role": "Joueur d'échecs offensif",
  "bio": "Présenté comme l'un des joueurs les plus forts n'ayant jamais obtenu le titre de champion du monde, réputé pour son style très offensif. Estonien. Petite anecdote d'enfance : il était aussi un très bon joueur de tennis, vice-champion d'Estonie de tennis.",
  "openings": []
}
```

*Note* : contrairement aux fiches 7 et 8, l'anecdote tennis est une seule phrase dans la source
(pas de récit développé) — je ne l'ai pas étoffée au-delà de ce qui est dit.

---

## Récapitulatif des liens OPS

| Personne | Lien vers une entrée `OPS` existante ? |
|---|---|
| William Davies Evans | Non — pas d'entrée gambit Evans dans `OPS` |
| Genrikh Kasparian | Non — vidéo de composition, pas d'ouverture |
| Arnold Denker | Non |
| Judit Polgár | Non |
| Napoléon Marache | Non |
| Gilles Andruet | Non |
| Joseph Henry Blackburne | Non |
| Wilhelm Steinitz | Non |
| Amos Burn | Non |
| Frank Marshall | Non (mentionne le gambit Marshall, absent d'`OPS`) |
| Paul Keres | Non |

Aucune des 9 figures demandées n'a de lien naturel vers une entrée `OPS` existante — toutes seraient
des fiches orphelines comme `alekhine`, ce que le schéma tolère déjà. Aucun lien forcé n'a été créé.
