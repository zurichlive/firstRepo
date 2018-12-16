# Admin.ch-Tool für Veranstaltungen und Mitteilungen

Tool zur Extrahierung und Auswertung von Medienmitteilungen und Veranstaltungen der Schweizer Bundesverwaltung (admin.ch). In einer ersten Version ist die Funktion der Veranstaltungen abgedeckt. Jede Veranstaltung im Veranstaltungskalender der Bundesverwaltung hat eine ID, vierstellig numerisch (XXXX). Die Zahl wird für neue Veranstaltungen jeweils erhöht und ist in der URL ersichtlich: https://www.admin.ch/gov/de/start/dokumentation/veranstaltungen.event-id-XXXX.html
Nicht jede Nummer ist vergeben, es gibt Lücken.

**Veranstaltungen**:
https://www.admin.ch/gov/de/start/dokumentation/veranstaltungen.html
**Medienmitteilungen**:
https://www.admin.ch/gov/de/start/dokumentation/medienmitteilungen.html?dyn_startDate=01.01.2017&dyn_organization=1


# Code-Dokumentation:

Wichtiger Hinweis zur Ausführung. Folgende Ordner-Struktur sollte im Projektordner vorhanden sein:

/html
/html/archive
/csvs

# Programm zur Extrahierung

**adminch_scrap.py**

Das Programm speichert Veranstaltungen mit bestimmten Veranstaltungs-ID vom Veranstaltungskalender auf admin.ch lokal ab. Dazu fragt das Programm nach zwei Inputs vom Nutzer (Veranstaltungs-ID), um die Range der Veranstaltungen zu bestimmen, die gespeichert werden sollen.

- Start id ist die ID der ersten Veranstaltung, die das Programm extrahieren soll. 
- End id ist die ID der letzten Veranstaltung, die das Programm extrahieren soll. 

Das Programm iteriert dann so lange bis die End id erreicht ist. Falls nur eine Veranstaltung mit einer ID extrahiert werden soll, muss und soll keine End id angegeben werden. Das Programm erstellt lokale html-Dateien in einem eigenen Unterverzeichnis (\html). Findet das Programm keine Veranstaltung mit einer ID in der Range, wird diese übersprungen.

Internet-Verbindung erforderlich.

**adminch_makecsv.py**

Das Programm erstellt aus den lokalen html-Dateien neue csv-Dateien in einem eigenen Unterverzeichnis (\csvs). Pro html-Datei erstellt es eine csv-Datei. Die verarbeiteten html-Dateien verschiebt es ins Archiv. Für Ausführung auf einem Server getestet.

# Programm zum Checken nach neuen Veranstaltungen

**adminch_serverupdate.py**

Dieses Programm ist zur Ausführung auf einem Server gedacht. Es checkt nach neuen Veranstaltungen im Veranstaltungskalender und speichert diese als html ab. Dazu sollten die csv der Veranstaltungen, aber mindestens das letzte csv im entsprechenden Ordner abgelegt sein (\csv). Denn das Programm startet ab der letzten ID, die bereits gespeichert wurde und checkt dann nach neuen Veranstaltungen bei den nächsten 100 ID. 

Zur weiteren Verarbeitung zu csv kann 1:1 das bestehende Programm **adminch_makecsv.py** verwendet werden.

# Programm zur Verarbeitung

**adminch_datamining.py** (work in progress!)

Das Programm lädt alle lokalen csv-Dateien und kombiniert sie zu einem einzelnen Dataframe. Durch dieses dynamische Vorgehen sind alle möglichen Veranstaltungs-Kategorie-Informationen berücksichtigt, auch zukünftige, die neu dazukommen. Das Programm reinigt die Daten, insbesondere das Datum, um damit arbeiten zu können. Zum Schluss speichert es das Dataframe in eine einzelne Arbeits-csv-Datei ("working.csv").

# Programm zur Auswertung

**adminch_stats.py** (work in progress!)

Fragen und Kontakt:
Florian Imbach, florian.imbach@srf.ch
