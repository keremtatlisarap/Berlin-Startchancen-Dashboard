"""
Startchancen-Schulen Berlin – Betreuungsschlüssel-Dashboard
Starte mit: streamlit run app.py
Dateien im gleichen Ordner: startchancen-schulen-bearb.xlsx, Tab.xls
"""

import re
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ── Seitenkonfiguration ──────────────────────────────────────────────────────

st.set_page_config(
    page_title="Startchancen-Schulen Berlin",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Styling ──────────────────────────────────────────────────────────────────

st.markdown("""
<style>
  /* Schriftart & Basis */
  @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono&display=swap');
  html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif; }

  /* Metrikkarten */
  [data-testid="metric-container"] {
    background: #F0F4F8;
    border-left: 4px solid #1A56DB;
    border-radius: 6px;
    padding: 14px 18px;
  }
  [data-testid="metric-container"] label { color: #4A5568; font-size: 0.78rem; letter-spacing: .06em; text-transform: uppercase; }
  [data-testid="metric-container"] [data-testid="stMetricValue"] { font-size: 1.9rem; font-weight: 600; color: #1A202C; }
  [data-testid="metric-container"] [data-testid="stMetricDelta"] { font-size: 0.82rem; }

  /* Tabelle */
  [data-testid="stDataFrame"] { border: 1px solid #E2E8F0; border-radius: 6px; }

  /* Sidebar */
  [data-testid="stSidebar"] { background: #1A202C; }
  [data-testid="stSidebar"] * { color: #E2E8F0 !important; }
  [data-testid="stSidebar"] .stSelectbox label { font-size: 0.78rem; letter-spacing: .06em; text-transform: uppercase; }

  /* Trennlinie */
  hr { border-color: #E2E8F0; margin: 1.5rem 0; }

  /* Warnbox */
  .warn-box { background: #FFFBEB; border-left: 4px solid #F6AD55; border-radius: 6px;
              padding: 10px 14px; font-size: 0.85rem; color: #744210; margin-top: 1rem; }
</style>
""", unsafe_allow_html=True)

# ── Datenladen (gecacht) ─────────────────────────────────────────────────────

@st.cache_data
def load_data():
    startchancen = pd.read_excel("startchancen-schulen-bearb.xlsx")

    for col in ["Telefonnummer", "E-Mailadresse"]:
        if col in startchancen.columns:
            startchancen[col] = startchancen[col].astype(str).apply(
                lambda x: re.sub(r"<[^>]+>", "", x).strip()
            )

    startchancen["Schulnummer"] = startchancen["Schulnummer"].astype(str).str.strip().str.upper()

    statistik = pd.read_html("Tab.xls", encoding="latin1", header=0)[0]
    statistik.columns = [
        "Schuljahr", "BSN", "Name",
        "Schueler_gesamt", "Schueler_w", "Schueler_m",
        "Lehrkraefte_gesamt", "Lehrkraefte_w", "Lehrkraefte_m",
    ]
    statistik["BSN"] = statistik["BSN"].astype(str).str.strip().str.upper()

    aktuellstes_schuljahr = statistik["Schuljahr"].max()
    statistik_aktuell = statistik[statistik["Schuljahr"] == aktuellstes_schuljahr].copy()

    merged = startchancen.merge(
        statistik_aktuell, left_on="Schulnummer", right_on="BSN",
        how="left", suffixes=("_sc", "_stat"),
    )

    analyse = merged.dropna(subset=["Schueler_gesamt", "Lehrkraefte_gesamt"]).copy()
    analyse = analyse[analyse["Lehrkraefte_gesamt"] > 0].copy()
    analyse["Betreuungsschluessel"] = (
        analyse["Schueler_gesamt"] / analyse["Lehrkraefte_gesamt"]
    ).round(2)

    bezirk_stats = (
        analyse.groupby("Bezirk")
        .agg(
            Anzahl_Schulen=("Schulnummer", "count"),
            Schueler_gesamt=("Schueler_gesamt", "sum"),
            Lehrkraefte_gesamt=("Lehrkraefte_gesamt", "sum"),
            BS_Mittel=("Betreuungsschluessel", "mean"),
            BS_Min=("Betreuungsschluessel", "min"),
            BS_Max=("Betreuungsschluessel", "max"),
        )
        .round(2)
    )
    bezirk_stats["BS_Gesamt"] = (
        bezirk_stats["Schueler_gesamt"] / bezirk_stats["Lehrkraefte_gesamt"]
    ).round(2)

    nicht_gefunden = merged[merged["BSN"].isna()][["Schulnummer", "Schulname"]]

    return analyse, bezirk_stats, aktuellstes_schuljahr, nicht_gefunden

# ── Daten laden ──────────────────────────────────────────────────────────────

try:
    analyse, bezirk_stats, schuljahr, nicht_gefunden = load_data()
except FileNotFoundError as e:
    st.error(f"Datei nicht gefunden: {e}\n\nBitte `startchancen-schulen-bearb.xlsx` und `Tab.xls` in denselben Ordner wie `app.py` legen.")
    st.stop()

gesamtschluessel = analyse["Schueler_gesamt"].sum() / analyse["Lehrkraefte_gesamt"].sum()
alle_bezirke = sorted(analyse["Bezirk"].unique())

# ── Sidebar ──────────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("## 🏫 Startchancen-Schulen")
    st.markdown(f"**Schuljahr {schuljahr}**")
    st.markdown("---")

    ansicht = st.radio(
        "ANSICHT",
        ["Berlinweite Übersicht", "Bezirksdetail"],
        index=0,
    )

    if ansicht == "Bezirksdetail":
        st.markdown("")
        gewaehlter_bezirk = st.selectbox(
            "BEZIRK WÄHLEN",
            alle_bezirke,
            index=0,
        )

        schularten_im_bezirk = sorted(
            analyse[analyse["Bezirk"] == gewaehlter_bezirk]["Schulart"].unique()
        )
        gewahlte_schularten = st.multiselect(
            "SCHULART FILTERN",
            schularten_im_bezirk,
            default=schularten_im_bezirk,
        )

    st.markdown("---")
    st.markdown(
        "<small style='opacity:.5'>Datenquelle: Senatsverwaltung für Bildung Berlin</small>",
        unsafe_allow_html=True,
    )

# ── Hauptbereich ─────────────────────────────────────────────────────────────

BLAU = "#1A56DB"
ROT  = "#E53E3E"
GRAU = "#718096"

if ansicht == "Berlinweite Übersicht":

    st.title("Betreuungsschlüssel an Berliner Startchancen-Schulen")
    st.caption(f"Schulen im Startchancen-Programm (sozial benachteiligte Gebiete) · Schuljahr {schuljahr}")

    # KPI-Zeile
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Schulen gesamt", len(analyse))
    k2.metric("Schülerinnen & Schüler", f"{int(analyse['Schueler_gesamt'].sum()):,}".replace(",", "."))
    k3.metric("Lehrkräfte", f"{int(analyse['Lehrkraefte_gesamt'].sum()):,}".replace(",", "."))
    k4.metric("Ø Betreuungsschlüssel", f"{gesamtschluessel:.1f}", help="Schüler pro Lehrkraft, berlinweit über alle Startchancen-Schulen")

    st.markdown("---")

    col_links, col_rechts = st.columns([3, 2], gap="large")

    with col_links:
        st.subheader("Betreuungsschlüssel nach Bezirk")

        bezirk_sorted = bezirk_stats.sort_values("BS_Gesamt")
        farben = [ROT if v > gesamtschluessel else BLAU for v in bezirk_sorted["BS_Gesamt"]]

        fig_bar = go.Figure(go.Bar(
            y=bezirk_sorted.index,
            x=bezirk_sorted["BS_Gesamt"],
            orientation="h",
            marker_color=farben,
            text=bezirk_sorted["BS_Gesamt"].apply(lambda x: f"{x:.1f}"),
            textposition="outside",
            hovertemplate="<b>%{y}</b><br>%{x:.2f} Schüler/Lehrkraft<extra></extra>",
        ))
        fig_bar.add_vline(
            x=gesamtschluessel, line_dash="dash", line_color=GRAU, line_width=1.5,
            annotation_text=f"Ø {gesamtschluessel:.1f}", annotation_font_size=11,
            annotation_position="top right",
        )
        fig_bar.update_layout(
            height=420, margin=dict(l=0, r=60, t=10, b=30),
            xaxis_title="Schüler pro Lehrkraft",
            yaxis_title=None,
            plot_bgcolor="white",
            xaxis=dict(gridcolor="#EDF2F7", range=[0, bezirk_sorted["BS_Gesamt"].max() * 1.18]),
            font=dict(family="IBM Plex Sans"),
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with col_rechts:
        st.subheader("Verteilung nach Schulart")

        schularten = (
            analyse.groupby("Schulart")["Betreuungsschluessel"]
            .apply(list)
        )
        schularten = schularten[schularten.apply(len) >= 3]

        fig_box = go.Figure()
        for schulart, werte in schularten.items():
            fig_box.add_trace(go.Box(
                y=werte, name=schulart,
                marker_color=BLAU, line_color=BLAU,
                boxmean=True,
                hovertemplate="%{y:.1f}<extra>" + schulart + "</extra>",
            ))
        fig_box.add_hline(
            y=gesamtschluessel, line_dash="dash", line_color=GRAU, line_width=1.5,
            annotation_text=f"Ø {gesamtschluessel:.1f}", annotation_font_size=11,
        )
        fig_box.update_layout(
            height=420, margin=dict(l=0, r=20, t=10, b=80),
            yaxis_title="Schüler pro Lehrkraft",
            xaxis_title=None,
            showlegend=False,
            plot_bgcolor="white",
            yaxis=dict(gridcolor="#EDF2F7"),
            font=dict(family="IBM Plex Sans"),
        )
        st.plotly_chart(fig_box, use_container_width=True)

    st.markdown("---")
    st.subheader("Top 10 — höchster Betreuungsschlüssel")

    top10 = (
        analyse[["Schulname", "Bezirk", "Schulart", "Schueler_gesamt", "Lehrkraefte_gesamt", "Betreuungsschluessel"]]
        .sort_values("Betreuungsschluessel", ascending=False)
        .head(10)
        .reset_index(drop=True)
    )
    top10.index += 1
    st.dataframe(
        top10.rename(columns={
            "Schulname": "Schule", "Schueler_gesamt": "Schüler",
            "Lehrkraefte_gesamt": "Lehrkräfte", "Betreuungsschluessel": "Schlüssel",
        }),
        use_container_width=True,
        column_config={
            "Schlüssel": st.column_config.ProgressColumn(
                "Schlüssel", min_value=0, max_value=30, format="%.2f"
            )
        },
    )

    if not nicht_gefunden.empty:
        st.markdown(
            f"<div class='warn-box'>⚠ {len(nicht_gefunden)} Schule(n) ohne Statistik-Treffer "
            f"(kein BSN-Match): {', '.join(nicht_gefunden['Schulname'].tolist())}</div>",
            unsafe_allow_html=True,
        )

# ── Bezirksdetail-Ansicht ────────────────────────────────────────────────────

else:
    bezirk_df = analyse[
        (analyse["Bezirk"] == gewaehlter_bezirk) &
        (analyse["Schulart"].isin(gewahlte_schularten))
    ].copy()

    if bezirk_df.empty:
        st.warning("Keine Schulen für diese Auswahl.")
        st.stop()

    bezirk_schluessel = bezirk_df["Schueler_gesamt"].sum() / bezirk_df["Lehrkraefte_gesamt"].sum()
    delta = bezirk_schluessel - gesamtschluessel

    st.title(gewaehlter_bezirk)
    st.caption(f"Startchancen-Schulen · Schuljahr {schuljahr}")

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Schulen", len(bezirk_df))
    k2.metric("Schüler", f"{int(bezirk_df['Schueler_gesamt'].sum()):,}".replace(",", "."))
    k3.metric("Lehrkräfte", f"{int(bezirk_df['Lehrkraefte_gesamt'].sum()):,}".replace(",", "."))
    k4.metric(
        "Ø Betreuungsschlüssel",
        f"{bezirk_schluessel:.2f}",
        delta=f"{delta:+.2f} ggü. Berlin",
        delta_color="inverse",
        help="Negativ = weniger Schüler pro Lehrkraft als Berliner Durchschnitt (besser)",
    )

    st.markdown("---")

    col_l, col_r = st.columns([3, 2], gap="large")

    with col_l:
        st.subheader("Schulen im Bezirk")

        bezirk_sorted = bezirk_df.sort_values("Betreuungsschluessel", ascending=True)
        farben_b = [ROT if v > gesamtschluessel else BLAU for v in bezirk_sorted["Betreuungsschluessel"]]

        fig_b = go.Figure(go.Bar(
            y=bezirk_sorted["Schulname"].str[:45],
            x=bezirk_sorted["Betreuungsschluessel"],
            orientation="h",
            marker_color=farben_b,
            text=bezirk_sorted["Betreuungsschluessel"].apply(lambda x: f"{x:.1f}"),
            textposition="outside",
            customdata=bezirk_sorted[["Schulname", "Schulart", "Schueler_gesamt", "Lehrkraefte_gesamt"]].values,
            hovertemplate=(
                "<b>%{customdata[0]}</b><br>"
                "%{customdata[1]}<br>"
                "Schüler: %{customdata[2]:.0f} · Lehrkräfte: %{customdata[3]:.0f}<br>"
                "<b>Schlüssel: %{x:.2f}</b><extra></extra>"
            ),
        ))
        fig_b.add_vline(
            x=gesamtschluessel, line_dash="dash", line_color=GRAU, line_width=1.5,
            annotation_text=f"Berlin Ø {gesamtschluessel:.1f}", annotation_font_size=10,
            annotation_position="top right",
        )
        fig_b.update_layout(
            height=max(300, len(bezirk_df) * 32),
            margin=dict(l=0, r=70, t=10, b=30),
            xaxis_title="Schüler pro Lehrkraft",
            yaxis_title=None,
            plot_bgcolor="white",
            xaxis=dict(gridcolor="#EDF2F7", range=[0, bezirk_df["Betreuungsschluessel"].max() * 1.2]),
            font=dict(family="IBM Plex Sans"),
        )
        st.plotly_chart(fig_b, use_container_width=True)

    with col_r:
        st.subheader("Geschlechterverteilung")

        schueler_w = int(bezirk_df["Schueler_w"].sum())
        schueler_m = int(bezirk_df["Schueler_m"].sum())
        lk_w = int(bezirk_df["Lehrkraefte_w"].sum())
        lk_m = int(bezirk_df["Lehrkraefte_m"].sum())

        fig_pie = go.Figure()
        fig_pie.add_trace(go.Bar(
            name="weiblich", x=["Schülerinnen & Schüler", "Lehrkräfte"],
            y=[schueler_w, lk_w], marker_color="#63B3ED",
            text=[f"{schueler_w:,}".replace(",", "."), f"{lk_w:,}".replace(",", ".")],
            textposition="inside",
        ))
        fig_pie.add_trace(go.Bar(
            name="männlich", x=["Schülerinnen & Schüler", "Lehrkräfte"],
            y=[schueler_m, lk_m], marker_color=BLAU,
            text=[f"{schueler_m:,}".replace(",", "."), f"{lk_m:,}".replace(",", ".")],
            textposition="inside",
        ))
        fig_pie.update_layout(
            barmode="stack", height=280,
            margin=dict(l=0, r=0, t=10, b=10),
            plot_bgcolor="white",
            legend=dict(orientation="h", y=-0.15),
            font=dict(family="IBM Plex Sans"),
            yaxis=dict(gridcolor="#EDF2F7"),
        )
        st.plotly_chart(fig_pie, use_container_width=True)

        st.subheader("Schularten im Bezirk")
        schulart_counts = bezirk_df.groupby("Schulart").agg(
            Schulen=("Schulname", "count"),
            Schlüssel=("Betreuungsschluessel", "mean"),
        ).round(2).sort_values("Schlüssel", ascending=False)
        st.dataframe(schulart_counts, use_container_width=True)

    st.markdown("---")
    st.subheader("Alle Schulen – Detailtabelle")

    anzeige = bezirk_df[[
        "Schulname", "Schulart", "Adresse",
        "Schueler_gesamt", "Lehrkraefte_gesamt", "Betreuungsschluessel",
        "E-Mailadresse", "Telefonnummer",
    ]].sort_values("Betreuungsschluessel", ascending=False).reset_index(drop=True)
    anzeige.index += 1

    st.dataframe(
        anzeige.rename(columns={
            "Schulname": "Schule", "Schulart": "Art",
            "Schueler_gesamt": "Schüler", "Lehrkraefte_gesamt": "Lehrkräfte",
            "Betreuungsschluessel": "Schlüssel",
            "E-Mailadresse": "E-Mail",
        }),
        use_container_width=True,
        column_config={
            "Schlüssel": st.column_config.ProgressColumn(
                "Schlüssel", min_value=0, max_value=30, format="%.2f"
            )
        },
    )

    # CSV-Download
    csv = anzeige.to_csv(index=False).encode("utf-8")
    st.download_button(
        label=f"⬇ CSV herunterladen – {gewaehlter_bezirk}",
        data=csv,
        file_name=f"betreuungsschluessel_{gewaehlter_bezirk.replace(' ', '_')}.csv",
        mime="text/csv",
    )
