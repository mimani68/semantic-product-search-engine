import json, os

from utiles.query_for_images import semantic_images_query

def semantic_image_search_service(query_text: str):
    if not query_text:
        return {
            "message": "Query is not defined."
        }
    
    # load database embedded result
    with open("./database/image_db.json", "r") as f:
        image_features_loaded = json.loads(f.read())

    # define score of ranking
    result = semantic_images_query(query_text, image_features_loaded, 2)

    return {
        "result": result
    }

def text_search_service(query_text: str):
    if not query_text:
        return {
            "message": "Query is not defined."
        }

    #  Using pinacone

    return {
        "result": []
    }

def hybrid_search_service(query_text: str):
    if not query_text:
        return {
            "message": "Query is not defined."
        }

    #  Using pinacone

    return {
        "result": []
    }