# CLAUDE.md — LM-78 Scienze Filosofiche Applicate (Unicusano)

## Contesto
Repository di studio e tracking di Davide Settembre Blundo per la LM-78 Unicusano, a.a. 2026/27, matricola FI78000380. Davide lavora a tempo pieno, è dottorando Unicusano in cotutela con la Universidad de Sevilla e segue in parallelo i Master 1MG e TSM (repository separato). Lingua di lavoro: italiano.

## Regole di studio
Le regole di preparazione esami (ancoraggio lessicale R1), il formato dei documenti di studio e la toolchain LaTeX sono quelle del repository di studio della laurea L-5: **`Aristofane7/laurea-L5`**, file `PROTOCOLLO.md`. Valgono anche qui, salvo le eccezioni elencate sotto. Riferimenti puntuali:
- regole di decisione sugli item, compresa R1 e l'avvertenza permanente: `PROTOCOLLO.md` §4;
- ciclo per lezione: §3; formato dei file (test, nodi, `STATO.md`): §7;
- stile e toolchain LaTeX (`pdflatex`, `mathpazo`, colori `blu`/`oro`, `ideabox`/`schemabox`/`orobox`, `longtable`+`booktabs`, `fancyhdr`, `babel` con `english`): §8;
- scheletro di un insegnamento: cartella `_template/`, da copiare in `esami/<slug>/` (o `carenze/<slug>/`) con gli stessi nomi di file.

Il repository `Aristofane7/fondamenti-razionalita` (Rationality Foundations Lab, che contiene le unità del 1MG) non definisce regole d'esame: è la fonte dei contenuti del Lab e del registro delle decisioni rinviate (vedi sotto).

Eccezioni: nessuna per ora. Da verificare al primo appello: R1 è tarata sui quiz a risposta multipla di UniPegaso. Se gli scritti Unicusano hanno un formato diverso (domande aperte, orale a Roma), annotare qui l'eccezione prima di applicare il metodo.

## Piano di studi
Fonti: piano ufficiale a.a. 2026/27 sul sito Unicusano (copia in `piano/piano-ufficiale-2026-27.md`) e schema di riconoscimento CFU della segreteria del 06/11/2026. Il dato strutturato è in `piano/piano.yaml`; le tabelle sotto sono un promemoria.

**Il riconoscimento è provvisorio.** La lettera è «informale e ufficiosa»: la Giunta di Dipartimento delibera solo all'immatricolazione, sulla base dell'autodichiarazione, e può riconoscere un numero di CFU diverso, per eccesso o per difetto. L'autodichiarazione (eventualmente aggiornata, con lo storico esami) va depositata entro 30 giorni dall'iscrizione: senza, i titoli non vengono riconosciuti. Fino alla delibera, in `piano.yaml` vale `riconoscimento: provvisorio`.

### Riconosciuti: 33 CFU
| Insegnamento | Anno | CFU | Da (esame sostenuto, CFU) |
|---|---|---|---|
| Neuroetica ed etica applicata | 1 | 9 | Master FMC: «L'individuo e la persona» (6) → 6; «Filosofia e comunicazione» (6) → 3 |
| Esame a scelta | 1 | 6 | LS 84/S Unimore: Strategie di internazionalizzazione (4) |
| Storia del pensiero scientifico | 2 | 6 | Master FMC: Storia della scienza (6). Occupa l'opzione a scelta tra Storia del pensiero economico, Storia della medicina e Storia del pensiero scientifico |
| Estetica delle arti e dei media | 2 | 9 | Master FMC: Il dibattito contemporaneo sui temi dell'estetica (6) |
| Lingua inglese C.A. | 2 | 3 | LS 84/S Unimore: Lingua inglese II (4) |

### Prerequisiti bloccanti
1. Carenze M-FIL/01 (PHIL-01/A), con prove di idoneità libere e fuori calendario: Filosofia teoretica (9) e Teoria della persona e della relazione (9).
2. Test d'accesso online (D.M. 270/04), dopo le carenze.

Nessun esame della magistrale può essere sostenuto prima di aver completato 1 e 2.

### Da sostenere: 87 CFU
| Anno | Insegnamento | SSD (2015 / 2024) | CFU |
|---|---|---|---|
| 1 | Teoria dei processi cognitivi ed emotivi | M-FIL/01 / PHIL-01/A | 9 |
| 1 | Neurodiritto | IUS/20 / GIUR-17/A | 6 |
| 1 | Teoria della medicina e scienza del vivente | M-FIL/02 / PHIL-02/A | 9 |
| 1 | Teoria del linguaggio e della comunicazione C.A. | M-FIL/05 / PHIL-04/B | 9 |
| 1 | Filosofia della complessità: metodi e storia | M-FIL/06 / PHIL-05/A | 12 |
| 2 | Psicologia dei processi cognitivi | M-PSI/01 / PSIC-01/A | 9 |
| 2 | Filosofia della mente C.A. | M-FIL/05 / PHIL-04/B | 6 |
| 2 | Filosofia della psicologia | M-FIL/01 / PHIL-01/A (la pagina del piano dice PHIL-04/A: da verificare) | 9 |
| 2 | Altre conoscenze utili per il mondo del lavoro | — | 3 |
| 2 | Prova finale | — | 15 |

## Seminari (Altre conoscenze, 3 CFU)
- Completamento: 3 seminari da remoto in diretta OPPURE 2 in presenza (non si sommano in modo misto senza conferma della segreteria).
- Relazione finale: almeno 10.000 battute, inquadramento teorico, una sezione per seminario, bibliografia e sitografia. Va inviata alla segreteria di Filosofia, che comunica l'idoneità.
- Fonte degli annunci: "Avvisi di facoltà" sulla piattaforma e-learning.
- Si può partecipare già prima del test d'accesso.
- Ogni seminario va registrato in `seminari/tracker.yaml` lo stesso giorno, con appunti utili alla relazione.

## Comandi
- `make status`: CFU riconosciuti, acquisiti e mancanti, prerequisiti aperti, seminari validi, prossime scadenze (legge `piano/piano.yaml`, `seminari/tracker.yaml`, `admin/scadenze.md`). Richiede Python 3 con PyYAML.
- `make relazione`: conta le battute di `seminari/relazione/relazione.md` (o del template, se la relazione non esiste ancora) e le confronta con la soglia di 10.000.

## Esami
Appelli ogni 35-40 giorni. Scritti in sede esterna, uno al mese, al momento telematici. Orali solo a Roma. Per ogni insegnamento, in `esami/<slug>/`: programma ufficiale, testi, documenti di studio secondo le regole R1, prove di verifica, eventuale etivity.

## Raccordo con il dottorato
La convenzione di cotutela richiede la frequenza di almeno tre insegnamenti della LM-78 (scadenze indicative, slittate di un anno). Titolo della tesi di dottorato: "From deduction to meaning: logic in transformation in the era of the cognitive industry". Nei documenti di studio di Filosofia della complessità, Teoria dei processi cognitivi ed emotivi e Filosofia della mente, segnala esplicitamente i punti di contatto con la tesi.

Nel repository del Rationality Foundations Lab (`Aristofane7/fondamenti-razionalita`, file `content/curriculum.json`, chiave `decisioni_rinviate`, voci d1–d6) c'è un registro di decisioni rinviate (trigger: `ammissione_lm78`). La voce D1 riguarda il modulo M5 "Fenomenologia ed ermeneutica" come preparazione alle carenze M-FIL/01: tienine conto prima di preparare i materiali delle carenze, senza duplicarli.

## Scadenze note
- 14/11/2026: prova finale di Storia della Filosofia Moderna presso UniPegaso (Parma), che copre la carenza in Storia della filosofia
- dopo la verbalizzazione: certificato Pegaso scaricato, poi rinuncia agli studi a Pegaso
- 18/11/2026: convegno "Oriana Fallaci, «come un tarlo nella storia»" (primo seminario possibile)
- 04/12/2026: autocertificazione a Unicusano (l'autodichiarazione va depositata entro 30 giorni dall'iscrizione, pena il mancato riconoscimento dei titoli)
- dopo la verifica didattica: ricevuta della tassa regionale su Sophia (manuale, punto 3.1.3)
- entro dicembre 2026 (obiettivo): carenze + test d'accesso
- da gennaio 2027 (obiettivo): primi esami

## Cosa non fare
- Non inserire dati sensibili in chiaro (documenti, codici fiscali, IBAN).
- Non duplicare materiali del 1MG o del Lab: collegali.
- Non cambiare lo stato di un insegnamento in `piano.yaml` senza una fonte (verbale, mail della segreteria, schermata della piattaforma) annotata nel commit.
