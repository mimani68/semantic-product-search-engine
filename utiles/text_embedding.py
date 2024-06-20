import torch, os, clip, openai

openai.api_key = os.getenv("OPENAI_API_KEY")
TEXT_EMBEDDING_ENGINE = os.getenv("TEXT_EMBEDDING_ENGINE")

def get_text_embedding(text):
    if TEXT_EMBEDDING_ENGINE == 'openai':
        model_name = "text-embedding-ada-002"
        response = openai.Embedding.create(
            model= model_name,
            input = text
        )
        embedding_vector = response['data'][0]['embedding']
        return embedding_vector
    else:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        text = clip.tokenize([text]).to(device)
        return text
