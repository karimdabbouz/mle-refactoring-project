from sklearn.pipeline import Pipeline
from data_cleaning import DropRowTransformer, SqftBasementTransformer, FillMissingViewWaterfrontTransformer, LastChangedTransformer
from feature_engineering import PricePerSqftTransformer, DistanceToCenterTransformer, DistanceToWaterfrontTransformer
import pandas as pd



class PreprocessingKingCountyHouseDataset():
    def __init__(self):
        self.data_cleaning_pipeline = Pipeline([
            ('drop_row', DropRowTransformer()),
            ('sqft_basement', SqftBasementTransformer()),
            ('missing_view_waterfront', FillMissingViewWaterfrontTransformer()),
            ('last_changed', LastChangedTransformer())
        ])
        self.feature_engineering_pipeline = Pipeline([
            ('price_per_sqft', PricePerSqftTransformer()),
            ('distance_to_center', DistanceToCenterTransformer()),
            ('distance_to_waterfront', DistanceToWaterfrontTransformer())
        ])
        self.preprocessor_pipeline = Pipeline([
            ('data_cleaning', self.data_cleaning_pipeline),
            ('feature_engineering', self.feature_engineering_pipeline)
        ])

    def preprocess_fit_transform(self, df):
        return self.preprocessor_pipeline.fit_transform(df)


train_df = pd.read_csv('../data/King_County_House_prices_dataset.csv')
print(train_df.head(2))
preprocessor = PreprocessingKingCountyHouseDataset()
train_df = preprocessor.preprocess_fit_transform(train_df)
print(train_df.head(2))