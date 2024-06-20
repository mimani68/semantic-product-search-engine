from typing import List
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float

# Mock products data
products = [
    Product(id=1, name="Product A", description="An awesome product A", price=25.50),
    Product(id=2, name="Product B", description="A fantastic product B", price=45.00),
    Product(id=3, name="Product C", description="A superb product C", price=75.75),
]

def simple_search(query_string: str) -> List[Product]:
    # Perform a simple search based on the query string
    return [p for p in products if query_string.lower() in p.name.lower()]

def advanced_search() -> List[Product]:
    # Perform an advanced search (Mock implementation)
    return products
