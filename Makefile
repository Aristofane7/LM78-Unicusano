PY ?= python3
REL := $(if $(wildcard seminari/relazione/relazione.md),seminari/relazione/relazione.md,seminari/relazione/template.md)

.PHONY: status relazione

status:
	@$(PY) scripts/status.py $(OGGI)

relazione:
	@$(PY) scripts/battute.py $(REL)
