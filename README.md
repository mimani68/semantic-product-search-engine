## Semantic product searching


### Install dependencies

```bash
pip install git+https://github.com/openai/CLIP.git
```

### Development

```bash
uvicorn main:app --reload
```

### Testing

```bash
curl -X POST http://127.0.0.1:8000/api/search/semantic \
   -H 'Content-Type: application/json' \
   -d '{"query_string": "car", "search_method": "hybrid"}'
```

