import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('whatcom_filtered_file.csv')

# Convert 'Sale Price' to a numeric format by removing dollar signs and commas
df['Sale Price'] = df['Sale Price'].str.replace(',', '').str.replace('$', '').astype(float)


# Convert 'Sale Date' to datetime format and sort
df['Sale Date'] = pd.to_datetime(df['Sale Date'])
df = df.sort_values(by='Sale Date')

# Calculate a 30-day rolling average
df['Rolling Average'] = df['Sale Price'].rolling(window=30).mean()

# Resample by month and get the average for each month
monthly_avg = df.resample('M', on='Sale Date')['Sale Price'].mean()

# Plotting
plt.figure(figsize=(15, 8))

# Plot the raw data in a light color
plt.plot(df['Sale Date'], df['Sale Price'], color='lightgray', label='Daily Sale Prices')

# Plot the rolling average
plt.plot(df['Sale Date'], df['Rolling Average'], color='blue', label='30-Day Rolling Average')

# Plot the monthly average
plt.plot(monthly_avg.index, monthly_avg.values, color='red', marker='o', label='Monthly Average')

plt.title('Sale Prices Over Time')
plt.xlabel('Sale Date')
plt.ylabel('Sale Price')
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.legend()  # Display the legend
# Save the figure before showing it
plt.savefig('sale_prices_timeseries.png', dpi=300)  # Save as a PNG file with a resolution of 300 dpi
plt.show()
