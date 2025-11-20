from pydantic import BaseSettings
from pydantic import Field

class OpenAISettings(BaseSettings):
    
    open_ai_api_key: SecretStr = Field()
    
    