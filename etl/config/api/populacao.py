
class PopulacaoConfig():
    """
    Configurações da API do IBGE para Consulta de população via SIDRA (Tabela 6579)
    """
    
    # Dados da população
    # API SIDRA (Tabela 6579 - Estimativa de População)
    # v/93 = Variável População Residente
    # n6/in n3 23 = Todos os municípios (n6) dentro do estado 23 (n3)
    POPULACAO_URL = "https://apisidra.ibge.gov.br/values/t/6579/n6/in%20n3%2023/v/93/p/all"
