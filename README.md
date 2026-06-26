# Berlin Startchancen Dashboard (English Version of this below)

Beim **Berlin Startchancen Dashboard** handelt es sich um eine Webanwendung, die das Schüler-Lehrer-Verhältnis an Berliner Schulen untersucht, die am Startchancen-Programm teilnehmen.

**Projekt:** berlin-startchancen-dashboard.streamlit.app

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

### Ansicht 1: Berlinweiter Überblick (Makroperspektive)

* Zusammenfassung von: Anzahl der Startchancen-Schulen, der gesamten Schülerzahl, der Anzahl der Lehrkräfte sowie des durchschnittlichen Schüler-Lehrer-Verhältnisses über alle Berliner Bezirke hinweg.
* Es gibt einen Bezirksvergleich (Dynamisches Balkendiagramm). Dieses visualisiert das durchschnittliche Schüler-Lehrer-Verhältnis aller zwölf Berliner Bezirke. Balken werden automatisch rot gefärbt, wenn der Bezirk über dem Berliner Durchschnitt liegt,und blau, wenn er darunter liegt.
* Es wird auch verteilt nach Schularten (Boxplot-Analyse). Dies zeigt die statistische Verteilung (Minimum, Maximum, Median und Quartile) verschiedener Schularten (z. B. Grundschulen oder Oberstufenzentren), um strukturelle Unterschiede bei der Personalausstattung sichtbar zu machen.
* Zuletzt, gibt es eine Rangliste der zehn Schulen mit dem höchsten Schüler-Lehrer-Verhältnis. 

### Ansicht 2: Bezirksanalyse (Mikroperspektive)

* Nach Auswahl eines Bezirks wird automatisch berechnet, wie stark dieser vom Berliner Durchschnitt abweicht.
* Ein interaktives Diagramm zeigt alle Startchancen-Schulen des ausgewählten Bezirks. Beim Überfahren eines Datenpunkts mit der Maus werden zusätzliche Informationen wie die genaue Schülerzahl und die Anzahl der Lehrkräfte angezeigt.
* Ein gestapeltes Balkendiagramm visualisiert die Geschlechterverteilung der Lehrkräfte und ermöglicht demografische Analysen.
* Eine Zusammenfassung berechnet Durchschnittswerte für die verschiedenen Schularten innerhalb des ausgewählten Bezirks.
* Eine filterbare Datentabelle mit integrierter Downloadfunktion ermöglicht den Export der aufbereiteten Daten als CSV-Datei, beispielsweise für weiterführende wissenschaftliche Analysen.


## 3. Datenaufbereitung und Datenpipeline

Eine der größten Herausforderungen dieses Projekts war die Zusammenführung unterschiedlicher Datensätze. Die Anwendung bereinigt und verknüpft automatisch zwei voneinander unabhängige Datensätze des Berliner Open-Data-Portals (`daten.berlin.de`):

1. **Startchancen-Verzeichnis:** Eine `.xlsx`-Datei mit der offiziellen Liste aller Startchancen-Schulen.
2. **Personalstatistik des Berliner Senats:** Eine `.xls`-Datei, deren Inhalte als HTML-Struktur eingebettet sind und institutionelle Personaldaten enthalten.

### Schritte der Datenaufbereitung in Python

* **Datenbereinigung:** Mithilfe regulärer Ausdrücke (`re`) wurden verschachtelte HTML-Tags aus Kontaktfeldern wie Telefonnummern und E-Mail-Adressen entfernt.
* **Normalisierung der Schlüssel:** Entwicklung eines robusten Zuordnungssystems, das unterschiedliche Schulkennungen (`Schulnummer` und `BSN`) in ein einheitliches Format ohne Leerzeichen und ausschließlich in Großbuchstaben überführt.
* **Algorithmische Zusammenführung:** Die Datensätze wurden mithilfe eines `inner merge` in `pandas` zusammengeführt, sodass ausschließlich eindeutig verifizierte und übereinstimmende Schulprofile in die Visualisierung übernommen werden.


## 4. Verwendete Technologien

* **Programmiersprache:** Python 
* **Datenverarbeitung:** Pandas (DataFrames, Datenbereinigung und Zusammenführung)
* **Datenvisualisierung:** Plotly Express und Plotly Graph Objects (interaktive, webbasierte Diagramme)
* **Frontend-Framework:** Streamlit (Benutzeroberfläche, responsive Layouts und interaktive Widgets)
* **Parsing-Bibliotheken:** `lxml` (HTML-Parsing), `xlrd` und `openpyxl` (Verarbeitung älterer und moderner Excel-Dateien)


# English Version

# Berlin Startchancen Dashboard

The **Berlin Startchancen Dashboard** is a web application that analyzes the student-to-teacher ratio at Berlin schools participating in the Startchancen Program.

**Project:** berlin-startchancen-dashboard.streamlit.app

## 1. General Information

### What is the Startchancen Program?

First, it is important to understand what the Startchancen Program is. The Startchancen Program is Germany's largest education initiative. It enables the federal and state governments to jointly invest in schools with a high proportion of socially disadvantaged students.

### Why is this project relevant?

Financial investment is often essential for maintaining a high standard of education for everyone. However, I believe that the student-to-teacher ratio is also a key factor influencing educational quality. Even within the same city—in this case, Berlin—substantial differences can exist between districts, potentially contributing to educational inequality.

This project explores the following question: **How well staffed are the schools that rely most heavily on adequate teacher availability due to serving socially disadvantaged student populations?**

### Project Motivation

I wanted to use my programming skills and ideas to investigate real-world social challenges and examine whether there are potential issues regarding the student-to-teacher ratio at Berlin's Startchancen schools.


## 2. Core Features

The application processes official data provided by the Berlin Senate and presents it through an interactive interface with two different views. This allows users to perform both citywide analyses and detailed district-level investigations.

### View 1: Berlin-Wide Overview (Macro Perspective)

* Summary of the total number of Startchancen schools, total student enrollment, total number of teachers, and the average student-to-teacher ratio across all Berlin districts.
* District comparison (dynamic bar chart). This visualization compares the average student-to-teacher ratio across Berlin's twelve districts. Bars are automatically highlighted in red if a district exceeds the Berlin average and in blue if it falls below it.
* Distribution by school type (box plot analysis). This visualization displays the statistical distribution (minimum, maximum, median, and quartiles) for different school types (e.g., primary schools or upper secondary vocational schools), making structural differences in staffing levels more visible.
* A ranking of the ten schools with the highest student-to-teacher ratios.

### View 2: District Analysis (Micro Perspective)

* After selecting a district, the application automatically calculates how much it deviates from the Berlin-wide average.
* An interactive scatter plot displays all Startchancen schools within the selected district. Hovering over a data point reveals additional information, including the exact number of students and teachers.
* A stacked bar chart visualizes the gender distribution of teachers, enabling demographic analyses.
* A summary table calculates average values for the different school types within the selected district.
* A filterable data table with an integrated download feature allows users to export the processed data as a CSV file for further research or analysis.


## 3. Data Preparation and Data Pipeline

One of the biggest challenges of this project was integrating multiple independent datasets. The application automatically cleans and combines two separate datasets from Berlin's Open Data Portal (`daten.berlin.de`):

1. **Startchancen Directory:** An `.xlsx` file containing the official list of all Startchancen schools.
2. **Berlin Senate Staff Statistics:** An `.xls` file whose contents are embedded as an HTML structure and contain institutional staffing data.

### Data Processing Steps in Python

* **Data cleaning:** Regular expressions (`re`) were used to remove nested HTML tags from contact fields such as phone numbers and email addresses.
* **Key normalization:** A robust mapping system was developed to convert different school identifiers (`Schulnummer` and `BSN`) into a standardized format without whitespace and using uppercase letters only.
* **Algorithmic data integration:** The datasets were merged using an `inner merge` in `pandas`, ensuring that only uniquely verified and matching school records were included in the final visualizations.


## 4. Technologies Used

* **Programming Language:** Python
* **Data Processing:** Pandas (DataFrames, data cleaning, and dataset merging)
* **Data Visualization:** Plotly Express and Plotly Graph Objects (interactive web-based visualizations)
* **Frontend Framework:** Streamlit (user interface, responsive layouts, and interactive widgets)
* **Parsing Libraries:** `lxml` (HTML parsing), `xlrd`, and `openpyxl` (processing legacy and modern Excel files)

# Quellen / Sources

This project is built entirely on official, publicly available civic data provided by the State of Berlin via the Berlin Open Data Portal (`daten.berlin.de`).

Senatsverwaltung für Bildung, Jugend und Familie (2025): Schulen im Startchancen-Programm. Berlin Open Data. Verfügbar unter: https://daten.berlin.de/datensaetze/schulen-im-starchancen-programm-1570794 (Zugriff: 25.06.2026).

Senatsverwaltung für Bildung, Jugend und Familie (2024): Schulen in Berlin. Berlin Open Data. Verfügbar unter: https://daten.berlin.de/datensaetze/schulen-in-berlin-1096779 (Zugriff: 25.06.2026).

Note: All data used is published under open-government licenses (dl-de-zero-2.0 / CC-BY) allowing public modification and processing.
