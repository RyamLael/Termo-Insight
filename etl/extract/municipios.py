import requests
from config.api.municipios import MunicipiosConfig

class MunicipiosExtractor:


    @staticmethod
    def fetch_municipios(estado_id:str = MunicipiosConfig.STATE_ID):

        """
        Faz requisição para obter todos os municípios de um estado.

        Args:
            estado_id(str): ID do estado usado na requisição

        Returns: 
            list[dict]: Lista de municipios normalizados
        """

        url = f"{MunicipiosConfig.BASE_URL}{estado_id}/municipios"

        try:
            response = requests.get(url, timeout=MunicipiosConfig.TIMEOUT)
            response.raise_for_status()
            data = response.json()

        except requests.RequestException as e:
            raise RuntimeError(f"Erro ao buscar municípios: {e}")

        except ValueError:
            raise RuntimeError("Erro ao converter resposta para JSON")

        return MunicipiosExtractor.parse(data)
    
    @staticmethod
    def parse(data):
        """
        Converte a resposta da API em estrutura padronizada.

        Args:
            data (list): JSON retornado pela API

        Returns:
            list[dict]: Lista de municípios normalizados
        """

        municipios = []

        for item in data:
            try:
                municipios.append({
                    "id": item["id"],
                    "nome": item["nome"],
                    # ajuste aqui dependendo da estrutura real:
                    "estado_id": item["UF-id"]
                })
            except KeyError as e:
                raise RuntimeError(f"Erro ao parsear município: campo ausente {e}")

        return municipios
