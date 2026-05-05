class GeocodingConfig():
    """
    Configuração do serviço de geocoding (cidade -> latitude/longitude).
    """

    BASE_URL = "https://geocoding-api.open-meteo.com/v1/search"

    PARAMS_DEFAULT = {
        "count": 1,          # retorna apenas o resultado mais relevante
        "language": "pt",    # nomes em português
        "format": "json",
        "country_code": "BR"
    }

    # Timeout para requisições HTTP
    TIMEOUT = 10
