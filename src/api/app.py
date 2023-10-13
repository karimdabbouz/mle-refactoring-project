from fastapi import Depends, FastAPI, HTTPException
import models
import schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()


models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get('/')
def index():
    return {'hi': 'there!'}


@app.get('/read_houses')
def read_houses(db: Session = Depends(get_db)):
    houses = db.query(models.House).all()
    if not houses:
        raise HTTPException(status_code=404, detail='Houses not found')
    return houses


@app.post('/create-house')
def create_house(house: schemas.HouseModel, db: Session = Depends(get_db)):
    new_house = models.House(
        date=house.date,
        price=house.price,
        bedrooms=house.bedrooms,
        bathrooms=house.bathrooms,
        sqft_living=house.sqft_living,
        sqft_lot=house.sqft_lot,
        floors=house.floors,
        waterfront=house.waterfront,
        view=house.view,
        condition=house.condition,
        grade=house.grade,
        sqft_above=house.sqft_above,
        sqft_basement=house.sqft_basement,
        yr_built=house.yr_built,
        yr_renovated=house.yr_renovated,
        zipcode=house.zipcode,
        lat=house.lat,
        long=house.long,
        sqft_living15=house.sqft_living15,
        sqft_lot15=house.sqft_lot15
    )
    db.add(new_house)
    db.commit()
    db.refresh(new_house)
    return new_house


@app.post('/update-house')
def update_house(house_id: int,  house: schemas.HouseModel, db: Session = Depends(get_db)):
    existing_house = db.query(models.House).filter(models.House.id == house_id).first()
    if existing_house is None:
        raise HTTPException(status_code=404, detail='House not found')
    updated_house = models.House(
        date=house.date,
        price=house.price,
        bedrooms=house.bedrooms,
        bathrooms=house.bathrooms,
        sqft_living=house.sqft_living,
        sqft_lot=house.sqft_lot,
        floors=house.floors,
        waterfront=house.waterfront,
        view=house.view,
        condition=house.condition,
        grade=house.grade,
        sqft_above=house.sqft_above,
        sqft_basement=house.sqft_basement,
        yr_built=house.yr_built,
        yr_renovated=house.yr_renovated,
        zipcode=house.zipcode,
        lat=house.lat,
        long=house.long,
        sqft_living15=house.sqft_living15,
        sqft_lot15=house.sqft_lot15
    )
    db.add(updated_house)
    db.commit()
    db.refresh(updated_house)
    return updated_house


@app.post('/delete-house')
def delete_house(house_id: int, db: Session = Depends(get_db)):
    existing_house = db.query(models.House).filter(models.House.id == house_id).first()
    if existing_house is None:
        raise HTTPException(status_code=404, detail='House not found')
    db.delete(existing_house)
    db.commit()
    return {'message': 'House deleted'}