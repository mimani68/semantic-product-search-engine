import os
from fastapi import FastAPI, HTTPException
from service.search import SearchRequest, simple_search, advanced_search

app = FastAPI()

@app.post("/api/search/semantic")
async def semantic_search(search_request: SearchRequest):
    if search_request.search_method == "simple":
        # Using the simple search function from the service layer
        return {"products": simple_search(search_request.query_string)}
    elif search_request.search_method == "advanced":
        # Using the advanced search function from the service layer
        return {"products": advanced_search()}
    else:
        raise HTTPException(status_code=400, detail="Unsupported search method")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=os.getenv('PORT'))
