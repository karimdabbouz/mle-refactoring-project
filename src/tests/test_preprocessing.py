import pytest, sys
import pandas as pd
from pydantic import BaseModel
sys.path.append('../')
from preprocessing import PreprocessingKingCountyHouseDataset


class DataSchema(BaseModel):
    id: int
    date: object
    price: float
    bedrooms: int
    sqft_living: int
    sqft_lot: int
    floors: float
    waterfront: float
    view: float
    condition: int
    grade: int
    sqft_above: int
    sqft_basement: float
    zipcode: int
    lat: float
    long: float
    sqft_living15: int
    sqft_lot15: int
    last_known_change: int
    sqft_price: float
    delta_lat: float
    delta_long: float
    center_distance: float
    water_distance: float


class TestPipeline():
    def __init__(self, data_schema):
        self.data_schema = data_schema

    def run_test(self):
        class DataframeValidation(BaseModel):
            df_as_dict: list[self.data_schema]
        train_df = pd.read_csv('../../data/King_County_House_prices_dataset.csv')
        preprocessor = PreprocessingKingCountyHouseDataset()
        train_df = preprocessor.preprocess_fit_transform(train_df)
        df_as_dict = train_df.to_dict(orient='records')
        DataframeValidation(df_as_dict=df_as_dict)