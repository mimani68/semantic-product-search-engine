uvicorn main:app --reload


curl -X POST http://127.0.0.1:8000/api/search/semantic \
   -H 'Content-Type: application/json' \
   -d '{"query_string": "Product", "search_method": "simple"}'
