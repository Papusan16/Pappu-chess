// ---------------------------------------------------------------------------
// Test ciblé — neutralisation du champ en-passant lors d'un trait forcé.
//
//   node _fonds/test_mauvais_fou_en_passant.js
//   (depuis la racine du dépôt ; aucune dépendance, aucun build)
//
// Le détecteur de mauvais fou interroge un camp HORS DE SON TOUR : il réécrit
// le champ « trait » de la FEN. chess.js 0.10.3 refuse alors la FEN si le champ
// en-passant contredit le nouveau trait (validate_fen, erreur 11 « Illegal
// en-passant square »), et — c'est le piège — `new Chess(fen)` NE LÈVE PAS
// d'erreur : il rend un ÉCHIQUIER VIDE. Toute position suivant une poussée
// double rendait donc les critères du détecteur muets (0 coup légal partout).
//
// Le test charge le VRAI code de Papu_Chess.html via vm — pas de
// réimplémentation à côté, conformément à la méthode de vérification déjà
// employée pour ce détecteur (cf. mauvais_fou_fen_test_c8.txt).
// ---------------------------------------------------------------------------
const fs=require('fs'), vm=require('vm'), path=require('path');
const HTML=fs.readFileSync(process.argv[2]||path.join(__dirname,'..','Papu_Chess.html'),'utf8');
const L=HTML.split('\n');

function slice(startRe, endRe){
  let i=L.findIndex(l=>startRe.test(l));
  if(i<0) throw new Error('introuvable : '+startRe);
  let j=i; for(;j<L.length;j++) if(endRe.test(L[j])) break;
  return L.slice(i,j+1).join('\n');
}
// 1) la bibliothèque chess.js intégrée
const chessSrc = slice(/chess\.js 0\.10\.3 intégré/, /^<\/script>$/).replace(/^<\/script>$/m,'');
// 2) le détecteur complet (safeMobility + isSafeDestination sont dedans)
const detSrc = slice(/^function fouBadBishopSquares\(mi\)\{/, /^\}$/);

const ctx={console};
vm.createContext(ctx);
vm.runInContext(chessSrc, ctx);
vm.runInContext(detSrc, ctx);
vm.runInContext('var VAL={p:1,n:3,b:3,r:5,q:9,k:0};', ctx);

// --- accès direct à safeMobility, extraite telle quelle du fichier ---
const smSrc = slice(/^    function safeMobility\(fenAt, sq, color\)\{/, /^    \}$/);
const isdSrc = slice(/^    function isSafeDestination\(fenBefore, from, to, pieceVal\)\{/, /^    \}$/);
const ftSrc = slice(/^    function forceTurn\(fen, color\)\{/, /^    \}$/);
vm.runInContext(ftSrc+'\n'+isdSrc+'\n'+smSrc, ctx);

let echecs=0;
function ok(nom, cond, detail){
  console.log((cond?'  OK   ':'  ÉCHEC')+' | '+nom+(detail?'  → '+detail:''));
  if(!cond) echecs++;
}

console.log('\n=== T1 — safeMobility sur une FEN portant un en-passant ===');
// Position de test connue (_fonds/mauvais_fou_fen_test_c8.txt), variante où
// les Noirs viennent de jouer la poussée double d7-d5 : trait aux Blancs, e.p. = d6.
const FEN_EP  = 'rNb2rk1/pp3ppp/2n1pq2/2PpP3/3P4/5N2/PP3PPP/R1BQK2R w - d6 0 12';
const FEN_REF = 'rNb2rk1/pp3ppp/2n1pq2/2PpP3/3P4/5N2/PP3PPP/R1BQK2R w - - 0 12';

// Contrôle : la FEN e.p. est bien valide en soi, l'échiquier n'est pas vide.
const nEp=new ctx.Chess(FEN_EP).board().flat().filter(Boolean).length;
ok('la FEN de départ (avec e.p.) donne un échiquier peuplé', nEp===28, nEp+' pièces');

// Le forçage brut du trait, sans neutraliser l'e.p., produit une FEN INVALIDE.
const brut=FEN_EP.split(' '); brut[1]='b';
const nBrut=new ctx.Chess(brut.join(' ')).board().flat().filter(Boolean).length;
ok('trait forcé SANS neutraliser e.p. → échiquier vide (le bug)', nBrut===0, nBrut+' pièces');

// Ce que safeMobility doit renvoyer : la même chose avec ou sans champ e.p.
const smEp =ctx.safeMobility(FEN_EP , 'c8', 'b');
const smRef=ctx.safeMobility(FEN_REF, 'c8', 'b');
ok('safeMobility(FEN avec e.p.) == safeMobility(FEN sans e.p.)', smEp===smRef, 'avec e.p. = '+smEp+', sans = '+smRef);

// Contre-épreuve : un fou qui a de la mobilité doit la garder malgré l'e.p.
const mobEp =ctx.safeMobility(FEN_EP , 'c1', 'w');
const mobRef=ctx.safeMobility(FEN_REF, 'c1', 'w');
ok('fou c1 (mobile) : mobilité préservée malgré e.p.', mobEp===mobRef && mobEp>0, 'avec e.p. = '+mobEp+', sans = '+mobRef);

// Cas discriminant : un fou de la MÊME couleur que le camp qui vient de pousser,
// et qui a une vraie mobilité. Est-indienne, les Noirs viennent de jouer c7-c5 :
// trait aux Blancs, e.p. = c6. Interroger le fou g7 force le trait à 'b' → e.p. incohérent.
const KID_EP  = 'rnbq1rk1/pp2ppbp/3p1np1/2p5/2PPP3/2N2N2/PP2BPPP/R1BQK2R w KQ c6 0 7';
const KID_REF = 'rnbq1rk1/pp2ppbp/3p1np1/2p5/2PPP3/2N2N2/PP2BPPP/R1BQK2R w KQ - 0 7';
const kidEp =ctx.safeMobility(KID_EP , 'g7', 'b');
const kidRef=ctx.safeMobility(KID_REF, 'g7', 'b');
ok('fou g7 après ...c7-c5 : mobilité identique avec ou sans e.p.', kidEp===kidRef && kidRef>0,
   'avec e.p. = '+kidEp+', sans = '+kidRef);

console.log('\n=== T2 — détecteur complet, non-régression sur la position c8 ===');
function detecte(fen){
  const c2={console, fullMoves:[], VAL:ctx.VAL};
  vm.createContext(c2);
  vm.runInContext(chessSrc, c2);
  const Real=c2.Chess;
  // new Chess() sans argument rend la position de test ; avec argument, comportement normal.
  c2.Chess=function(f){ return new Real(f===undefined?fen:f); };
  vm.runInContext(detSrc, c2);
  return c2.fouBadBishopSquares(-1);
}
const attendu='[{"s":"c8","side":"Noirs","safe":0,"gene":2,"colorCount":3,"dev":1}]';
const rRef=JSON.stringify(detecte(FEN_REF));
ok('position de référence inchangée', rRef===attendu, rRef);

const rEp=JSON.stringify(detecte(FEN_EP));
ok('même position après poussée double d7-d5 : même verdict', rEp===attendu, rEp);

console.log('\n'+(echecs?'>>> '+echecs+' ÉCHEC(S)':'>>> tout passe')+'\n');
process.exit(echecs?1:0);
