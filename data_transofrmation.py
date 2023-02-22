from typing import List, Set
import pandas as pd
import data_loading


def data_cleaning(data: pd.DataFrame):
    """
    droping nan's from dataframe
    """
    data.dropna(inplace=True)
    data.reset_index(inplace=True, drop=True)


def find_common_years(list_of_yeras_from_different_sources: List[List[str]]) -> List[str]:
    """
    return set of common yers from list of lists of yeras
    """
    common_years = set(list_of_yeras_from_different_sources[0])
    for yeras in list_of_yeras_from_different_sources[1:]:
        common_years.intersection_update(set(yeras))
    return sorted(list(common_years))


def leave_only_common_years(gdp_dataframe: pd.DataFrame, population_dataframe: pd.DataFrame,
                            co2_dataframe: pd.DataFrame):
    common_years = find_common_years(
        [gdp_dataframe.columns[4:], population_dataframe.columns[4:], [str(x) for x in co2_dataframe['Year']]])
    common_years = common_years
    gdp_dataframe = gdp_dataframe.filter(items=list(gdp_dataframe.columns[:4]) + common_years, axis=1)
    population_dataframe = population_dataframe.filter(items=list(gdp_dataframe.columns[:4]) + common_years, axis=1)

    common_years = [int(x) for x in common_years]

    co2_dataframe = co2_dataframe.loc[co2_dataframe['Year'].isin(common_years)]
    co2_dataframe = co2_dataframe.pivot(index='Country', columns='Year',
                        values=['Total', 'Solid Fuel', 'Liquid Fuel', 'Gas Fuel', 'Cement', 'Gas Flaring',
                                'Per Capita'])





pd.set_option('display.max_columns', None)  # ustawia wyświetlanie wszystkich kolumn
pd.set_option('display.max_rows', None)
datas = data_loading.raw_data_import(
    'C:\\Users\\ChecDoNauki\\Documents\\uw_matma\\sem5\\npd\\projekt_zaliczeniowy\\API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562\\API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv',
    'C:\\Users\\ChecDoNauki\\Documents\\uw_matma\\sem5\\npd\\projekt_zaliczeniowy\\API_SP.POP.TOTL_DS2_en_csv_v2_4751604\\API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv',
    'C:\\Users\\ChecDoNauki\\Documents\\uw_matma\\sem5\\npd\\projekt_zaliczeniowy\\co2-fossil-by-nation_zip\\data\\fossil-fuel-co2-emissions-by-nation_csv.csv')
for data in datas:
    data_cleaning(data)
leave_only_common_years(datas[0], datas[1], datas[2])
