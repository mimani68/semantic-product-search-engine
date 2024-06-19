import openai, os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_text_embedding(text):
    model_name = "text-embedding-ada-002"
    response = openai.Embedding.create(
        model= model_name,
        input = text
    )
    embedding_vector = response['data'][0]['embedding']
    return embedding_vector
