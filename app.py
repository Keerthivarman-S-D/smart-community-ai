import streamlit as st
from utils.weather import get_coordinates, get_weather, get_forecast
from utils.charts import (
    create_forecast_chart,
    plot_temperature,
    plot_humidity,
    plot_wind,
    score_gauge
)
from utils.score import calculate_score
from utils.ai import generate_advice
from utils.air_quality import get_air_quality
from utils.map import show_map

st.set_page_config(
    page_title="Smart Community AI",
    page_icon="🌍",
    layout="wide"
)

st.sidebar.title("🌍 Smart Community AI")

st.sidebar.write(
"""
Helping citizens make smarter decisions using live data.
"""
)

st.sidebar.markdown("---")

st.sidebar.write("Version 1.0")

st.sidebar.write("Built with ❤️ using Streamlit")

st.markdown("""
# 🌍 Smart Community AI

### AI-powered decision support for healthier and smarter communities

Analyze weather, air quality and receive personalized AI recommendations in seconds.
""")

st.write("Helping citizens make smarter daily decisions.")

city = st.text_input("Enter your city", "Chennai")

if st.button("Analyze"):

    location = get_coordinates(city)

    if location is None:
        st.error("City not found")

    else:
        air = get_air_quality(
            location["latitude"],
            location["longitude"]
        )
        
        weather = get_weather(
            location["latitude"],
            location["longitude"]
        )

        st.info(f"""
        ## 📍 {location['name']}

        Country: **{location['country']}**
        """)
        
        st.divider()

        left, right = st.columns([2,1])

        with left:
            st.subheader("Current Weather")

            c1, c2, c3, c4 = st.columns(4)

            c1.metric(
                "🌡 Temperature",
                f"{weather['temperature_2m']}°C"
            )

            c2.metric(
                "💧 Humidity",
                f"{weather['relative_humidity_2m']}%"
            )

            c3.metric(
                "🤒 Feels Like",
                f"{weather['apparent_temperature']}°C"
            )

            c4.metric(
                "💨 Wind",
                f"{weather['wind_speed_10m']} km/h"
            )
        
        with right:
            st.subheader("Current Air Quality")

            aqi = air["us_aqi"]

            if aqi <= 50:
                st.success(f"🟢 AQI: {aqi} (Good)")
            elif aqi <= 100:
                st.warning(f"🟡 AQI: {aqi} (Moderate)")
            elif aqi <= 150:
                st.error(f"🟠 AQI: {aqi} (Unhealthy for Sensitive Groups)")
            else:
                st.error(f"🔴 AQI: {aqi} (Unhealthy)")

            col1, col2 = st.columns(2)

            col1.metric("PM2.5", air["pm2_5"])
            col2.metric("PM10", air["pm10"])
        
        forecast = get_forecast(
            location["latitude"],
            location["longitude"]
        )

        df = create_forecast_chart(forecast)
        
        st.divider()

        st.subheader("📈 5-Day Forecast")

        tab1, tab2, tab3 = st.tabs([
            "Temperature",
            "Humidity",
            "Wind"
        ])

        with tab1:
            st.plotly_chart(
            plot_temperature(df),
            width="stretch",
            key="temp_chart"
        )

        with tab2:
            st.plotly_chart(
            plot_humidity(df),
            width="stretch",
            key="humidity_chart"
        )

        with tab3:
            st.plotly_chart(
            plot_wind(df),
            width="stretch",
            key="wind_chart"
        )
        
        st.divider()

        st.subheader("🤖 AI Smart Recommendations")
        
        with st.spinner("Analyzing today's conditions..."):

            advice = generate_advice(
                location["name"],
                weather,
                air
            )
            
        with st.container(border=True):
            st.markdown(advice)
            
        st.divider()

        # -----------------------
        # Community Wellness Score
        # -----------------------

        score = calculate_score(weather, air)

        st.subheader("🏆 Community Wellness Score")

        st.plotly_chart(
            score_gauge(score),
            width="stretch",
            key="community_score_gauge"
        )
        
        if score >= 80:
            st.success("🟢 Excellent community conditions today!")
        elif score >= 60:
            st.warning("🟡 Moderate conditions. Take some precautions.")
        else:
            st.error("🔴 Poor conditions. Outdoor activities are not recommended.")

        st.divider()

        # -----------------------
        # Location Map
        # -----------------------

        st.subheader("📍 Location Map")

        show_map(
            location["latitude"],
            location["longitude"]
        )
        
        st.divider()
        
        score = calculate_score(weather, air)

        st.subheader("🏆 Community Wellness Score")
        
        st.plotly_chart(
            score_gauge(score),
            use_container_width=True
        )
        if score >= 80:
            st.success("🟢 Excellent community conditions today!")
        elif score >= 60:
            st.warning("🟡 Moderate conditions. Take some precautions.")
        else:
            st.error("🔴 Poor conditions. Outdoor activities are not recommended.")        
        
        st.divider()
        
        st.subheader("📍 Location Map")

        show_map(
            location["latitude"],
            location["longitude"]
        )
