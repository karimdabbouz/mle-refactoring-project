import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin



class DropRowTransformer(BaseEstimator, TransformerMixin):
    ''' Data in this row is obviously wrong '''
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X.drop(15856, axis=0, inplace=True)
        return X


class SqftBasementTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X['sqft_basement'] = X['sqft_basement'].replace('?', np.nan)
        X['sqft_basement'] = X['sqft_basement'].astype(float)
        X.eval('sqft_basement = sqft_living - sqft_above', inplace=True)
        return X


class FillMissingViewWaterfrontTransformer():
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X['view'] = X['view'].fillna(0)
        X['waterfront'] = X['waterfront'].fillna(0)
        return X


class LastChangedTransformer():
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        last_known_change = []
        for idx, yr_re in X.yr_renovated.items():
            if str(yr_re) == 'nan' or yr_re == 0.0:
                last_known_change.append(X.yr_built[idx])
            else:
                last_known_change.append(int(yr_re))
        X['last_known_change'] = last_known_change
        X.drop('yr_renovated', axis=1, inplace=True)
        X.drop('yr_built', axis=1, inplace=True)
        return X