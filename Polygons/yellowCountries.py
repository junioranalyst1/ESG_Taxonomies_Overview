import geopandas as gpd

# Replace 'path/to/shapefile_folder' with the actual path to the folder containing the shapefile files.
shapefile_path = '/Users/nicolashock/Documents/GitHub/green_finance_taxonomies/Polygons/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'

# Load the shapefile into a GeoDataFrame
gdf_countries = gpd.read_file(shapefile_path)

# Replace 'Country 1', 'Country 2', etc., with the names of the countries you want to extract.
countries_to_extract = ['Canada', 'Mexico', 'Dominican Republic', 'Peru', 'Brazil', 'Chile', 'United Kingdom', 'South Africa', 'India', 'Bangladesh', 'Sri Lanka', 'New Zealand', 'Russia', 'Kazakhstan', 'Thailand', 'South Korea', 'Vietnam', 'Philippines', 'Singapore', 'Indonesia']

# Filter the GeoDataFrame to keep only the specified countries
filtered_gdf = gdf_countries[gdf_countries['ADMIN'].isin(countries_to_extract)]

# Print information about the filtered countries (optional)
print(filtered_gdf[['ADMIN', 'geometry']])

# Save the filtered GeoDataFrame to a new shapefile named 'greenCountries'
output_shapefile = '/Users/nicolashock/Documents/GitHub/green_finance_taxonomies/Polygons/yellowCountries_Output'  # Replace '/path/to/output_folder/' with the actual path to the output folder.
filtered_gdf.to_file(output_shapefile, driver='ESRI Shapefile')

# You can also save the filtered GeoDataFrame as a GeoJSON file if you prefer
# output_geojson = '/path/to/output_folder/greenCountries.geojson'
# filtered_gdf.to_file(output_geojson, driver='GeoJSON')