#Configuración centralizada de la aplicación usando variables de entorno.

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    #Configuración de la aplicación cargada desde variables de entorno.

    app_name: str = "Task API"
    database_url: str = "sqlite:///./tasks.db"
    debug: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()