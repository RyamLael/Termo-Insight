
class OpenMeteoConfig():
    """
    Configurações da API de dados meteorológicos históricos (Open-Meteo).

    Utilizada para consultas na API de archive (reanalysis climático),
    incluindo parâmetros padrão de unidade e modelagem.
    """

    WEATHER_URL = f"https://archive-api.open-meteo.com/v1/archive"

    DEFAULT_PARAMS = {
        "timezone": "America/Fortaleza",
        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh",
        "precipitation_unit": "mm",
        "models": "auto",
    }