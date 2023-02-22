from typing import List
import pandas as pd
import data_loading


def data_cleaning(datas: List[pd.DataFrame]) -> List[pd.DataFrame]:
    """
    droping nan's from dataframe
    """
    datas[2]['Year'] = datas[2]['Year'].astype(str)
    for data in datas:
        data.dropna(inplace=True)
        data.reset_index(inplace=True, drop=True)
    datas[2] = datas[2][['Year', 'Country', 'Per Capita']]
    datas[2] = datas[2].pivot(index='Country', columns='Year', values='Per Capita').reset_index()

    for data in datas[:2]:
        data.rename(columns={'Country Name': 'Country'}, inplace=True)
        data.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis=1, inplace=True)
        data['Country'] = data['Country'].str.upper()

    datas = leave_only_common_years(datas)

    datas[2].dropna(inplace=True)

    return datas


def find_common_years(list_of_yeras_from_different_sources: List[List[str]]) -> List[str]:
    """
    return set of common yers from list of lists of yeras
    """
    common_years = set(list_of_yeras_from_different_sources[0])
    for yeras in list_of_yeras_from_different_sources[1:]:
        common_years.intersection_update(set(yeras))
    return sorted(list(common_years))


def leave_only_common_years(datas: List[pd.DataFrame]) -> List[pd.DataFrame]:
    gdp_dataframe, population_dataframe, co2_dataframe = datas

    common_years = find_common_years(
        [gdp_dataframe.columns[1:], population_dataframe.columns[1:], co2_dataframe.columns[1:]])

    gdp_dataframe = gdp_dataframe[list(gdp_dataframe.columns[:1]) + common_years]

    population_dataframe = population_dataframe[list(population_dataframe.columns[:1]) + common_years]

    co2_dataframe = co2_dataframe[list(co2_dataframe.columns[:1]) + common_years]

    return [gdp_dataframe, population_dataframe, co2_dataframe]


def data_merging(datas: List[pd.DataFrame]) -> List[pd.DataFrame]:
    gdp_dataframe, population_dataframe, co2_dataframe = datas
    common_years = gdp_dataframe.columns[1:]

    gdp_for_analysis = gdp_dataframe.merge(population_dataframe, on='Country', suffixes=('_gdp', '_population'))

    for year in common_years:
        gdp_for_analysis[year] = gdp_for_analysis[year + '_gdp'].div(gdp_for_analysis[year + '_population'])
        gdp_for_analysis.drop([year + '_gdp', year + '_population'], axis=1, inplace=True)

    return [gdp_for_analysis, co2_dataframe]

