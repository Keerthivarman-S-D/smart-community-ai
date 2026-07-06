import folium
from streamlit_folium import st_folium

def show_map(lat, lon):

    m = folium.Map(
        location=[lat, lon],
        zoom_start=12
    )

    folium.Marker(
        [lat, lon],
        tooltip="Selected Location"
    ).add_to(m)

    return st_folium(
        m,
        width=700,
        height=400
    )