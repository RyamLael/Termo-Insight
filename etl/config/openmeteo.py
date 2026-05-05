
class OpenMeteoConfig():

    WEATHER_URL = f"https://archive-api.open-meteo.com/v1/archive"

    DEFAULT_PARAMS = {
        "timezone": "America/Fortaleza",
        "temperature_unit": "celcius",
        "wind_speed_unit": "km/h",
        "precipitation_unit": "mm",
        "models": "auto",
    }