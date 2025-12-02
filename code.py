import base64
import geopandas as gpd
import pandas as pd
import folium
from streamlit_folium import st_folium
import streamlit as st
from functions import *

# ================== CONFIG ==================
st.set_page_config(
    page_title="The Data Project - Plataforma",
    page_icon="./static/logos/TDP-circle-white.svg",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ================== PATHS ===================
logo_path = "./static/logos/TDP_Logo_White.svg"
shp_path = "/data/PAN_adm2.shp"
tif_path = "./data/dem-cr.tiff"
# data_path = 
# csv_path = 

#  ================== ESTILOS ===================
st.markdown(f"""
<style>
/* ===== Tipografía: local (./static) con fallback a Google ===== */
@font-face {{
  font-family: 'PoppinsLocal';
  src: url('./static/Poppins-Regular.woff2') format('woff2'),
       url('./static/Poppins-Regular.ttf') format('truetype');
  font-weight: 300;
  font-style: normal;
  font-display: swap;
}}

/* ===== Fondo y contenedor principal ===== */
[data-testid="stAppViewContainer"] {{
  background: linear-gradient(90deg, #175CA1, #07A9E0 140%);
  background-attachment: fixed;
}}

/* ===== Cabecera (logo + título) ===== */
.header-row {{ display:flex; align-items:center; gap:12px; }}
.header-row h1 {{ margin:0; font-size:4vh; font-weight:500; color:#fff; }}
.header-row img {{ height:5vh; width:auto; }}


/* ===== Ajustes generales ===== */
.block-container label:empty {{ margin:0; padding:0; }}
footer {{ visibility: hidden; }}
section[data-testid="stSidebar"] {{ display:none !important; }}
header[data-testid="stHeader"] {{ display:none !important; }}
MainMenu {{ visibility: hidden; }}
main blockquote, .block-container {{ padding-top: 0.6rem; padding-bottom: 0.6rem; }}

/* ======================================================================================= */
/* ===== A PARTIR D'AQUÍ AFEGIU ELS ESTILS DEL GRAFICS Y ELEMENS QUE ANEU CONSTRUINT ===== */
/* ======================================================================================= */

</style>
""", unsafe_allow_html=True)


# ================== DATA (Aqui va la carga y procesado de datos) ==================
logo_data_uri = img_to_data_uri(logo_path)   #logo

# ========= Dades inventades =========
df = pd.DataFrame({
    "region": [
        "Central", "Brunca", "Chorotega",
        "Pacífico Central", "Huetar Norte", "Huetar Caribe", "Occidental"
    ],
    "variable": [1250, 480, 720, 610, 830, 540, 390]  
})
df["porcentaje"] = (df["variable"] / df["variable"].sum() * 100).round(1)

# L'aternativa es carregar aqui el df des d'un csv
# df = pd.read_csv(csv_path)

# ================== CABECERA ==================
st.markdown(
    f"""
    <div class="header-box">
      <div class="header-row">
        <img src="{logo_data_uri}" alt="TDP Logo" />
        <h1>Plataforma</h1>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ================== TABLERO ==================
columna1, columna2 = st.columns([2.8, 1]) # Aqui se definen las columnas y su tamaño
with columna1:
    col1, col2, col3 = st.columns([1, 1, 1]) # Aqui se definen las columnas y su tamaño

    with col1:
        with st.container(border=True):
            c1, c2 = st.columns([1, 6])
            with c1:
                demo_logo = img_to_data_uri('./static/logos/demografia.png')
                st.image(demo_logo, width=50)
            with c2:
                st.markdown("<p style='font-size: 2.5vh; font-weight: 300; color: #fff;'>Demografía y Territorio</p>", unsafe_allow_html=True)
            st.button("Censo poblacional")
            st.button("Tendencias demográficas")
            st.button("Migración interna")
            st.button("Uso del suelo")

    with col2:
        with st.container(border=True):
            c1, c2 = st.columns([1, 6])
            with c1:
                eco_logo = img_to_data_uri('./static/logos/economia.png')
                st.image(eco_logo, width=50)
            with c2:
                st.markdown("<p style='font-size: 2.5vh; font-weight: 300; color: #fff;'>Economía Local</p>", unsafe_allow_html=True)
            st.button("PIB regional")
            st.button("Tasa de empleo")
            st.button("Sectores económicos")
            st.button("Comercio local")

    with col3:
        with st.container(border=True):
            c1, c2 = st.columns([1, 6])
            with c1:
                salu_logo = img_to_data_uri('./static/logos/salud.png')
                st.image(salu_logo, width=50)
            with c2:
                st.markdown("<p style='font-size: 2.5vh; font-weight: 300; color: #fff;'>Salud</p>", unsafe_allow_html=True)
            st.button("Incidencia de enfermedades")
            st.button("Acceso a servicios de salud")
            st.button("Infraestructura sanitaria")
            st.button("Mapa de riesgo epidemiológico")

    col4, col5, col6 = st.columns([1, 1, 1]) # Aqui se definen las columnas y su tamaño
    with col4:
        with st.container(border=True):
            c1, c2 = st.columns([1, 6])
            with c1:
                eneg_logo = img_to_data_uri('./static/logos/energia.png')
                st.image(eneg_logo, width=50)
            with c2:
                st.markdown("<p style='font-size: 2.5vh; font-weight: 300; color: #fff;'>Servicios Públicos e Infraestructura</p>", unsafe_allow_html=True)
            st.button("Agua potable")
            st.button("Acceso a electricidad")
            st.button("Infraestructura energetica")
            st.button("Energias renovables")
    with col5:
        with st.container(border=True):
            c1, c2 = st.columns([1, 6])
            with c1:
                seg_logo = img_to_data_uri("./static/logos/movilidad y seguridad.png")
                st.image(seg_logo, width=50)
            with c2:
                st.markdown("<p style='font-size: 2.5vh; font-weight: 300; color: #fff;'>Seguridad y Movilidad</p>", unsafe_allow_html=True)
            st.button("Indice de criminalidad")
            st.button("Delitos reportados")
            st.button("Accidentes de tránsito")
            st.button("Infraestructura vial")
    
    with col6:
        with st.container(border=True):
            c1, c2 = st.columns([1, 6])
            with c1:
                opin_logo = img_to_data_uri("./static/logos/opinion.png")
                st.image(opin_logo, width=50)
            with c2:
                st.markdown("<p style='font-size: 2.5vh; font-weight: 300; color: #fff;'>Opinión pública</p>", unsafe_allow_html=True)
            st.button("Encuesta nacional")
            st.button("Encuesta de calidad de vida")
            st.button("Encuesta de percepción de seguridad")
            st.button("Encuesta de percepción del gobierno")

with columna2:
    # Carga del shp
        gdf = load_gdf_wgs84(shp_path)
        geojson_str, bounds, name_col = make_geojson_simplified(gdf, tol_m=200)
        # Centro y zoom
        minx, miny, maxx, maxy = bounds
        center_lat = (miny + maxy) / 2
        center_lon = (minx + maxx) / 2
        print(gdf.head())
        
        # show_regions = st.checkbox("Mostrar regiones", value=True)


        # --------------------- MAPA FOLIUM -------------------------------
        m = folium.Map(location=[center_lat, center_lon], 
                        zoom_start=3, 
                        tiles="cartodbpositron",
                        prefer_canvas=True,
                        control_scale=False,
                        zoom_control=False, #coulta els botosn de zoom de leaflet (per defecte)

                        )
        #--------------------------------------------------------------
        # AQUEST BLOC ES PER OCULTAR ELS CREDITS DE LEAFLET / CARTODB
        #--------------------------------------------------------------
        m.get_root().html.add_child(folium.Element("""
        <style>
        .leaflet-control-attribution {display:none !important;}
        .leaflet-container a {display:none !important;}
        </style>
        """))

        #--------------------- Afegir el geojson ----------------------
        folium.GeoJson(
            data=geojson_str,
            name="Regiones",
            smooth_factor=0.8,  # fa el geojson més suau i triga menys en carregar
            tooltip=folium.GeoJsonTooltip(
                fields=[name_col],
                aliases=["Región:"],
                sticky=True,
            ),
            style_function=lambda _:
                {"color": "#175CA1", "weight": 1.1, "opacity": 1,
                "fill": True, "fillColor": "#07A9E0", "fillOpacity": 0.15},
        ).add_to(m)

        # Definim els limits del mapa a partir del geojson
        m.fit_bounds([[miny, minx], [maxy, maxx]])
        st_folium(m, height=420, width=None)
    
        with st.container(border=True):
            st.markdown("<p style='font-size: 2.5vh; font-weight: 300; color: #fff;'>Alertas y Actualizaciones</p>", unsafe_allow_html=True)
            alerta1 = st.checkbox("Agua Potable - Actualización Datos 2025", value=False)
            alerta2 = st.checkbox("Energía Renovable - Datos Eólica [Nuevo]", value=False)
            alerta4 = st.checkbox("Salud Pública - Actualización Datos 2024", value=False)
            # Aquí puedes agregar más elementos como gráficos, tablas

# with st.container(border=True):

#     st.markdown('bla bla bla')
       
