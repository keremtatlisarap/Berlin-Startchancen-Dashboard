# Berlin Startchancen Dashboard (English Version of this below)

Beim Berlin Startchancen Dashboard handelt es sich um eine Webanwendung, die das Schüler-Lehrer-Verhältnis an Berliner Schulen untersucht, die am Startchancen-Programm teilnehmen.

**Projekt:** https://berlin-startchancen-dashboard.streamlit.app

## 1. Grundlegende Informationen

### Was ist das Startchancen-Programm?

Zunächst muss geklärt werden, was das Startchancen-Programm ist. Das Startchancen-Programm ist das größte Bildungsprogramm Deutschlands. Es trägt dazu bei, dass Bund und Länder gemeinsam in Schulen investieren, die einen hohen Anteil sozial benachteiligter Schülerinnen und Schüler aufweisen.

### Warum ist mein Projekt relevant?

Finanzielle Investitionen sind oftmals notwendig, um einen hohen Bildungsstandard für alle aufrechterhalten zu können. Dennoch denke ich, dass das Schüler-Lehrer-Verhältnis die Bildungsqualität in hohem Maße mitbestimmt. Selbst innerhalb derselben Stadt – in diesem Fall Berlin – können große Unterschiede zwischen den Bezirken entstehen, die zu Ungleichheiten führen können.

Mithilfe dieses Projekts gehe ich der Frage nach: Wie gut sind die Schulen personell besetzt, die aufgrund sozialer Benachteiligung besonders auf eine gute Lehrkräfteversorgung angewiesen sind?

### Motivation für das Projekt

Ich wollte meine Programmierfähigkeiten und Ideen nutzen, um reale gesellschaftliche Herausforderungen zu untersuchen und zu überprüfen, ob es potenzielle Probleme beim Schüler-Lehrer-Verhältnis an Berliner Startchancen-Schulen gibt.


## 2. Kernfunktionen 

Die Anwendung verarbeitet Daten des Berliner Senats und stellt diese in einer interaktiven Oberfläche mit zwei Ansichten dar. Dadurch eignet sie sich sowohl für eine berlinweite Analyse als auch für die detaillierte Betrachtung einzelner Bezirke.

### Ansicht 1: Berlinweiter Überblick 

* Zusammenfassung von: Anzahl der Startchancen-Schulen, der gesamten Schülerzahl, der Anzahl der Lehrkräfte sowie des durchschnittlichen Schüler-Lehrer-Verhältnisses über alle Berliner Bezirke hinweg.
* Es gibt einen Bezirksvergleich (Dynamisches Balkendiagramm). Dieses visualisiert das durchschnittliche Schüler-Lehrer-Verhältnis aller zwölf Berliner Bezirke. Balken werden automatisch rot gefärbt, wenn der Bezirk über dem Berliner Durchschnitt liegt,und blau, wenn er darunter liegt.
* Es wird auch verteilt nach Schularten (Boxplot-Analyse). 
* Zuletzt, gibt es eine Rangliste der zehn Schulen mit dem höchsten Schüler-Lehrer-Verhältnis. 

### Ansicht 2: Bezirksanalyse 

* Nach Auswahl eines Bezirks wird automatisch berechnet, wie stark dieser vom Berliner Durchschnitt abweicht.
* Ein interaktives Diagramm zeigt alle Startchancen-Schulen des ausgewählten Bezirks. Beim Überfahren eines Datenpunkts mit der Maus werden zusätzliche Informationen wie die genaue Schülerzahl und die Anzahl der Lehrkräfte angezeigt.
* Ein Balkendiagramm visualisiert die Geschlechterverteilung der Lehrkräfte 
* Eine Zusammenfassung berechnet Durchschnittswerte für die verschiedenen Schularten innerhalb des ausgewählten Bezirks.
* Es gibt eine filterbare Datentabelle mit integrierter Downloadfunktion. Sie ermöglicht den Export der aufbereiteten Daten als CSV-Datei.



## 3. Verwendete Technologien

* **Programmiersprache:** Python 
* **Datenverarbeitung:** Pandas 
* **Datenvisualisierung:** Plotly Express und Plotly Graph Objects 
* **Frontend:** Streamlit 
* **Parsing-Bibliotheken:** lxml (HTML-Parsing), xlrd und openpyxl


## Hinweis zur Verwendung von KI:

Ich habe dieses Projekt eigenständig konzipiert, strukturiert und inhaltlich ausgearbeitet. Bei der technischen Umsetzung des Codes, wurde generative KI unterstützend als Werkzeug zur Code-Generierung und Fehlerbehebung eingesetzt. Die Kontrolle, das Zusammenführen der Datensätze und die Sicherstellung valider Ergebnisse, lagen vollständig in meiner Verantwortung. 

# English Summary of this:

The Berlin Startchancen Dashboard is a web application that examines the student-teacher ratio at Berlin schools participating in the Startchancen-Programm 

**Project:** https://berlin-startchancen-dashboard.streamlit.app

The Startchancen Program is Germany’s largest education funding initiative, aiming to financially support schools with a high share of socially disadvantaged students.
While financial investment is oftentimes necessary to maintain a high standard of education I believe the student-teacher ratio also plays a major role in shaping educational quality. Even within the same city (Berlin) significant disparities between districts can arise leading to inequality. With the help of this project, I investigate the question: how well-staffed are the schools that due to social disadvantage depend most heavily on an adequate amount of teachers?

I wanted to apply my programming skills and ideas to examine a real societal issue checking whether there are potential problems with the student-teacher-ratio at Berlin’s Startchancen schools.

This application processes data from the Berlin Senate and presents it through an interactive interface with two views. A Berlin-wide overview (comparing all districts by average student-teacher ratio, distribution by school type and a ranking of the ten schools with the highest ratios) and a district level analysis (how much that district deviates from the Berlin average, teacher gender distribution, etc.)

**Technologies used:** Python, Pandas, Plotly Express/Graph objects, Streamlit, lxml, xlcd, openpyxl.

## Note on AI use:

I independently conceived and structured the content of this project. I used generative AI as a supporting tool for code generation and debugging during the implementation. However, reviewing the results, merging the datasets and ensuring their validity remained entirely my own responsibility.


# Quellen / Sources

This project is built entirely on official, publicly available civic data provided by the State of Berlin via the Berlin Open Data Portal (daten.berlin.de).

Senatsverwaltung für Bildung, Jugend und Familie (2025): Schulen im Startchancen-Programm. Berlin Open Data. Verfügbar unter: https://daten.berlin.de/datensaetze/schulen-im-starchancen-programm-1570794 (Letzter Zugriff: 25.06.2026).

Senatsverwaltung für Bildung, Jugend und Familie (2024): Schulen in Berlin. Berlin Open Data. Verfügbar unter: https://daten.berlin.de/datensaetze/schulen-in-berlin-1096779 (Letzter Zugriff: 25.06.2026).

Note: All data used is published under open-government licenses (dl-de-zero-2.0 / CC-BY) allowing public modification and processing.
