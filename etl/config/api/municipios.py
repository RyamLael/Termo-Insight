class MunicipiosConfig():
    """
    Configurações da API do IBGE utilizada para consulta de municípios do Ceará
    """
    
    # Dados das cidades
    STATE_ID = 23 # Ceará
    MUNICIPIOS_URL = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{STATE_ID}/municipios"
