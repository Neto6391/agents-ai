from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # API Configuration
    youtube_api_key: Optional[str] = None
    search_api_key: Optional[str] = None
    search_engine_id: Optional[str] = None

    # Model Configuration
    onnx_model_path: str = "./models/model.onnx"
    tokenizer_name: str = "organization/model"
    max_context_length: int = 512
    max_generation_tokens: int = 150

    # Performance Configuration
    cache_size: int = 1000
    request_timeout: int = 30
    max_concurrent_requests: int = 10

    # Intent Detection
    intent_confidence_threshold: float = 0.3

    class Config:
        env_file = ".env"

# instância global de configurações
settings = Settings()