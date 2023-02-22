import argparse
import data_loading, data_transofrmation, data_analysis
parser = argparse.ArgumentParser()

parser.add_argument('--gdp', type=str, help='ścieżka do pliku 1')
parser.add_argument('--population', type=str, help='ścieżka do pliku 2')
parser.add_argument('--co2', type=str, help='ścieżka do pliku 3')

args = parser.parse_args()

data = data_loading.raw_data_import(args.gdp, args.population, args.co2)

data = data_transofrmation.data_cleaning(data)

data_for_analytics = data_transofrmation.data_merging(data)

print(data_analysis.most_co2_per_capita(data_for_analytics),
                                        data_analysis.most_gdp_per_capita(data_for_analytics),
                                        data_analysis.most_co2_decrease(data_for_analytics),
                                        data_analysis.most_co2_increase(data_for_analytics), sep='\n\n')