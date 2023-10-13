from pydantic import BaseModel
from datetime import datetime


class HouseModel(BaseModel):
    id: int
    date: datetime
    price: float
    bedrooms: int
    bathrooms: float
    sqft_living: int
    sqft_lot: int
    floors: float
    waterfront: float
    view: float
    condition: int
    grade: int
    sqft_above: int
    sqft_basement: float
    yr_built: int
    yr_renovated: float
    zipcode: int
    lat: float
    long: float
    sqft_living15: int
    sqft_lot15: int

    class Config:
        orm_mode = True