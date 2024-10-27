import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import trackintel as ti

def preprocess_mobility_data(city_data):
    """
    Preprocess mobility data for a city: clean, convert to GeoDataFrame, and generate triplegs.
    
    Args:
    city_data (pd.DataFrame): The mobility data for a city.
    
    Returns:
    triplegs (GeoDataFrame): The generated triplegs after processing.
    """
    # Remove rows with missing data (-999 values)
    city_data_clean = city_data[~((city_data['x'] == -999) & (city_data['y'] == -999))]
    
    # Convert DataFrame to GeoDataFrame for trackintel
    city_data_clean['geometry'] = city_data_clean.apply(lambda row: Point(row['x'], row['y']), axis=1)
    gdf = gpd.GeoDataFrame(city_data_clean, geometry='geometry')
    
    # Set required columns for trackintel positionfixes
    gdf['tracked_at'] = pd.to_datetime(gdf['d'] + ' ' + gdf['t'])  # Combine date and time into a datetime column
    gdf['user_id'] = gdf['uid']
    
    # Generate triplegs from positionfixes
    positionfixes = ti.io.from_geopandas(gdf, trackintel_type='positionfixes')
    triplegs = positionfixes.as_triplegs()
    
    return triplegs
