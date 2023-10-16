import pandas as pd
import matplotlib.pyplot as plt


# Read the data
df = pd.read_csv('whatcom_filtered_file.csv')

# Convert 'Sale Date' to datetime format
df['Sale Date'] = pd.to_datetime(df['Sale Date'])

# Convert the Sale Price to a float type if it's not already
df['Sale Price'] = df['Sale Price'].str.replace(',', '').str.replace('$', '').astype(float)

# Extract month from the 'Sale Date' and create a new 'Month' column
df['Month'] = df['Sale Date'].dt.strftime('%Y-%m')  # this format will represent data as 'YYYY-MM'


plt.figure(figsize=(15, 8))

# Create box plot
df.boxplot(column='Sale Price', by='Month', grid=True, vert=False, rot=45, patch_artist=True)

plt.title('Box Plot of Sale Prices by Month')
plt.suptitle('')  # This line removes the default title set by pandas' boxplot
plt.xlabel('Sale Price')
plt.ylabel('Month')
plt.tight_layout()

plt.savefig('sale_prices_boxplot.png', dpi=300)  # Save as a PNG file with a resolution of 300 dpi

plt.show()
