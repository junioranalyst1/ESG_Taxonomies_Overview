import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Load data from CSV
csv_file_path = '/Users/nicolashock/Documents/GitHub/ESG_Taxonomies_Overview/Book1.csv'
df = pd.read_csv(csv_file_path)

# Convert DataFrame to GeoDataFrame
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry)

# Define the CRS (Coordinate Reference System) for your data
# For example, for WGS 84 (EPSG: 4326):
gdf.crs = "EPSG:4326"

# Save to GeoJSON file
geojson_file_path = '/Users/nicolashock/Documents/GitHub/ESG_Taxonomies_Overview/map_features.geojson'
gdf.to_file(geojson_file_path, driver='GeoJSON')
