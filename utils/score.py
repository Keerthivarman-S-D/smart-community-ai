from utils.weather import get_coordinates, get_weather, get_forecast

def calculate_score(weather, air):
    """
    Calculate Community Wellness Score (0-100)
    based on Weather + Air Quality.
    """

    score = 100

    # Current weather
    temp = weather["temperature_2m"]
    humidity = weather["relative_humidity_2m"]
    wind = weather["wind_speed_10m"]

    # Air Quality
    aqi = air["us_aqi"]

    # -------------------------
    # Temperature
    # -------------------------
    if temp >= 40:
        score -= 30
    elif temp >= 35:
        score -= 20
    elif temp >= 30:
        score -= 10

    # -------------------------
    # Humidity
    # -------------------------
    if humidity >= 90:
        score -= 15
    elif humidity >= 80:
        score -= 10
    elif humidity >= 70:
        score -= 5

    # -------------------------
    # Wind Speed
    # -------------------------
    if wind >= 40:
        score -= 15
    elif wind >= 25:
        score -= 8

    # -------------------------
    # Air Quality Index
    # -------------------------
    if aqi >= 200:
        score -= 35
    elif aqi >= 150:
        score -= 25
    elif aqi >= 100:
        score -= 15
    elif aqi >= 50:
        score -= 5

    # Keep score between 0 and 100
    score = max(0, min(score, 100))

    return score