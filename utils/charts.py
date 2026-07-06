import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def create_forecast_chart(forecast):

    df = pd.DataFrame({
        "Time": forecast["time"],
        "Temperature": forecast["temperature_2m"],
        "Humidity": forecast["relative_humidity_2m"],
        "Wind": forecast["wind_speed_10m"]
    })

    return df


def plot_temperature(df):
    return px.line(
        df,
        x="Time",
        y="Temperature",
        title="🌡 Temperature Forecast"
    )


def plot_humidity(df):
    return px.line(
        df,
        x="Time",
        y="Humidity",
        title="💧 Humidity Forecast"
    )


def plot_wind(df):
    return px.line(
        df,
        x="Time",
        y="Wind",
        title="💨 Wind Speed Forecast"
    )
    
def score_gauge(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,

            title={"text": "Community Wellness Score"},

            gauge={
                "axis": {"range": [0, 100]},

                "bar": {"color": "green"},

                "steps": [
                    {"range": [0, 40], "color": "red"},
                    {"range": [40, 70], "color": "orange"},
                    {"range": [70, 100], "color": "lightgreen"},
                ],
            },
        )
    )

    return fig