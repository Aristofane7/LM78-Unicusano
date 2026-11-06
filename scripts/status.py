#!/usr/bin/env python3
"""Stato della LM-78: CFU, prerequisiti, seminari, scadenze. Uso: make status [OGGI=GG/MM/AAAA]."""
import re
import sys
from datetime import date, datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Serve PyYAML: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent


def load(rel):
    with open(ROOT / rel, encoding="utf-8") as f:
        return yaml.safe_load(f)


def oggi():
    for a in sys.argv[1:]:
        if a.strip():
            return datetime.strptime(a.strip(), "%d/%m/%Y").date()
    return date.today()


def scadenze(path):
    righe = []
    for line in (ROOT / path).read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not line.lstrip().startswith("|") or len(cells) < 4 or cells[0] in ("Data", "") or set(cells[0]) <= {"-"}:
            continue
        data, tipo, voce, fatto = cells[:4]
        try:
            d = datetime.strptime(data, "%d/%m/%Y").date()
        except ValueError:
            d = None
        righe.append({"data": d, "testo_data": data, "tipo": tipo, "voce": voce, "fatto": fatto.lower() == "x"})
    return righe


def main():
    today = oggi()
    piano = load("piano/piano.yaml")
    ins = piano["insegnamenti"]
    tot = piano["cfu_totali"]

    ric = sum(i["cfu"] for i in ins if i["stato"] == "riconosciuto")
    sup = [i for i in ins if i["stato"] == "superato"]
    acq_esami = sum(i["cfu"] for i in sup)
    da = [i for i in ins if i["stato"] == "da_sostenere"]
    mancanti = sum(i["cfu"] for i in da)

    print(f"LM-78 — stato al {today:%d/%m/%Y}")
    print("=" * 40)
    print("CFU")
    print(f"  riconosciuti:     {ric}")
    print(f"  acquisiti esami:  {acq_esami}")
    print(f"  acquisiti totali: {ric + acq_esami}/{tot}")
    print(f"  da sostenere:     {mancanti} ({len(da)} attività)")
    if piano.get("riconoscimento") == "provvisorio":
        print("  (riconoscimento provvisorio: in attesa della delibera della Giunta)")
    for anno in sorted({i["anno"] for i in ins if "anno" in i}):
        s_anno = sum(i["cfu"] for i in ins if i.get("anno") == anno)
        if s_anno != 60:
            print(f"  ATTENZIONE: anno {anno} = {s_anno} CFU, attesi 60")
    if ric + acq_esami + mancanti != tot:
        print(f"  ATTENZIONE: la somma ({ric + acq_esami + mancanti}) non torna con {tot}")

    pre = piano["prerequisiti"]
    aperte = [c for c in pre["carenze"] if c["stato"] != "colmata"]
    ta = pre["test_accesso"]
    print("\nPrerequisiti")
    print(f"  carenze aperte: {len(aperte)}")
    for c in aperte:
        print(f"    - {c['nome']} ({c['ssd']}, {c['cfu']} CFU)")
    if ta["stato"] != "superato":
        print(f"  test d'accesso: {ta['stato']} — BLOCCANTE (nessun esame prima di carenze + test)")
    else:
        print("  test d'accesso: superato")

    sem = load("seminari/tracker.yaml")
    regola = sem["regola"]
    validi = [s for s in (sem.get("seminari") or []) if s.get("valido", True)]
    rem = sum(1 for s in validi if s.get("modalita") == "remoto")
    pres = sum(1 for s in validi if s.get("modalita") == "presenza")
    completo = rem >= regola["remoto_richiesti"] or pres >= regola["presenza_richiesti"]
    print("\nSeminari (Altre conoscenze, 3 CFU)")
    print(f"  remoto in diretta: {rem}/{regola['remoto_richiesti']}")
    print(f"  in presenza:       {pres}/{regola['presenza_richiesti']}")
    if completo:
        print("  requisito soddisfatto: inviare la relazione (≥ 10.000 battute) alla segreteria")
    elif rem and pres:
        print("  attenzione: modalità miste, non si sommano senza conferma della segreteria")

    voci = [v for v in scadenze("admin/scadenze.md") if not v["fatto"]]
    future = sorted((v for v in voci if v["data"] and v["data"] >= today), key=lambda v: v["data"])
    scad = [v for v in future if v["tipo"] == "scadenza"]
    eventi = [v for v in future if v["tipo"] == "evento"]
    print("\nScadenze")
    if scad:
        p = scad[0]
        print(f"  prossima scadenza: {p['data']:%d/%m/%Y} — {p['voce']} (tra {(p['data'] - today).days} giorni)")
    else:
        print("  prossima scadenza: nessuna con data certa")
    for v in eventi[:3]:
        print(f"  evento: {v['data']:%d/%m/%Y} — {v['voce']}")
    scadute = [v for v in voci if v["data"] and v["data"] < today]
    for v in scadute:
        print(f"  SCADUTA, non spuntata: {v['data']:%d/%m/%Y} — {v['voce']}")
    for v in voci:
        if not v["data"]:
            print(f"  [{v['testo_data']}] {v['voce']}")


if __name__ == "__main__":
    main()
