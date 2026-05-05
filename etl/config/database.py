import os

class DatabaseConfig:

    URL = os.getenv(
        "DATABASE_URL",
        "postgresql://admin:admin@localhost:5432/etl_db"
    )
    
    POOL_SIZE = int(os.getenv("DB_POOL_SIZE", 5))
    MAX_OVERFLOW = int(os.getenv("DB_MAX_OVERFLOW", 10))
    
    # Schemas (Organização do seu diagrama)
    SCHEMAS = {
        "bronze": "bronze",
        "silver": "silver",
        "gold": "gold"
    }
