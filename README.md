# Berlin-Startchancen-Dashboard

An advanced data science web application exploring and visualizing the student-to-teacher ratio at Berlin schools participating in the federal Startchancen-Programm. 

**Live Application:** https://berlin-startchancen-dashboard.streamlit.app
**Source Code:** 


## 1. Project Background & Social Relevance

### What is the "Startchancen-Programm"?
The Startchancen-Programm is the largest and most heavily funded educational equity initiative in the history of Germany. Jointly financed by the federal and state governments, it aims to decouple academic success from socioeconomic backgrounds. The program targets schools with a high percentage of socially disadvantaged students, providing them with additional funding, infrastructure, and specialized personnel. (https://www.berlin.de/sen/bildung/unterstuetzung/startchancen-programm/)

### Why is this Research Crucial?
Financial investments are vital. However I believe that the local student-to-teacher ratio (Betreuungsschlüssel)** is of high relevamce when determining the level of educational quality. Even though all of these schools are in Berlin, structural differences between districts can lead to major disparities. I wanted to build this project in order to answer the question of how well-staffed schools in Berlin are that belong the Startchancen-Programm

### Motivation behind this Project
I wanted to utilize my programming skills to address a real-world issue. I am a huge advocate of improving educational quality for everyone. For that to happen I believe a project like this one could be a small step in that direction by being able to observe actual statistics and recognize regional disparities. As a result of that, one could see where one can find a deficiency of teachers in Startchancen-Programm Schulen. I believe this to be vital since if you want to fix a problem you need to first be able to recognize a problem. 


## 2. Core Features & Architecture

The application processes raw data from the Berlin Senate and provides an interactive dual-view interface designed for both macro-level (Berlin-wide) policy analysis and micro-level (district-level) school inspection.

### View 1: Berlin-Wide Overview (Macro Perspective)
- **Key Performance Indicators:** Aggregation showing the total number of processed Startchancen-schools, total enrolled students, total teaching staff, and the calculated cross-district average student-to-teacher ratio.
- **District Comparison (Dynamic Bar Chart):** Visualizes the average ratio for all 12 Berlin districts. Includes a dynamic threshold system: bars automatically turn red if a district's ratio exceeds the Berlin-wide average, or blue if it stays below it.
- **School Type Distribution (Boxplot Analysis):** Displays statistical spreads (min, max, median, quartiles) grouped by school types (e.g., Grundschulen, Oberstufenzentren) to identify systemic staffing anomalies.
- **Top 10 High-Load Analytics:** A leaderboard tracking the 10 schools with the most demanding student-to-teacher workloads, utilizing custom embedded Streamlit progress bars.

### View 2: District-Level Insights (Micro Perspective)
- **Contextual Delta Metrics:** Selecting a specific district automatically computes how much better or worse that region performs compared to the Berlin average.
- **Granular School Tooltips:** An interactive plot charting every single Startchancen-school within the selected district. Hovering over a data point reveals deep information, including exact enrollment numbers and available staff.
- **Staff Gender Demographics:** A stacked bar chart visualizing the gender ratio of the teaching faculty, enabling demographic analysis across educational institutions.
- **School-Type Aggregations:** A clean data summary compiling sub-averages specifically for the types of schools located in that district.
- **Curated Raw Data & Export:** A filterable database table equipped with a custom download feature, allowing users to extract the finalized dataset as a clean CSV file for secondary academic research.

---

## 3. Data Engineering & Pipeline

A key challenge of this project was data fusion. The application programmatically cleans and links two completely different datasets provided by the Berlin Open Data Portal (`daten.berlin.de`):
1. **The Startchancen Registry:** An `.xlsx` file containing the official list of target schools.
2. **The Senate's Personnel Statistics:** An underlying HTML structure wrapped inside a `.xls` file containing institutional data.

### Preprocessing Steps in Python:
- **Sanitization:** Applied Regular Expressions (`re`) to strip nested HTML tags out of contact fields (phone numbers/emails) from the registry.
- **Key Normalization:** Created a robust matching system by transforming heterogeneous school identifiers (`Schulnummer` and `BSN`) into standardized, white-space-free, uppercase strings.
- **Algorithmic Join:** Executed an inner merge using `pandas` to ensure only perfectly verified, cross-referenced school profiles enter the visualization pipeline.

---

## 4. Technology Stack

- **Programming Language:** Python 3.11+
- **Data Wrangling:** Pandas (Dataframes, cleaning, merges)
- **Data Visualization:** Plotly Express & Plotly Graph Objects (Interactive, web-native plotting)
- **Frontend Framework:** Streamlit (UI components, responsive layouts, interactive widgets)
- **Parsing Engines:** `lxml` (HTML parsing), `xlrd` / `openpyxl` (Legacy and modern Excel processing)

---

## 5. Local Setup & Installation

To run this dashboard locally on your machine, follow these steps:

1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git)
   cd YOUR-REPO-NAME
