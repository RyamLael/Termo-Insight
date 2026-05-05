
class OpenMeteoConfig():

    WEATHER_URL = f"https://archive-api.open-meteo.com/v1/archive"
    AIR_QUALITY_URL = f"https://air-quality-api.open-meteo.com/v1/air-quality"

    DEFAULT_PARAMS = {
        "timezone": "America/Fortaleza",
        "temperature_unit": "celcius",
        "wind_speed_unit": "km/h",
        "precipitation_unit": "mm",
        "models": "auto",
    }