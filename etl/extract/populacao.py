import requests
from config.api.populacao import PopulacaoConfig

class PopulationExtractor:


    @staticmethod
    def fetch_populacao(anos="last", nivel="municipio", estado_id=None, municipios_ids=None):

        """
        Busca dados de população no SIDRA.

        Args:
            anos (str): "2022", "2020,2021", "2015-2022", "last"
            estado_id (int): ex: n3 (Ceará)
            municipios_ids (list[int]): lista de códigos IBGE

        Returns:
            list[dict]
        """

        if municipios_ids:
            municipios_str = ",".join(map(str, municipios_ids))
            territorial = f"n6/{municipios_str}"# ← faltava isso

        elif estado_id:
            territorial = f"n6/in n3 {estado_id}"

        else:
            raise ValueError("Informe estado_id ou municipios_ids")
        
        url = (
            f"{PopulacaoConfig.POPULACAO_URL}/t/6579/"
            f"{territorial}/"
            f"p/{anos}/"
            f"?formato=json"
        )

        try:
            
            response = requests.get(url, timeout=PopulacaoConfig.TIMEOUT)
            response.raise_for_status()
            data = response.json()

        except requests.RequestException as e:
            raise RuntimeError(f"Erro na requisição de população: {e}")
            
        except ValueError:
            raise RuntimeError("Erro ao converter resposta para JSON")

        return PopulationExtractor.parse(data)

    @staticmethod
    def parse(data):
        """
        Converte a resposta da API SIDRA em uma estrutura padronizada de dados de população.

        A função extrai, para cada registro retornado pela API, o ID do município,
        nome do município, ano e população, tratando também valores especiais
        retornados pelo SIDRA (como "...", "X", etc.).

        Args:
            data (list[dict]): Lista de dicionários retornados pela API do SIDRA
                já no formato JSON (sem header, caso tenha sido removido com /h/n).
                Cada item representa um registro da tabela multidimensional.

        Returns:
            list[dict]: Lista de dicionários normalizados com os seguintes campos:
                - municipio_id (int): Código IBGE do município
                - municipio_nome (str): Nome do município
                - ano (int): Ano da observação
                - populacao (int | None): População estimada. Pode ser None caso o
                valor seja inválido, inexistente ou suprimido na API.
        """

        resultado = []

        for item in data:
            try:
                valor = item.get("V")

                if valor in ("...", "..", "X", "-"):
                    populacao = None
                else:
                    populacao = int(valor)

                resultado.append({
                    "municipio_id": int(item.get("D1C")),
                    "municipio_nome": item.get("D1N"),
                    "ano": int(item.get("D2N")),
                    "populacao": populacao
                })

            except (ValueError, TypeError) as e:
                print(f"Erro ao processar linha: {item} | erro: {e}")
                continue

        return resultado
