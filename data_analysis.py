from typing import List

import pandas as pd
import data_loading, data_transofrmation

def

def most_co2_per_capita(datas: List[pd.DataFrame]) -> pd.DataFrame:
    _, co2_dataframe = datas
    #merged_data = population_dataframe.merge(co2_dataframe, left_on='Country Name', right_on='Country')
    #print(merged_data.iloc[:3,:])


pd.set_option('display.max_columns', None)  # ustawia wyświetlanie wszystkich kolumn
pd.set_option('display.max_rows', None)
datas = data_loading.raw_data_import(
    'C:\\Users\\ChecDoNauki\\Documents\\uw_matma\\sem5\\npd\\projekt_zaliczeniowy\\API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562\\API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv',
    'C:\\Users\\ChecDoNauki\\Documents\\uw_matma\\sem5\\npd\\projekt_zaliczeniowy\\API_SP.POP.TOTL_DS2_en_csv_v2_4751604\\API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv',
    'C:\\Users\\ChecDoNauki\\Documents\\uw_matma\\sem5\\npd\\projekt_zaliczeniowy\\co2-fossil-by-nation_zip\\data\\fossil-fuel-co2-emissions-by-nation_csv.csv')

datas = data_transofrmation.data_cleaning(datas)
datas_for_analysis = data_transofrmation.data_merging(datas)

