import requests

def get_air_quality(lat, lon):

    url = (
        "https://air-quality-api.open-meteo.com/v1/air-quality?"
        f"latitude={lat}"
        f"&longitude={lon}"
        "&current=pm2_5,pm10,us_aqi"
    )

    response = requests.get(url)

    return response.json()["current"]