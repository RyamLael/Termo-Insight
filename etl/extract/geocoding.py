import requests
import time
from config.api.geocoding import GeocodingConfig

class GeocodingExtractor:


    def fetch_geocoding_for_cities(cities: list[str], state: str = "Ceará"):
        """
        Fetch geocoding for multiple cities in a given state.

        Args:
            cities (list[str]): List of city names
            state (str): State name

        Returns:
            list[dict]: List of geocoded cities
        """

        results = []

        for city in cities:
            try:
                geo = GeocodingExtractor.fetch_geocoding(city, state)

                if geo:
                    results.append(geo)

            except RuntimeError as e:
                print(f"Erro ao buscar {city}: {e}")
                continue

            time.sleep(0.2)

        return results

    @staticmethod
    def fetch_geocoding(city_name:str, state:str = "Ceará"):


        params = {
            "name": city_name,
            "countryCode": "BR",
            "count": 5
        }

        url = f"{GeocodingConfig.BASE_URL}"

        try:
            response = requests.get(url, params=params, timeout=GeocodingConfig.TIMEOUT)
            response.raise_for_status()

            data = response.json()
            results = data.get("results", [])

            best_match = GeocodingExtractor.select_best_city_match(results, state)

        except requests.RequestException as e:
            raise RuntimeError(f"Erro ao buscar municípios: {e}")

        except ValueError:
            raise RuntimeError("Erro ao converter resposta para JSON")

        return GeocodingExtractor.parse(best_match)

    @staticmethod
    def parse(item:dict):
        """
        Converte a resposta da API em estrutura padronizada.

        Args:
            item (dict): JSON retornado pela API

        Returns:
            dict: Geolocalização normalizada
        """

        if not item:
            return None

        try:
            return {
                "id": item.get("id"),
                "name": item.get("name"),
                "latitude": item.get("latitude"),
                "longitude": item.get("longitude"),
                "state": item.get("admin1"),
            }

        except (ValueError, TypeError):
            return None

    @staticmethod
    def select_best_city_match(data:list, state:str = "Ceará"):
        """
        Seleciona melhor correspondência baseada em país e estado.

        Args:
            data (list[dict]): List of geocoding data
            state (str): State name to filter (e.g., "Ceará")

        Returns:
            dict | None: Best matching city result or None if no results
        """

        candidates = [
            item for item in data
            if item.get("country_code") == "BR"
            and item.get("admin1", "").lower() == state.lower()
        ]

        if candidates:
            return max(candidates, key=lambda x: x.get("population", 0))

        return data[0] if data else None
