from typing import List
import pandas as pd


def most_co2_per_capita(datas: List[pd.DataFrame]) -> pd.DataFrame:
    """
    return dataframe of top 5 co2 producers per capita for every year
    """
    _, co2_dataframe = datas
    top_5_by_year = dict()
    for year in co2_dataframe.columns[1:]:
        top_5_by_year[year] = co2_dataframe.nlargest(5, year).reset_index(drop=True)['Country']
    return pd.DataFrame(top_5_by_year)


def most_gdp_per_capita(datas: List[pd.DataFrame]) -> pd.DataFrame:
    """
    return dataframe of top 5 gdp per capita for every year
    """
    gdp_dataframe, _ = datas
    top_5_by_year = dict()
    for year in gdp_dataframe.columns[1:]:
        top_5_by_year[year] = gdp_dataframe.nlargest(5, year).reset_index(drop=True)['Country']
    return pd.DataFrame(top_5_by_year)


def most_co2_increase(datas: List[pd.DataFrame]) -> pd.DataFrame:
    """
    return dataframe of top 5 increase of co2 per capita between 2004 and 2014
    """
    _, co2_dataframe = datas

    co2_dataframe['Increase'] = co2_dataframe['2014'].subtract(co2_dataframe['2004'])
    return co2_dataframe.nlargest(5, 'Increase').reset_index(drop=True)[['Country']]


def most_co2_decrease(datas: List[pd.DataFrame]) -> pd.DataFrame:
    """
    return dataframe of top 5 decrease of co2 per capita between 2004 and 2014
    """
    _, co2_dataframe = datas

    co2_dataframe['Increase'] = co2_dataframe['2014'].subtract(co2_dataframe['2004'])
    return co2_dataframe.nsmallest(5, 'Increase').reset_index(drop=True)[['Country']]
