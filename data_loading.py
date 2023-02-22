import pandas as pd
from typing import List


def raw_data_import(path_to_gdp: str, path_to_population: str, path_to_co2: str) -> List[pd.DataFrame]:
    """
    This function get path to data files and return list of three data frames - one for every data source.
    In this function there is no data transformation.
    """
    # loading data
    gdp_dataframe = pd.read_csv(filepath_or_buffer=path_to_gdp, sep=",", skiprows=4, header=0)
    population_dataframe = pd.read_csv(filepath_or_buffer=path_to_population, sep=",", skiprows=4, header=0)
    co2_dataframe = pd.read_csv(filepath_or_buffer=path_to_co2, sep=",", header=0)

    # because there is separator at the end of every line pandas created extra empty column
    for data in [gdp_dataframe, population_dataframe, co2_dataframe]:
        for name in data.columns:
            if "Unanmed" in name:
                name_to_delete = name
        data.drop(labels=name, axis=1, inplace=True)

    return [gdp_dataframe, population_dataframe, co2_dataframe]

