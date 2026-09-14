"""
Démo Streamlit — Affichage cartographique avec pydeck (fond OpenStreetMap)
============================================================================

Pour lancer l'application :
    pip install -r requirements.txt
    streamlit run app.py

Le fichier `donnees.csv` doit contenir au minimum deux colonnes :
    latitude, longitude
(des colonnes supplémentaires comme "nom" ou "valeur" sont optionnelles
et utilisées ici pour la couleur/taille des points et les infobulles).
"""

import pandas as pd
import pydeck as pdk
import streamlit as st

# --------------------------------------------------------------------------
# Configuration générale de la page
# --------------------------------------------------------------------------
st.set_page_config(
    page_title="Démo carto — pydeck + OpenStreetMap",
    page_icon="🗺️",
    layout="wide",
)

st.title("🗺️ Démo — Carte de données avec pydeck sur fond OpenStreetMap")
st.caption("Exemple pédagogique pour un cours de Python en production (Streamlit)")

# --------------------------------------------------------------------------
# 1. Chargement des données
# --------------------------------------------------------------------------
st.sidebar.header("⚙️ Paramètres")

fichier_uploade = st.sidebar.file_uploader(
    "Charger un CSV (colonnes: latitude, longitude, ...)", type=["csv"]
)

@st.cache_data
def charger_donnees(source) -> pd.DataFrame:
    """Charge un CSV et vérifie la présence des colonnes latitude/longitude."""
    df = pd.read_csv(source)
    df.columns = [c.strip().lower() for c in df.columns]
    if "latitude" not in df.columns or "longitude" not in df.columns:
        raise ValueError(
            "Le CSV doit contenir des colonnes 'latitude' et 'longitude'."
        )
    return df

# Si l'utilisateur ne charge rien, on utilise le CSV d'exemple fourni
if fichier_uploade is not None:
    df = charger_donnees(fichier_uploade)
else:
    df = charger_donnees("streamlit/donnees.csv")
    st.sidebar.info("Aucun fichier chargé : utilisation de `donnees.csv` (exemple).")

st.sidebar.write(f"**{len(df)}** points chargés")

# --------------------------------------------------------------------------
# 2. Réglages d'affichage (widgets interactifs)
# --------------------------------------------------------------------------
rayon_points = st.sidebar.slider("Taille des points (m)", 500, 20000, 4000, step=500)
opacite = st.sidebar.slider("Opacité des points", 0.1, 1.0, 0.8)
style_fond = st.sidebar.selectbox(
    "Fond de carte",
    options=["OpenStreetMap (clair)", "OpenStreetMap (standard)"],
)

# Tuiles OpenStreetMap : on les fournit nous-mêmes via TileLayer
# (pas besoin de jeton Mapbox/Carto)
url_tuiles = (
    "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
    if style_fond == "OpenStreetMap (standard)"
    else "https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png"
)

couche_fond = pdk.Layer(
    "TileLayer",
    data=url_tuiles,
    min_zoom=0,
    max_zoom=19,
    tile_size=256,
)

# --------------------------------------------------------------------------
# 3. Filtre optionnel sur une colonne numérique (si présente, ex: "valeur")
# --------------------------------------------------------------------------
colonnes_numeriques = [
    c for c in df.select_dtypes("number").columns if c not in ("latitude", "longitude")
]

df_filtre = df
if colonnes_numeriques:
    col_filtre = st.sidebar.selectbox("Filtrer sur la colonne", ["(aucun)"] + colonnes_numeriques)
    if col_filtre != "(aucun)":
        vmin, vmax = float(df[col_filtre].min()), float(df[col_filtre].max())
        seuil = st.sidebar.slider(
            f"Seuil minimum — {col_filtre}", vmin, vmax, vmin
        )
        df_filtre = df[df[col_filtre] >= seuil]

# --------------------------------------------------------------------------
# 4. Couche de points (ScatterplotLayer)
# --------------------------------------------------------------------------
couche_points = pdk.Layer(
    "ScatterplotLayer",
    data=df_filtre,
    get_position="[longitude, latitude]",
    get_radius=rayon_points,
    get_fill_color="[200, 30, 0, 160]",
    opacity=opacite,
    pickable=True,
    stroked=True,
    get_line_color=[255, 255, 255],
    line_width_min_pixels=1,
)

# --------------------------------------------------------------------------
# 5. Vue initiale (centrée sur le barycentre des points)
# --------------------------------------------------------------------------
vue_initiale = pdk.ViewState(
    latitude=df_filtre["latitude"].mean() if len(df_filtre) else 46.6,
    longitude=df_filtre["longitude"].mean() if len(df_filtre) else 2.2,
    zoom=5,
    pitch=0,
)

# Infobulle : on liste dynamiquement les colonnes disponibles
colonnes_infobulle = [c for c in df.columns if c not in ("latitude", "longitude")]
texte_infobulle = "<br/>".join([f"<b>{c}</b>: {{{c}}}" for c in colonnes_infobulle])
texte_infobulle += "<br/><b>lat/lon</b>: {latitude}, {longitude}"

carte = pdk.Deck(
    map_style=None,
    layers=[couche_points],
    initial_view_state=vue_initiale,
    tooltip={"html": texte_infobulle} if colonnes_infobulle else True,
    map_provider=None,  # on n'utilise pas de fond Mapbox/Carto natif, mais nos tuiles OSM
)

# --------------------------------------------------------------------------
# 6. Affichage
# --------------------------------------------------------------------------
col1, col2 = st.columns([3, 1])

with col1:
    st.pydeck_chart(carte, use_container_width=True)

with col2:
    st.metric("Points affichés", len(df_filtre))
    if colonnes_numeriques:
        st.metric(
            f"Moyenne ({colonnes_numeriques[0]})",
            round(df_filtre[colonnes_numeriques[0]].mean(), 1) if len(df_filtre) else "—",
        )

st.subheader("📋 Données")
st.dataframe(df_filtre, use_container_width=True, hide_index=True)

st.caption(
    "Fond de carte : © contributeurs OpenStreetMap — tuiles servies via TileLayer pydeck."
)
