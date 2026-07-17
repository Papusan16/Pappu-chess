# Lexique de normalisation du vocabulaire échiquéen

**Statut : liste à valider — aucune application, aucun transcript modifié.**

## Méthode

- Corpus : les 871 `transcript.txt` du dossier `Marc Quenehen/` (sous-titres
  auto-générés, très bruités).
- Comptage de fréquence de tous les mots du corpus (3,2M mots), puis
  inspection manuelle du contexte (échantillons aléatoires) pour chaque
  variante candidate d'un terme échiquéen correct.
- Cette normalisation est prévue pour s'appliquer **à la lecture seulement**
  (ex. au moment d'un recomptage), jamais en réécrivant les fichiers source.
- Échelle de fiabilité :
  - ✅ **FIABLE** — motif récurrent, contexte échiquéen quasi systématique
    dans les échantillons, peu de collision avec un mot courant.
  - ⚠️ **MOYEN** — motif réel mais volume faible et/ou collision partielle
    avec un mot courant ; substitution possible seulement sous condition
    contextuelle (ex. "doit être suivi d'une case").
  - 🚫 **RISQUÉ** — collision majeure avec un ou plusieurs mots très
    fréquents du français, ou échantillon trop rare/instable pour trancher.
    À ne pas substituer aveuglément.

---

## 1. Cavalier

Le mot "cavalier" est déjà bien transcrit dans la majorité des cas
(37 505 fois, + 3 898 "cavaliers"). Les variantes ci-dessous apparaissent
presque systématiquement juste avant une case ("cavalier + coordonnée") ou
un verbe de coup ("prend", "joue").

| Variante | Occurrences | Fiabilité | Note |
|---|---|---|---|
| cahier | 479 | ✅ | "jouer cahier à 6", "le cahier peut sortir" |
| calier | 536 | ✅ | "calier G4", "calier C3 défend" |
| cavaler | 585 | ✅ | forme verbale parasite : "cavaler G6", "je joue cavaler là" |
| cavale | 248 | ✅ | "cavale et prend", "j'attaque l'option cavale" |
| cavaly | 113 | ✅ | "perdre le cavaly", "bouger le cavaly" |
| caval | 115 | ✅ | "Caval F6", "jouer Caval" |
| cavalia | 50 | ✅ | "cavalia à quatre", "avec cette idée cavalia" |
| cavali | 68 | ✅ | "cavali F3", "mon cavali cloué" |
| cavalière | 172 | ✅ | "la cavalière 6", "un cavalière de 4" |
| lecavalier (soudé) | 456 | ✅ | artefact de collage "le" + "cavalier", pas une déformation phonétique |
| cavalé | 21 | ⚠️ | volume faible mais contexte net ("cavalé g5 échec") |
| cavier | 21 | ⚠️ | volume faible ("le cavier en F6") |
| caviar | 20 | ⚠️ | volume faible ; homonyme du mot "caviar" mais aucun faux positif observé dans l'échantillon |
| cav (abrégé) | 79 | ⚠️ | contexte propre dans l'échantillon ("K B5", "CAV blanc"), mais jeton court à 3 lettres, à surveiller |
| cavalerie | 37 | 🚫 | usage mixte : parfois métaphore correcte ("sa cavalerie et son fou G7"), parfois cavalerie **militaire réelle** (parties historiques, ex. Nicopolis) — ne pas substituer sans vérifier le contexte |
| K (lettre seule) | 260 | 🚫 | dans l'échantillon, 100% suivi d'une case ("K G7", "K C3") donc motif propre *dans ce corpus*, mais lettre unique = risque de collision élevé sur un corpus plus large (OK, kg, km, K.-O...) — à valider au cas par cas |
| quel / quelle | 888 | 🚫 | exemple cité par l'utilisateur : très largement un mot courant ("n'importe quel", "à quel âge", "quel est le but"). Seule une minorité de cas ("jouer quel et b4") est une déformation de "cavalier". **Ne pas substituer sans règle contextuelle forte** |

---

## 2. Fou

"fou" seul est déjà bien transcrit (34 304 occurrences).

| Variante | Occurrences | Fiabilité | Note |
|---|---|---|---|
| foot | 1 725 | ✅ | "mon foot case noir", "la sortie du foot" |
| fout | 754 | ✅ | "son fout de case noire", "diagonale à son fout" |
| fond | 761 | ⚠️ | net dans un sous-ensemble ("le fond des6", "mettre un fond en fianchetto") mais collision avec "au fond" (sens courant) — fiable seulement si suivi d'une case ou de "de case" |
| faux | 1 530 | ⚠️ | net dans l'échantillon ("je joue faux F4", "des faux E3") mais homonyme direct de l'adjectif "faux" (mensonger) — volume élevé, à contrôler par contexte |
| foux | 7 | ⚠️ | volume trop faible pour trancher seul, contexte cohérent |
| foufou | 7 | 🚫 | volume très faible, sens incertain (réduplication ou fusion de deux mentions) |
| fous | 1 641 | — | **déjà correct** : pluriel légitime de "fou" (pièce). Mais fort risque d'homonymie avec l'expression "je m'en fous" — ne compte pas ce mot sans distinguer les deux usages |

---

## 3. Roi / Roque

"roi" est bien transcrit (19 513 fois). "roque" (nom), lui, est presque
toujours déformé — la forme correcte n'apparaît que 145 fois contre 4 115
pour sa déformation dominante :

| Variante | Occurrences | Fiabilité | Note |
|---|---|---|---|
| rock | 4 115 | ✅ | forme dominante et quasi systématique : "petit rock" (2 049 vs "petit roque" 6), "grand rock" (494 vs "grand roque" 88) |
| roc | 243 | ⚠️ | "Grand Roc", "Roc Blanc" (probable déformation de "roque") mais homonyme du mot "roc" (rocher), utilisé parfois en métaphore de solidité du roi |
| roy | 262 | ⚠️ | "roy c7" (roi c7) net, mais quelques faux positifs probables (noms propres type "Alain le Roy") |
| roquer, déroquer | 128 / 23 | — | **déjà corrects**, ce sont les vrais verbes du jeu — pas de substitution nécessaire |
| troquer, croquer, perroquet, baroque | 92 / 6 / 3 / 1 | 🚫 exclus | fausses pistes : ce sont des mots français distincts et corrects ("troquer" = échanger une pièce, usage légitime), pas des déformations de "roque" |

---

## 4. Dame

"dame" est bien transcrite (28 887 fois). Une déformation nette existe,
et un phénomène distinct de **fusion** avec la case qui suit mérite d'être
signalé séparément (pas une simple substitution mot-à-mot).

| Variante | Occurrences | Fiabilité | Note |
|---|---|---|---|
| dam | 528 | ✅ | "dam F3", "vis-à-vis dam tour", "bougé leur dam" |
| dams | 93 | ⚠️ | motif moins net ("dams est comme"), à vérifier |
| damage, damache, damashin... (famille "dame"+case[+mat/échec] soudés) | damage=151, damache=23, dizaines d'autres formes à occurrence unique | 🚫 structure, pas liste | Il s'agit d'un phénomène de **collage ASR** : "dame" + lettre de colonne + chiffre (+ parfois "mat"/"échec") fusionnés en un seul faux mot (ex. "damage 3" = "dame g3", "damashismat" ≈ "dame h5 mat"). La longue traîne de formes à 1-2 occurrences est trop instable pour une liste ; ce cas demandera une règle par motif (regex), pas une substitution lexicale simple |

---

## 5. Tour

Aucune déformation identifiée : "tour" est déjà la bonne transcription.
**Mais c'est le terme le plus à risque du lexique pour un recomptage**,
car "tour" est aussi un mot très courant (tour de jeu, tour Eiffel, "à son
tour"...). Impossible de le désambiguïser par simple normalisation
orthographique — il faudra une règle de contexte (proximité d'une case,
de "grande/petite tour", de "les tours", etc.) si on veut un jour compter
les mentions de la pièce spécifiquement.

---

## 6. Pion

"pion"/"pions" déjà bien transcrits (34 372 / 7 578).

| Variante | Occurrences | Fiabilité | Note |
|---|---|---|---|
| pioncer | 127 | ✅ | "le pioncer 4", contexte échiquéen net dans l'échantillon ; à noter : "pioncer" est aussi un verbe d'argot ("dormir") — homonyme théorique mais non observé dans l'échantillon |
| pione | 96 | ✅ | "pression sur le Pione 4" |
| pionroi (soudé) | 21 | ✅ | fusion de l'expression correcte "pion roi" (pion e2/e4), pas une déformation phonétique |
| pioche | 15 | ⚠️ | volume faible, homonyme du mot courant "pioche" (jeu de cartes/outil) |

---

## 7. Échec / Mat

"échec"/"échecs" bien transcrits dans l'immense majorité des cas
(8 747 / 3 104).

| Variante | Occurrences | Fiabilité | Note |
|---|---|---|---|
| matte | 36 | ✅ | "je le matte en G2", "double échec et je matte" |
| mate | 38 | ⚠️ | net dans l'échantillon mais collision possible avec l'anglicisme "mate"/l'adjectif "mate" (teint mat) |
| échemat, écheekat, échecemat... | 12, 4, 2 ... | 🚫 structure, pas liste | même phénomène de fusion que pour "dame" : "échec" + "et" + "mat" collés. Volumes trop faibles individuellement pour une substitution fiable |

---

## 8. Gambit et autres termes tactiques

| Variante | Occurrences | Fiabilité | Note |
|---|---|---|---|
| gambi | 131 | ✅ | "Gambi Evans", "Gambi Benko", "Gambi de Budapest" |
| combi | 33 | ✅ | échantillon vérifié un par un : toujours un nom de gambit ("combi roi", "combi Evans", "combi Budapest", "combi Schilling", "combi Plattsburgh") — pas de confusion observée avec "combinaison" |
| gambidame (soudé) | 44 | ✅ | fusion de "Gambit Dame" |
| gambidam (soudé) | 33 | ✅ | idem, variante orthographique |
| gambirois / gambiroi (soudé) | ~9 | ⚠️ | volume faible, fusion de "Gambit Roi" |
| logobi (roi/evans) | 1-2 | 🚫 | dérive phonétique extrême de "le gambit" — trop rare et trop instable pour être listé sérieusement |
| fiancé | 68 | 🚫 | déformation nette de "fianchetto" dans l'échantillon ("un fond en fiancé") mais collision totale avec le mot courant "fiancé" (personne fiancée) — volume élevé de faux positifs attendus, substitution seulement si proche de "roi", "fou" ou d'une case |
| fiancetto / fiancéto | 9 / 8 | ⚠️ | plus proches de la forme correcte, moins de risque de collision, volume faible |
| fianchetto (correct) | 4 | — | forme correcte, très rare — le terme est presque toujours déformé en "fiancé" |

**Déjà corrects, pas de déformation trouvée :** fourchette (1 936),
clouage/clouer/cloué (1 140/546/960), passant ("prise en passant", 264),
pat (59), promotion (423).

---

## 9. Cases / coordonnées (a1-h8)

Ce n'est pas un lexique de mots isolés mais un **motif structurel** :
la lettre de colonne prononcée seule ("e", "a", "g"...) se confond avec un
mot-outil français très fréquent, et se colle au chiffre de la rangée.
Comptage des bigrammes "mot + chiffre" sur tout le corpus :

| Colonne visée | Mots-outils repérés | Exemples de comptes | Fiabilité |
|---|---|---|---|
| **e** (colonne centrale) | des / les / ces / et | "des quatre" = e4 (1 454), "des cinq" = e5 (1 192), "des six" = e6 (688), "des trois" = e3 (543) | ⚠️ motif très fréquent et cohérent avec l'usage réel (e4/e5 sont les coups les plus commentés), mais "des", "les", "ces" sont parmi les mots les plus fréquents du français — nécessite une règle contextuelle (proximité de "joue", "prend", nom de pièce) plutôt qu'une substitution brute |
| **a** (colonne a) | à / a | "à quatre" = a4 (122), "à trois" = a3 (217), "a deux" = a2 (395) | 🚫 "à"/"a" sont parmi les tout premiers mots du français — risque de faux positifs très élevé, à ne traiter qu'avec un marqueur de coup juste avant |
| **g** (colonne g) | j'ai | "j'ai quatre" = g4 (83), "j'ai cinq" = g5 (87), "j'ai deux" = g2 (274) | 🚫 "j'ai + chiffre" est très majoritairement un décompte littéral ("j'ai deux pions", "j'ai trois minutes") plutôt qu'une case — le nombre brut de coïncidences est trompeur, à écarter d'un comptage automatique sans vérification manuale ligne par ligne |
| **b, c, d, f, h** | (aucun mot-outil courant identifié) | quasi aucune occurrence de fusion trouvée | ✅ ces colonnes semblent déjà transcrites correctement en notation alphanumérique dans la grande majorité des cas — pas de déformation récurrente à corriger |

**Conclusion pour cette catégorie : c'est la zone la plus dangereuse du
lexique.** Les motifs "des/les/ces + chiffre" (e), "à/a + chiffre" (a) et
"j'ai + chiffre" (g) touchent des mots-outils parmi les plus fréquents du
français ; une substitution mécanique produirait un volume de faux
positifs sans doute supérieur au volume de vrais positifs pour les colonnes
a et g. Seule la colonne e semble avoir un rapport signal/bruit
raisonnable, et encore sous condition de contexte.

---

## 10. Noms d'ouvertures étrangères

| Ouverture | Variante | Occurrences | Fiabilité | Note |
|---|---|---|---|---|
| Caro-Kann | carocane (soudé) | 110 | ✅ | forme dominante, très cohérente ("ma défense carocane", "C6... la carocane") |
| Caro-Kann | karo / kann (séparés) | 14 / 15 | ⚠️ | volume faible, formes isolées plus ambiguës |
| Alekhine | alekin / d'alekin | 16 / 6 | ⚠️ | chute du "h" muet, motif cohérent mais volume modeste |
| Pirc | pirk | 11 | ⚠️ | volume faible |
| Marshall (gambit/contre-gambit) | marchall / marchal | 14 / 7 | ⚠️ | "marchal" est proche du mot "maréchal" — homonymie possible, volume faible |
| Grünfeld | grunfeld (déjà correct) / greenfeld | 16 / 2 | — | déjà bien transcrite dans la quasi-totalité des cas |
| Traxler | traxler (déjà correct) | 19 | — | aucune déformation trouvée |
| Fegatello | fegatello (déjà correct) | 18 | — | aucune déformation trouvée |
| Réti | — | — | 🚫 | "reti" (41 occurrences) est noyé dans "retirer/retire/retiré" (700+ occurrences) — impossible à isoler de façon fiable sans lecture manuelle |
| Benoni | — | 2-3 | 🚫 | corpus quasi muet sur cette ouverture, volume trop faible pour conclure |
| Nimzo(-indienne) | nimzo / nimzovic | 2 / 3 | 🚫 | volume beaucoup trop faible |

**Déjà bien transcrites, pas de déformation trouvée :** Sicilienne (346),
Italienne (97), Espagnole (71), Anglaise (91), Française (221), Catalane
(30), Hollandaise (28), Scandinave (29), Système de Londres (159).

⚠️ **Piège de comptage (pas d'orthographe) sur ces dernières :** ce sont
toutes aussi des adjectifs/gentilés/toponymes du français courant
("défense française" vs "il parle français" ; "système de Londres" vs
"un tournoi à Londres"). L'orthographe est correcte, mais un comptage brut
de ces mots surestimera les mentions d'ouverture si on ne filtre pas le
contexte (présence de "défense", "système", "variante", coup d'ouverture
juste avant/après).

---

## Résumé — à valider avant toute application

- **Fiables sans condition (✅)** : cavalier → cahier/calier/cavaler/cavale/
  cavaly/caval/cavalia/cavali/cavalière/lecavalier ; fou → foot/fout ;
  roque → rock ; dame → dam ; gambit → gambi/combi/gambidame/gambidam ;
  mat → matte ; Caro-Kann → carocane ; pion → pioncer/pione/pionroi.
- **Fiables sous condition de contexte (⚠️)** : fou → fond/faux ; roi → roy ;
  roque → roc ; case e → des/les/ces/et + chiffre ; fianchetto →
  fiancetto/fiancéto ; mat → mate ; Alekhine/Pirc/Marshall ; dam → dams.
- **À exclure ou traiter au cas par cas (🚫)** : "quel" (cavalier), "K" seul
  (cavalier), "cavalerie" (cavalier vs cavalerie militaire réelle), "fous"
  (déjà correct mais homonyme de l'expression "je m'en fous"), "tour"
  (aucune correction possible, homonymie structurelle), "fiancé"
  (fianchetto vs personne fiancée), case a → à/a + chiffre, case g → j'ai +
  chiffre, "reti" (noyé dans "retirer"), noms d'ouverture déjà corrects mais
  homonymes de mots courants (française, anglaise, italienne, catalane,
  Londres...), fusions dame/case et échec/mat (damage, damashismat,
  échemat...) qui relèvent d'une règle de motif plutôt que d'une liste.

Rien n'a été appliqué à ce stade — cette liste sert uniquement de base de
discussion avant toute règle de normalisation à la lecture.
