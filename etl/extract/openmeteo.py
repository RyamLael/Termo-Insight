import requests
from config.api.openmeteo import OpenMeteoConfig


class WeatherExtractor:

    @staticmethod
    def fetch_weather(latitude: float, longitude: float, start_date: str, end_date: str):
        """
        Busca dados meteorológicos históricos diários.

        Args:
            latitude (float)
            longitude (float)
            start_date (str): YYYY-MM-DD
            end_date (str): YYYY-MM-DD

        Returns:
            list[dict]
        """

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "start_date": start_date,
            "end_date": end_date,
            "daily": [
                "temperature_2m_mean",
                "temperature_2m_max",
                "temperature_2m_min",
                "relative_humidity_2m_mean",
                "precipitation_sum",
                "precipitation_probability_mean",
                "apparent_temperature_mean",
                "wind_speed_10m_mean",
                "wind_speed_10m_max",
                "wind_gusts_10m_mean",
                "wind_gusts_10m_max",
                "wind_direction_10m_dominant",
                "surface_pressure_mean",
                "cloudcover_mean",
                "vapour_pressure_deficit_max",
                "et0_fao_evapotranspiration",
                "wet_bulb_temperature_2m_mean",
                "uv_index_max",
                "sunshine_duration",
                "shortwave_radiation_sum",
                "dew_point_2m_mean",
                "dew_point_2m_min"
            ],
            **OpenMeteoConfig.DEFAULT_PARAMS
        }

        try:
            response = requests.get(
                OpenMeteoConfig.WEATHER_URL,
                params=params,
                timeout=OpenMeteoConfig.TIMEOUT
            )
            response.raise_for_status()

            data = response.json()

        except requests.RequestException as e:
            raise RuntimeError(f"Erro ao buscar dados climáticos: {e}")

        except ValueError:
            raise RuntimeError("Erro ao converter resposta para JSON")

        return WeatherExtractor.parse(data)

    @staticmethod
    def parse(data: dict):
        """
        Converte resposta da API em lista estruturada.
        """

        daily = data.get("daily", {})

        if not daily:
            return []

        results = []

        for i in range(len(daily["time"])):
            try:
                results.append({
                    "data": daily["time"][i],
                    "temperatura_med": daily["temperature_2m_mean"][i],
                    "temp_max": daily["temperature_2m_max"][i],
                    "temp_min": daily["temperature_2m_min"][i],
                    "umidade_ar_med": daily["relative_humidity_2m_mean"][i],
                    "precipitacao_total": daily["precipitation_sum"][i],
                    "prob_chuva_med": daily["precipitation_probability_mean"][i],
                    "sensacao_termica_med": daily["apparent_temperature_mean"][i],
                    "vel_vento_med_10m": daily["wind_speed_10m_mean"][i],
                    "vel_vento_max_10m": daily["wind_speed_10m_max"][i],
                    "vel_rajada_vento_med_10m": daily["wind_gusts_10m_mean"][i],
                    "vel_rajada_vento_max_10m": daily["wind_gusts_10m_max"][i],
                    "dir_vento_predominante_10m": daily["wind_direction_10m_dominant"][i],
                    "pressao_superficie_med": daily["surface_pressure_mean"][i],
                    "cobertura_nuvem_med": daily["cloudcover_mean"][i],
                    "VPD_max": daily["vapour_pressure_deficit_max"][i],
                    "evotranspiracao_referencia_total": daily["et0_fao_evapotranspiration"][i],
                    "temp_bulbo_umido_med": daily["wet_bulb_temperature_2m_mean"][i],
                    "indice_uv_max": daily["uv_index_max"][i],
                    "duracao_luz_solar": daily["sunshine_duration"][i],
                    "radiacao_solar_total": daily["shortwave_radiation_sum"][i],
                    "ponto_de_orvalho_med": daily["dew_point_2m_mean"][i],
                    "ponto_de_orvalho_min": daily["dew_point_2m_min"][i],
                })

            except (KeyError, TypeError, IndexError):
                continue

        return results
