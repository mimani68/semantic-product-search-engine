import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from service.search import hybrid_search_service, semantic_image_search_service, text_search_service

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class SearchRequest(BaseModel):
    query_string: str
    search_method: str

@app.post("/api/search/semantic")
async def semantic_search(search_request: SearchRequest):
    try:
        result = []
        
        if search_request.search_method == "image":
            result = semantic_image_search_service(search_request.query_string, 10)
        elif search_request.search_method == "text":
            result = text_search_service(search_request.query_string, 10)
        elif search_request.search_method == "hybrid":
            result = hybrid_search_service(search_request.query_string, 10)
        else:
            result = text_search_service(search_request.query_string)

        return {
            'success': True,
            'data': [ item.to_dict() for item in result['matches'] ]
            }
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail="Error happened.")
    except:
        print("An exception occurred")
        raise HTTPException(status_code=400, detail="Unsupported search method.")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=os.getenv('PORT'))
