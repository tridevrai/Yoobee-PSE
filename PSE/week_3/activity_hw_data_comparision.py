# Activity W4-1:
# Load data for Auckland and Christchurch and 
# compare the temperature between two cities in a year monthly basis -  
# See Link: https://data.niwa.co.nz/pages/clidb-on-datahub

import pandas as pd



class CsvLoader:
    def __init__(self):
        self.csv_data = {}

    def load_csv(self, file_path, city_name):
        data_frame = pd.read_csv(file_path)
        # renaming the column name to be the city name to later after merging to perform the comparison
        renamed_column_name = build_data_column_name(city_name=city_name)
        data_frame.rename(columns={'STATS_VALUE': renamed_column_name}, inplace=True)
        self.csv_data[renamed_column_name] = data_frame

    def get_all_csv(self):
        return self.csv_data


class DataComparer:
    
    def __init__(self, csv_data_map):
        self.csv_data_map = csv_data_map

    def compare_data(self):
        if len(self.csv_data_map) != 2:
            print(f"Only two dataframes can be compared now. You provided {len(self.csv_data_map)}.")
            return None
        
        # Extract column names and corresponding dataframes
        columns = list(self.csv_data_map.keys())  # e.g., ['Temp_City1', 'Temp_City2']
        df1 = self.csv_data_map[columns[0]]
        df2 = self.csv_data_map[columns[1]]

        # Merge on PERIOD and YEAR
        merged = pd.merge(df1, df2, on=['PERIOD', 'YEAR'], how='inner')

        # Calculate temperature difference and store in merged dataframe
        merged['Temp_Diff'] = merged[columns[0]] - merged[columns[1]]

        return merged 




def build_data_column_name(city_name):
    return city_name.replace(' ', '_') + 'STATS_VALUE'


def main():
    # Load data for Auckland 
    
    auckland_file_path = './week_3/auckland_1962__monthly__Mean_air_temperature__Deg_C.csv'

    # Load data for Christchurch

    christchurch_file_path = './week_3/christchurch_4843__monthly__Mean_air_temperature__Deg_C.csv'

    loader = CsvLoader()
    loader.load_csv(auckland_file_path, 'Auckland')
    loader.load_csv(christchurch_file_path, 'Christchurch')

    csv_data_map = loader.get_all_csv()
    comparer = DataComparer(csv_data_map)
    comparison_result = comparer.compare_data()

    if comparison_result is not None:
        print(comparison_result)


if __name__ == "__main__":
    main()
