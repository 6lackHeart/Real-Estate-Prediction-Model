import pandas as pd

# Load your CSV file into a pandas DataFrame
df = pd.read_csv('GCed_property_sales2.csv')

# Filter out rows where either 'latitude' or 'longitude' is missing
df_filtered = df.dropna(subset=['Latitude', 'Longitude'])

# Save the filtered DataFrame back to a CSV file
df_filtered.to_csv('whatcom_filtered_file.csv', index=False)
