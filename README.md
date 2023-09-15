# Refactoring Project

## What are the steps you took to complete the project?

1. Read and understand the notebook
2. Make a copy of the original notebook
3. Refactored all steps for data cleaning and feature engineering into functions inside of the notebook
4. Created three python files: `preprocessing.py`, `data_cleaning.py`, `feature_engineering.py`
5. Put all data cleaning steps into `data_cleaning.py` and all feature engineering steps into `feature_engineering.py`.
6. Refactored the functions into Sklearn transformers and consolidated them in a class `PreprocessingKingCountyHouseDataset` in `feature_engineering.py`
7. Added a test using pydantic under `/tests/test_preprocessing.py` which runs the pipeline (csv file hard-coded) and validates the number of columns and their types (not using pytest for this one)

## What are the challenges you faced?

I find it hard to anticipate when it makes sense to use classes instead of functions and when to use Sklearn transformers. Also I often don't know how granular and/or general functions should become. For instance, I now have a custom transformer just to drop a specific row in the dataframe which probably doesn't make much sense. It would make sense to have a utility that could drop rows according to specific criteria.

## What are the things you would do differently if you had more time?

Extend the preproessing test so that it uses pytest in conjunction with pydantic: Implement a second test that checks if the columns are all non-empty. If they both pass, then pytest validates to True.