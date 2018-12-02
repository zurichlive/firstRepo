# Admin.ch-Tool für Veranstaltungen und Mitteilungen

Tool zur Extrahierung und Auswertung von Medienmitteilungen und Veranstaltungen der Schweizer Bundesverwaltung (admin.ch). In einer ersten Version ist die Funktion der Veranstaltungen abgedeckt. Jede Veranstaltung im Veranstaltungskalender der Bundesverwaltung hat eine ID, vierstellig numerisch (XXXX). Die Zahl wird für neue Veranstaltungen jeweils erhöht und ist in der URL ersichtlich: https://www.admin.ch/gov/de/start/dokumentation/veranstaltungen.event-id-XXXX.html
Nicht jede Nummer ist vergeben, es gibt Lücken.

https://www.admin.ch/gov/de/start/dokumentation/veranstaltungen.html
https://www.admin.ch/gov/de/start/dokumentation/medienmitteilungen.html?dyn_startDate=01.01.2017&dyn_organization=1

Code-Dokumentation:

# Programm zur Extrahierung: adminch_scrap.py

Programm fragt nach Ausführung nach zwei Inputs vom Nutzer. Start id ist die ID der ersten Veranstaltung, die das Programm extrahieren soll. End id ist die ID der letzten Veranstaltung, die das Programm extrahieren soll. Das Programm iteriert dann so lange bis End id erreicht ist. Falls nur eine Veranstaltung mit einer ID extrahiert werden soll, muss und soll keine End id angegeben werden.

Das Programm erstellt mit den Daten csv-Dateien. Nach 1000 Einträgen erstellt es eine neue Datei. Die Datei ist benannt nach dem Muster:
veranstaltungen_Start id_Anzahl Veranstaltungen extrahiert bis dahin_Zufallszahl.csv

# Programm zur Verarbeitung: adminch_makecsv.py / adminch_datamining.py

# Programm zur Auswertung: adminch_stats.py (work in progress!)

Fragen und Kontakt:
Florian Imbach, florian.imbach@srf.ch
