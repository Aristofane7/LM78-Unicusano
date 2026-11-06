# LM-78 Scienze Filosofiche Applicate — Unicusano, a.a. 2026/27

Repository **privato** di studio e tracking: piano di studi, carenze, test d'accesso, esami,
seminari per le Altre conoscenze, scadenze amministrative. Istruzioni operative in
[`CLAUDE.md`](CLAUDE.md); metodo di studio ereditato da `Aristofane7/laurea-L5` (`PROTOCOLLO.md`).

```bash
make status      # CFU, prerequisiti aperti, seminari, prossime scadenze
make relazione   # conteggio battute della relazione seminari (soglia 10.000)
```
Richiede Python 3 con PyYAML (`pip install pyyaml`). `make status OGGI=GG/MM/AAAA` simula un'altra data.

| Cartella | Contenuto |
|---|---|
| `piano/piano.yaml` | insegnamenti, SSD, CFU, anno, stato, data esame, voto; carenze e test d'accesso |
| `carenze/<slug>/` | prove di idoneità M-FIL/01 (vedi D1 nel Lab prima di preparare i materiali) |
| `test-accesso/` | materiali del test d'accesso online |
| `esami/<slug>/` | programma, fonti, documenti di studio, prove di verifica, etivity |
| `seminari/` | `tracker.yaml` e `relazione/` |
| `admin/` | `scadenze.md`; `documenti/` contiene solo riferimenti, mai dati sensibili |
| `templates/` | puntatori agli scheletri di `laurea-L5` e note di adattamento |
