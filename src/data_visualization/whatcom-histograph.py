import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV
df = pd.read_csv('whatcom_filtered_file.csv')

# Plotting the histogram
plt.figure(figsize=(10, 6))
plt.hist(df['Sale Price'], bins=30, edgecolor='black', alpha=0.7)
plt.title('Distribution of Sale Prices')
plt.xlabel('Sale Price')
plt.ylabel('Number of Properties')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

# Save the figure before showing it
plt.savefig('sale_prices_histogram.png', dpi=300)  # Save as a PNG file with a resolution of 300 dpi

# Now display the figure
plt.show()
