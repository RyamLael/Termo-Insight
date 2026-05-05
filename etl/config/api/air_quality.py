
class AirQualityConfig():
    """
    Configurações da API de dados de qualidade do ar (Open-Meteo).
    """

    AIR_QUALITY_URL = f"https://air-quality-api.open-meteo.com/v1/air-quality"

    DEFAULT_PARAMS = {
        "timezone": "America/Fortaleza",
        "models": "auto",
    }