import os
from openai import OpenAI
import dotenv 

dotenv.load_dotenv(dotenv_path = )

OPENAI_API_KEY: str = os.environ["OPENAI_API_KEY"]

OPENAI_BASE_URL: str = os.getenv("OPENAI_BASE_URL", "HELLO")

print(OPENAI_API_KEY)
print(OPENAI_BASE_URL)
print(os.environ)


def get_client() -> OpenAI:
    settings: OpenAISettings = OpenAISettings()