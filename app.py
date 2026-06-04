import streamlit as st
import pandas as pd
import geopandas as gpd
import pydeck as pdk

st.set_page_config(page_title="Wind Farm Prediction Dashboard", layout="wide")

st.title("🌬️ Wind Farm Socioeconomic Analysis Dashboard")
st.markdown("**Predicting Wind Farm Presence in Iowa, Oklahoma & Texas**")

# ============================================================
# LOAD DATA
# ============================================================
@st.cache_data
def load_data():
    gdf = gpd.read_parquet("data/processed/tracts_with_predictions.parquet")
    gdf = gdf.to_crs(epsg=4326)
    gdf["predicted_prob_pct"] = (gdf["predicted_prob"] * 100).round(1)
    return gdf

gdf = load_data()

# ============================================================
# SIDEBAR FILTERS
# ============================================================
st.sidebar.header("Filters")

# State filter
states = ["IA", "OK", "TX"]
selected_states = st.sidebar.multiselect(
    "Select States", 
    options=states, 
    default=states
)

# Probability range filter
min_prob, max_prob = st.sidebar.slider(
    "Predicted Probability Range",
    min_value=0.0,
    max_value=1.0,
    value=(0.0, 1.0),
    step=0.05
)

# Filter data
filtered_gdf = gdf[
    (gdf["STUSPS"].isin(selected_states)) &
    (gdf["predicted_prob"] >= min_prob) &
    (gdf["predicted_prob"] <= max_prob)
]

st.sidebar.markdown(f"**Showing {len(filtered_gdf):,} tracts**")

# ============================================================
# MAIN CONTENT
# ============================================================

# ---- Overview ----
st.header("Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Tracts Shown", f"{len(filtered_gdf):,}")
col2.metric("Model ROC-AUC", "0.830")
col3.metric("Avg Predicted Probability", f"{filtered_gdf['predicted_prob'].mean():.2%}")

# ---- Interactive Map (Predicted Probability Only) ----
st.header("Interactive Map: Predicted Probability of Wind Farm Presence")

layer = pdk.Layer(
    "GeoJsonLayer",
    filtered_gdf,
    opacity=0.85,
    stroked=True,
    filled=True,
    get_fill_color=[
        "200 + (55 * predicted_prob)",
        "150 * (1 - predicted_prob)",
        "255 * (1 - predicted_prob)"
    ],
    get_line_color=[255, 255, 255],
    get_line_width=0.3,
    pickable=True,
    auto_highlight=True,
)

view_state = pdk.ViewState(latitude=35.0, longitude=-98.0, zoom=5)

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={
        "html": """
        <b>GEOID:</b> {GEOID}<br/>
        <b>Predicted Probability:</b> {predicted_prob_pct}%<br/>
        <b>Actual Wind Farm:</b> {has_wind_farm}
        """
    },
    map_style="mapbox://styles/mapbox/light-v9"
)

st.pydeck_chart(deck, use_container_width=True)

# ---- Model Insights ----
st.header("Model Insights")
st.write("**Top Drivers of Wind Farm Presence:**")
st.markdown("""
- **Higher median household income** → increases probability  
- **Lower median home value** → strongly increases probability  
- **Higher housing density** → increases probability  
- **Older housing stock** → slightly increases probability
""")

st.caption("Model: Improved Logistic Regression | ROC-AUC = 0.830")

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.caption("Built with Streamlit + PyDeck | Data: USWTDB + ACS 2022 5-Year")