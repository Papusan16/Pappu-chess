# Manifeste — sauvegardes Chess.com (Papu_san)

Ce dossier archive les données extraites du compte Chess.com « Papu_san ».
Les blobs de données (PGN, JSON, CSV) ne sont **pas versionnés** — ils sont
sauvegardés via Google Drive. Seul ce manifeste entre dans git : il dit ce
qui existe, où, et de quand ça date.

## Données premium (capture du 4 septembre 2026)
- Capture du 2026-09-04 13:03 (ré-export incluant la partie du 4 sept ; `exportDate` 2026-09-04T13:03:33Z).
- `papu_san_chesscom_data.json` : 179 920 o ; `papu_san_chesscom_data.csv` : 63 015 o. Non versionnés (backup via Google Drive).
- Contenu : profil Diamant, classements/records, stats avancées par thème, historique rating partie par partie (577 Rapide + 27 En différé, dont 14 classées + 13 amicales).
- Schéma JSON : `profile`, `apiStats`, `clubs`, `summary`, `detailedStats`, `ratingHistory` — les stats par thème sont dans `detailedStats`.
- Détail versionné : `_sessions/2026-09-05.md` (section « Archive intégrale »).
