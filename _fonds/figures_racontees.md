# Figures d'échecs racontées en profondeur (au-delà d'une simple mention de nom)

Recherche du passage Gambit Evans / William Davies Evans, puis repérage de passages similaires
ailleurs dans le corpus (871 transcripts, Marc Quenehen/) : une figure présentée avec un vrai récit
biographique (naissance, trait de caractère, anecdote) avant d'enchaîner sur la partie/l'ouverture,
pas juste un nom cité en passant.

---

## Gambit Evans — William Davies Evans

**Fichier** : `Gambit Evans  variante agressive de l'ouverture italienne/transcript.txt`
**Timecode** : 0:02–1:26 (le récit démarre dès le début de la vidéo, donc pas de « avant » ;
fenêtre étendue jusqu'à 1:26 pour la transition vers le contenu théorique)

> 0:02 nous attend sur le combi evans / 0:03 l'ouverture du gobi evans créé par le / 0:06 capitaine
> william davies evans vous / 0:08 savez c'est un gallois né en 1790 qui va / 0:11 s'engager très tôt
> dans la marina quatre / 0:13 jours seulement et à 30 ans il va être / 0:15 capitaine et evans il a
> la particularité / 0:18 finalement d'avoir appris les échecs / 0:19 très tard il a appris auprès
> d'un / 0:21 officier de marine à l'âge de 27 28 ans / 0:23 je crois et quelques années plus tard il
> / 0:26 va a vanté le temps dit evans c'est pas / 0:28 la seule chose qui va inventer / 0:29
> d'ailleurs il va inventer alors je m'y / 0:30 connais pas en marine mais un système de / 0:32
> lanternes à trois couleurs qui évite les / 0:34 collisions nocturne de navires pour / 0:36 cette
> invention d'ailleurs il va être / 0:37 récompensé par le gouvernement anglais / 0:39 qui va lui
> octroyer une somme d'argent / 0:40 et même par les tsars de russie qui va / 0:41 lui offrir des
> objets en or comme une / 0:43 montre en or je crois malheureusement / 0:45 pour evans il va mourir
> dans la le grand / 0:49 dénouement la grande pauvreté malgré que / 0:52 juste avant sa mort les
> jours de chef de / 0:54 l'époque c'est de se cotiser pour lui / 0:55 venir en aide mais on va voir
> / 0:58 aujourd'hui des premières ouvertures du / 1:01 gambit et vaste de ses premières / 1:02
> créations...

**Nuance** : le transcript dit qu'Evans est devenu capitaine de marine et a appris les échecs
tardivement (27-28 ans) auprès d'un officier de marine — pas explicitement qu'il était lui-même
officier de marine marchande ayant appris à bord d'un bateau. Le fond de l'histoire (marine,
apprentissage tardif, inventeur de lanternes de signalisation, mort dans la pauvreté) correspond
bien à la demande initiale.

---

## Autres figures racontées en profondeur

| Figure | Fichier | Timecode | Contenu |
|---|---|---|---|
| **Genrikh Kasparian** | `Brillant et Mat !` | 0:01–0:31 | Compositeur d'échecs arménien, né 1917, mort ~1989-90, présenté comme un forgeur/compositeur de génie avant d'analyser une de ses parties |
| **Arnold Denker** (transcrit "Wenger") | `De la Boxe aux Echecs ! 🥊♟️` | 0:01–0:39+ | Né 1914 dans le Bronx, ex-boxeur prometteur, a découvert les échecs via des paris entre camarades de classe |
| **Judit Polgár** | `Judit Polgar ou la vraie Beth Harmon des échecs !` | 0:02–0:27 | Née 1976, comparée à Beth Harmon (Le Jeu de la Dame), père pédagogue qui a formé ses filles aux échecs, maths et langues |
| **Napoleon Marache** | `Magnifique Mat de Morphy ! 🤩` | 0:56–1:29 | Né 3 jours après Waterloo, prénommé Napoléon par ses parents, né à Meaux, émigré aux USA à 12 ans, gagne un tournoi à New York, écrit des livres d'échecs — avant d'affronter Morphy |
| **Gilles Andruet** | `Météore dans le monde des échecs` | 0:01–0:39+ | Né 1958, champion de France 1988, personnalité atypique/perturbatrice, "destin tragique" annoncé |

Ces 5 passages n'ont pas encore été extraits en fenêtre de 30s complète comme pour Evans (juste
repérés et confirmés sur la profondeur du récit) — à approfondir si besoin.

## Méthode de repérage

Recherche par grep sur les 871 transcripts, motif `\bné en 1[0-9]{3}\b|\bné à\b` (marqueur de
naissance biographique), puis vérification manuelle du contexte pour écarter les mentions courtes
(factoïde d'un joueur moderne dans un commentaire de partie, ex. MVL né en 1990, Nakamura) et ne
garder que les vrais récits.

## Piste pour l'encyclopédie Papu-Chess

Ces figures sont candidates au champ `person` du schéma `OPS` de `Papu_Chess.html` (objet `PEOPLE`,
voir `repertoire_C.md` section 0) : Kasparian, Denker, Polgár, Marache et Andruet n'y figurent pas
encore (12 entrées `PEOPLE` actuelles couvrent italienne/espagnole/sicilienne/française/etc., pas
ces figures-ci).
