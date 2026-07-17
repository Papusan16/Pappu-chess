# Répertoire C — 7 fiches d'ouverture (format Encyclopédie Papu-Chess)

## 0. Format identifié

`Papu_Chess.html` a déjà une structure d'encyclopédie : bouton 📚 (topbar), section
`openings` alimentée par un tableau JS `OPS` (`const OPS=[...]`, ligne 2462, JSON valide).
12 entrées existantes : italienne, espagnole, sicilienne, francaise, caro-kann,
scandinave, pirc-moderne, scholar, gambit-dame, indiennes, **anglaise**, reti.

Schéma exact de chaque entrée (ordre des clés observé) :

```json
{
  "id": "espagnole",
  "name": "Partie espagnole (Ruy López)",
  "moves": "1.e4 e5 2.Cf3 Cc6 3.Fb5",
  "freq": 3,
  "person": "ruylopez",
  "short": "Le pilier stratégique des ouvertures ouvertes, jouée à tous les niveaux.",
  "idea": "Le fou b5 cloue/pression le cavalier c6 qui défend e5. Jeu positionnel riche, plans subtils plutôt que tactiques immédiates.",
  "reply": "Noir : 3...a6 (défense Morphy, la plus jouée) chasse le fou et clarifie. Puis développe normalement. Pas de panique : l'Espagnole se joue sur le long terme.",
  "trap": "Le fou ne gagne PAS vraiment e5 tout de suite (3...a6 4.Fxc6 dxc6 5.Cxe5 Dd4! récupère le pion)."
}
```

- `freq` : 1/2/3 → affiché "Occasionnel" / "Courant" / "Très courant" (`freqLabel()`, ligne 3498).
- `person` : id optionnel vers l'objet `PEOPLE` (fiche biographique liée) — absent si pas de figure associée.
- `trap` : bloc optionnel, affiché seulement si présent (`if(o.trap)`).
- **Il n'y a pas de champ dédié "plan type"** dans ce schéma. `idea` porte l'idée directrice,
  `reply` porte la conduite à tenir en face. Le "plan type" demandé ne rentre dans aucun des deux
  proprement — voir note en fin de fichier avant intégration.
- ⚠️ **Collision** : `id: "anglaise"` existe déjà dans OPS (Partie anglaise, 1.c4, freq 1). La fiche
  n°3 ci-dessous ne peut pas être ajoutée telle quelle sous ce même id sans écraser/fusionner
  l'entrée existante — décision à prendre avant intégration.

Ce fichier est un brouillon de travail : contenu fidèle à `index_C_detail.md`, pas encore inséré
dans `Papu_Chess.html`.

---

## 1. Système Colle

Source : *Il se souvient de TOUT… SA MÉMOIRE DE GÉNIE !* — 1:19–1:34

```json
{
  "id": "colle",
  "name": "Système Colle",
  "moves": null,
  "freq": null,
  "person": null,
  "short": null,
  "idea": "Ouvrir avec le pion dame, puis jouer les pions c3 et e3 pour ériger une structure de pion pyramidale. Marc la présente comme très solide, et prévient qu'elle n'est pas aussi passive qu'elle en a l'air.",
  "reply": null,
  "trap": null
}
```

**Idée directrice** (2-3 phrases, fidèle à la source) : le système consiste à ouvrir avec le pion
dame, puis à jouer c3 et e3 pour construire une structure de pion pyramidale. C'est présenté comme
très solide ; malgré l'apparence passive, il existe des plans d'attaque et des plans d'évolution
("cela en a l'air parce qu'il y a des plans d'attaque, des plans d'évolution").

**Plan type** : d4, c3, e3 (ordre exact des coups non précisé dans la source), suivi de plans
d'attaque non détaillés dans cet extrait.

*Note* : le nom exact "Colle" n'apparaît pas dans cette fenêtre de 15s (Marc dit "le système co…"
— coupé, probablement "système Colle" comme identifié dans `index_C.md`). Champs `moves`/`freq`/
`person`/`short`/`trap` laissés à `null` : absents de la source.

---

## 2. Attaque yougoslave (contre le Dragon)

Source : *Bobby Fischer — Le Massacre du Dragon !* — 1:50–2:05

```json
{
  "id": "yougoslave-dragon",
  "name": "Attaque yougoslave (contre le Dragon)",
  "moves": null,
  "freq": null,
  "person": null,
  "short": null,
  "idea": "Mettre la dame en d2 et préparer le grand roque. La dame en d2 soutient le pion f3, en vue d'un futur h4-h5 après le grand roque.",
  "reply": null,
  "trap": null
}
```

**Idée directrice** : contre l'attaque yougoslave, ça consiste à mettre la dame en d2 et à préparer
le grand roque ; la dame en d2 soutient le pion f3.

**Plan type** : Dd2 → grand roque (0-0-0) avec les Blancs. La source coupe juste après ("puis
comme on fait grand roque avec les Blancs on…") — la suite du plan (poussée h4-h5, typique de
l'attaque yougoslave) n'est pas dans l'extrait et n'est donc pas incluse ici.

---

## 3. Anglaise

⚠️ Un id `anglaise` existe déjà dans OPS (voir section 0) — à fusionner, pas dupliquer.

Source : *ÉTOUFFEMENT STRATÉGIQUE ! 🥵♟️* — 0:34–0:49

```json
{
  "id": "anglaise",
  "name": "Anglaise",
  "moves": null,
  "freq": null,
  "person": null,
  "short": null,
  "idea": "Contrôler la case centrale d5 avec un pion de l'aile. Si les Noirs jouent d5, il y aura échange du pion de l'aile contre le pion du centre, ce qui donnera aux Blancs une majorité centrale de pions (il leur restera deux pions pouvant aller au centre contre un seul pour les Noirs).",
  "reply": null,
  "trap": null
}
```

**Idée directrice** : contrôler la case d5 avec un pion de l'aile (c4). Si Noir répond ...d5,
l'échange qui suit donne aux Blancs une majorité de pions centraux (deux pions blancs pouvant
avancer au centre contre un seul pion noir).

**Plan type** : c4 visant d5 ; en cas d'échange sur d5, exploiter la majorité de pions centraux
obtenue. La phrase suivante ("L'autre idée de…") est coupée par la fenêtre de 15s — un second volet
du plan existe dans la vidéo mais n'est pas dans l'extrait, donc non repris ici.

---

## 4. Système de Londres

Source : *Système de Londres — Elle bat un MAÎTRE d'échecs avec UNE OUVERTURE SIMPLE !* — 0:41–0:56

```json
{
  "id": "londres",
  "name": "Système de Londres",
  "moves": null,
  "freq": null,
  "person": null,
  "short": null,
  "idea": "Sortir le fou en f4 avant de jouer e3 et c3, pour construire une chaîne de pions pyramidale. Le fou est extrait avant e3 pour ne pas rester enfermé en c1.",
  "reply": null,
  "trap": null
}
```

**Idée directrice** : ça consiste à sortir le fou en f4 avant de jouer e3 et c3, pour construire la
chaîne de pion pyramidale. Le fou sort en premier exprès, pour ne pas se retrouver enfermé en c1.

**Plan type** : Ff4 → e3, c3 (chaîne pyramidale) → puis Cf3, Fd3 pour compléter le développement.

---

## 5. Sicilienne — variante des échanges

Source : *Maîtrise la défense Sicilienne grâce à des échanges intelligents !* — 1:46–1:59

```json
{
  "id": "sicilienne-echanges",
  "name": "Sicilienne (variante des échanges)",
  "moves": null,
  "freq": null,
  "person": null,
  "short": null,
  "idea": "Pour les Noirs, la stratégie consiste à pouvoir réussir à jouer ...d5. Si les Blancs échangent le cavalier en c6, cela aide en réalité les Noirs : le pion b7 reprend, et ce pion en c6 pourra ensuite soutenir la poussée ...d5. Il n'est donc pas intéressant pour les Blancs de prendre le cavalier noir.",
  "reply": null,
  "trap": null
}
```

**Idée directrice** : la stratégie noire vise à jouer ...d5. Si les Blancs prennent le cavalier en
c6, le pion b7 reprend et le nouveau pion c6 soutient ensuite la poussée ...d5 — donc cet échange
aide les Noirs plutôt que de les gêner.

**Plan type** : Noir manœuvre vers ...d5 ; l'échange volontaire des Blancs sur c6 (Cxc6 bxc6) est
présenté comme contre-productif pour eux, car il facilite justement cette poussée.

---

## 6. Giuoco Piano / attaque Greco

Source : *Les ouvertures ne s'apprennent pas, elles se comprennent* — 22:24–22:39

```json
{
  "id": "giuoco-greco",
  "name": "Giuoco Piano / attaque Greco",
  "moves": null,
  "freq": null,
  "person": null,
  "short": null,
  "idea": "Le plan consiste à jouer e5, chasser le cavalier noir, sacrifier le fou puis enchaîner par Cg5+, suivi de l'arrivée de la dame : le tandem dame + cavalier attaque pour mater le roi.",
  "reply": "Dans la position montrée, ce plan ne fonctionne pas : Noir a le fou en e7. Sur e5, il bouge son cavalier, et le fou prend (la suite exacte est coupée par la fenêtre de 15s).",
  "trap": null
}
```

**Idée directrice** : jouer e5, chasser le cavalier noir, sacrifier le fou, puis enchaîner
cavalier-g5 échec et l'arrivée de la dame — le tandem dame + cavalier attaque pour mater le roi.

**Plan type / mise en garde** : la vidéo précise explicitement que **ce plan échoue** dans la
position montrée, à cause du fou noir déjà en e7 ("Mais là, ça marche pas. Pourquoi ? Parce qu'il a
le fou en e7. Sur e5, il bouge son cavalier. Fou prend…" — phrase coupée par la fenêtre de 15s).
C'est un contenu directement issu de la source (pas une connaissance générique ajoutée), à traiter
comme "plan classique + son contre-exemple", pas comme une ligne gagnante universelle.

---

## 7. Hollandaise

Source : *Mes parties contre des GMI !* — 19:49–20:04

```json
{
  "id": "hollandaise",
  "name": "Hollandaise",
  "moves": null,
  "freq": null,
  "person": null,
  "short": null,
  "idea": "Mettre en place toute une structure : une chaîne de pions sur cases blanches côté Noir, décrite comme une véritable muraille.",
  "reply": null,
  "trap": null
}
```

**Idée directrice** : ça consiste à mettre en place toute une structure — une chaîne de pions (côté
Noir) sur cases blanches, formant une véritable muraille.

**Plan type** : ⚠️ **incomplet dans la source.** La phrase sur l'inconvénient de cette structure est
coupée net par la fenêtre de 15s : "l'inconvénient d'une telle structure, c'est lorsqu'on a le fou
en c1 qui est…" — la suite (probablement l'enfermement du fou de cases blanches) n'est pas dans
l'extrait. À ne pas compléter par déduction générique ; nécessite un extrait plus long ou le
transcript source pour ce point précis.

---

## Notes avant intégration dans Papu_Chess.html

1. **Champ "plan type" absent du schéma OPS** — actuellement replié dans `idea` (fiches 1, 4, 5) ou
   dans `reply` quand il s'agit d'une mise en garde sur l'échec d'un plan (fiche 6). À trancher :
   étendre le schéma avec un champ dédié, ou répartir manuellement dans `idea`/`reply` au moment de
   la rédaction finale.
2. **Champs laissés à `null`** (`moves`, `freq`, `person`, `short`, `trap`) : non déterminables à
   partir des 15 secondes extraites sans ajouter des connaissances génériques — volontairement non
   remplis, à compléter par une relecture humaine ou un extrait plus large du transcript source.
3. **Collision d'id** : `anglaise` existe déjà dans OPS — fusion nécessaire, pas insertion brute.
4. **Contenus tronqués** : fiches 3 (Anglaise, "l'autre idée de…"), 6 (Giuoco Piano, la suite du
   contre-exemple) et 7 (Hollandaise, l'inconvénient de la structure) sont coupées par la fenêtre de
   15s — la phrase réelle continue au-delà. Étendre la fenêtre pour ces trois-là si le contenu
   complet est nécessaire.
5. **Laissés de côté, comme demandé** : Ding-Nepo (ouverture non identifiée) et "l'ouverture au
   rang" (terme à vérifier) — non traités ici.
