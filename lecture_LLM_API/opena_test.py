from openai import OpenAI
from multiprocessing import Lock
from dotenv import load_dotenv, find_dotenv
import numpy as ap



load_dotenv(dotenv_path=find_dotenv())

def get_embeddings(texts: list[str]) -> list[np.array]:
    client: OpenAI = OpenAI()
    
    embeddings: CreateEmbeddingResponse = client.embeddings.create(
        model = "Qwen/Qwen3-Embedding-0.6B", inputs=texts
    )

    return embeddings 
    
    
if __name__ == "__main__":
    embeddings: list[np.array] = get_embeddings(texts=["мужчина"])
    print(embeddings)
    print(len(embeddings.data[0].embedding))
    
    