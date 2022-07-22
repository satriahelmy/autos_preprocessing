import pandas as pd
import pickle # joblib

from helper.data_check_preparation import read_and_check_data
from helper.feature_engineering import feature_engineering
from helper.constant import COLUMN, PATH, DATETIME_COLUMN

def data_preprocessing():
    # pembacaan dan pengecekan data
    df = read_and_check_data(PATH, COLUMN, DATETIME_COLUMN)
    
    # feature engineering
    df_transformed = feature_engineering(df)
    
    print("Start Saving Result Feature Engineering!")
    df_transformed.to_csv("artifacts/df_transformed.csv")
    

if __name__ == "__main__":
    print("START RUNNING PIPELINE!")
    data_preprocessing()
    print("FINISH RUNNING PIPELINE!")