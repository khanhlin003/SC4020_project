import os
import pandas as pd
from zipfile import ZipFile
from preprocess import preprocess_mobility_data

# Define paths to data files
data_folder = "data"
cityA_data_path = os.path.join(data_folder, "cityA_groundtruthdata.csv.gz")
cityB_data_path = os.path.join(data_folder, "cityB_challengedata.csv.gz")
cityC_data_path = os.path.join(data_folder, "cityC_challengedata.csv.gz")
cityD_data_path = os.path.join(data_folder, "cityD_challengedata.csv.gz")

# Function to load and unzip data if necessary
def load_data(file_path):
    if file_path.endswith('.gz'):
        # Read gzipped CSV file
        return pd.read_csv(file_path, compression='gzip')
    else:
        return pd.read_csv(file_path)

# Load data for each city
cityA_data = load_data(cityA_data_path)
cityB_data = load_data(cityB_data_path)
cityC_data = load_data(cityC_data_path)
cityD_data = load_data(cityD_data_path)

# Preprocess each city's data
print("Preprocessing data for City A...")
triplegs_cityA = preprocess_mobility_data(cityA_data)

print("Preprocessing data for City B...")
triplegs_cityB = preprocess_mobility_data(cityB_data)

print("Preprocessing data for City C...")
triplegs_cityC = preprocess_mobility_data(cityC_data)

print("Preprocessing data for City D...")
triplegs_cityD = preprocess_mobility_data(cityD_data)

# Further analysis like sequential pattern mining can be done here
