import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


# Read the CSV data
df = pd.read_csv('whatcom_filtered_file.csv')

# Convert the Sale Price to a float type if it's not already
df['Sale Price'] = df['Sale Price'].str.replace(',', '').str.replace('$', '').astype(float)

# Convert DataFrame to GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))


fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the properties on the map
gdf.plot(ax=ax, markersize=20, column='Sale Price', cmap='YlOrRd', legend=True)

# Adjusting the plot
ax.set_title('Properties by Sale Price')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

plt.savefig('sale_prices_scatterplot.png', dpi=300)  # Save as a PNG file with a resolution of 300 dpi


plt.show()
