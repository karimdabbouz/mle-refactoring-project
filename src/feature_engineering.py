import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin



class PricePerSqftTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X['sqft_price'] = (X.price / (X.sqft_living + X.sqft_lot)).round(2)
        return X


class DistanceToCenterTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X['delta_lat'] = np.absolute(47.62774 - X['lat'])
        X['delta_long'] = np.absolute(-122.24194 - X['long'])
        X['center_distance']= ((X['delta_long'] * np.cos(np.radians(47.6219)))**2 + X['delta_lat']**2)**(1/2)*2*np.pi*6378/360
        return X


class DistanceToWaterfrontTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def dist(self, long, lat, ref_long, ref_lat):
        ''' Helper function: dist computes the distance in km to a reference location. Input: long and lat of 
        the location of interest and ref_long and ref_lat as the long and lat of the reference location '''
        delta_long = long - ref_long
        delta_lat = lat - ref_lat
        delta_long_corr = delta_long * np.cos(np.radians(ref_lat))
        return ((delta_long_corr)**2 +(delta_lat)**2)**(1/2)*2*np.pi*6378/360
    
    def transform(self, X, y=None):
        water_list = X.query('waterfront == 1')
        water_distance = []
        for idx, lat in X.lat.items():
            ref_list = []
            for x, y in zip(list(water_list.long), list(water_list.lat)):
                ref_list.append(self.dist(X.long[idx], X.lat[idx],x,y).min())
            water_distance.append(min(ref_list))
        X['water_distance'] = water_distance
        return X
