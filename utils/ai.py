import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_advice(location, weather, air):

    prompt = f"""
You are an AI community advisor.

Location:
{location}

Weather:
Temperature: {weather['temperature_2m']}°C
Feels Like: {weather['apparent_temperature']}°C
Humidity: {weather['relative_humidity_2m']}%
Wind Speed: {weather['wind_speed_10m']} km/h

Air Quality:
AQI: {air['us_aqi']}
PM2.5: {air['pm2_5']}
PM10: {air['pm10']}

Give:

1. Health advice
2. Travel advice
3. Outdoor activity advice
4. Clothing recommendation
5. Air quality precautions

Keep it under 150 words.

Use bullet points.

Add suitable emojis.
"""

    response = model.generate_content(prompt)

    return response.text