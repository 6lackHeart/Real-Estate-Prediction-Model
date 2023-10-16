import pandas as pd
import matplotlib.pyplot as plt


# Read the data
df = pd.read_csv('whatcom_filtered_file.csv')

# Convert 'Sale Date' to datetime format
df['Sale Date'] = pd.to_datetime(df['Sale Date'])

# Convert the Sale Price to a float type if it's not already
df['Sale Price'] = df['Sale Price'].str.replace(',', '').str.replace('$', '').astype(float)

# Extract month from the 'Sale Date' and create a new 'Month' column
df['Month'] = df['Sale Date'].dt.strftime('%Y-%m')  # format represents data as 'YYYY-MM'


# Calculate average sale prices by month
average_prices = df.groupby('Month')['Sale Price'].mean()

plt.figure(figsize=(15, 8))

# Create the bar chart
average_prices.plot(kind='bar', color='skyblue')

plt.title('Average Sale Prices by Month')
plt.xlabel('Month')
plt.ylabel('Average Sale Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sale_prices_barchart.png', dpi=300)  # Save as a PNG file with a resolution of 300 dpi
plt.show()
