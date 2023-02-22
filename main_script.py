import argparse

import data_analysis
import data_loading
import data_transofrmation

parser = argparse.ArgumentParser()

parser.add_argument('--gdp', type=str, help='path to file with gdp data')
parser.add_argument('--population', type=str, help='path to file with population data')
parser.add_argument('--co2', type=str, help='path to file with co2 data')
parser.add_argument('--start', type=int, help='path to file with co2 data')
parser.add_argument('--koniec', type=int, help='path to file with co2 data')

args = parser.parse_args()

if args.start is not None and args.koniec is not None:
    years = [str(x) for x in range(args.start, args.koniec + 1)]
else:
    years = None


data = data_loading.raw_data_import(args.gdp, args.population, args.co2)
try:
    data = data_transofrmation.data_cleaning(data, years)
except Exception as e:
    print(e, "Check if you provided correct paths to files or look into your start and koniec.")
    raise e


data_for_analytics = data_transofrmation.data_merging(data)

print(data_analysis.most_co2_per_capita(data_for_analytics),
      data_analysis.most_gdp_per_capita(data_for_analytics),
      data_analysis.most_co2_decrease(data_for_analytics),
      data_analysis.most_co2_increase(data_for_analytics), sep='\n\n')
