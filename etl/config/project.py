import os

class ProjectConfig:
    # Localização da raiz do projeto
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    
    # Organização do Data Lake (Bronze Layer)
    BRONZE_RAW_DIR = os.path.join(BASE_DIR, "data", "bronze")
    
    # Subpastas para cada origem
    BRONZE_IBGE = os.path.join(BRONZE_RAW_DIR, "ibge")
    BRONZE_METEO = os.path.join(BRONZE_RAW_DIR, "open_meteo")
    
    # Cria pastas automaticamente
    @classmethod
    def setup_directories(cls):
        for path in [cls.BRONZE_IBGE, cls.BRONZE_METEO]:
            os.makedirs(path, exist_ok=True)

# Executa o setup das pastas
ProjectConfig.setup_directories()