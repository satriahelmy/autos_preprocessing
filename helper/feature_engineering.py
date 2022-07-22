import pandas as pd
import numpy as np
from helper.preprocessing import CategoricalFeatures, standard_scaler

def feature_engineering(df):
    #cleansing column odometer and convert into int64
    df['odometer'] = df['odometer'].str.replace("km","")
    df['odometer'] = df['odometer'].str.replace(",","")
    df['odometer'] = df['odometer'].astype(np.int64)
    
    #cleansing column price and convert into int64
    df['price'] = df['price'].str.replace('$','', regex=True)
    df['price'] = df['price'].str.replace(',','')
    df['price'] = df['price'].astype(np.int64)
    
    #drop column yang perbandingan data unik terlalu besar
    df = df.drop(['offer_type', 'seller'], axis=1)
    
    #drop column yang tidak berisi informasi apapun
    df = df.drop(['num_of_pictures'], axis=1)
    
    #drop column yang informasinya unik disetiap baris datanya dan kolom yang memiliki banyak kategori namun tidak balance
    df = df.drop(['name','postal_code'], axis=1)
    
    #hapus outliers yang memiliki nilai price sehingga hanya yang memiliki nilai 500 s.d 40000
    df = df[(df['price']>=500) & (df['price']<=40000)]
        
    #imputasi nilai NaN dengan mode pada kolom bertipe object
    kolom_object = [col for col in df.columns if df[col].dtype=='object']
    for kolom in kolom_object:
        df[kolom] = df[kolom].fillna(df[kolom].mode()[0])
    
    #imputasi nilai NaN dengan median pada kolom bertipe numeric
    kolom_num = [col for col in df.columns if (df[col].dtype=='int64' or df[col].dtype=='float')]
    for kolom in kolom_num:
        df[kolom] = df[kolom].fillna(df[kolom].median())
    
    #normalization
    kolom_normalize = [col for col in df.columns if (df[col].dtype=='int64' and col != 'price')]
    scaler, df_normalized = standard_scaler(df[kolom_normalize])
    for kolom in kolom_normalize:
        df[kolom] = df_normalized[kolom]
    
    #encoding
    kolom_encoding = [col for col in df.columns if df[col].dtype=='object']
    cat_feats = CategoricalFeatures(df, categorical_features=kolom_encoding, encoding_type="label", handle_na=True)
    df = cat_feats.fit_transform()
    
    return df