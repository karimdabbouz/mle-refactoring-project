from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session


app = FastAPI()

# import database

# Add db Dependency

@app.get('/')
def index():
    return {'hi': 'there!'}


@app.get('/read_houses')
def read_houses():
    houses = db.query(models.Houses).all()
    if not houses:
        raise HTTPException(status_code=404, detail="Houses not found")
    return houses


@app.post('/create-house')
def create_house(
        date: datetime,
        price: float,
        bedrooms: int,
        bathrooms: int,
        sqft_lot: int,
        sqft_living: int,
        floors: float,
        waterfront: int,
        view: int
        # and so on...
    ):
    pass