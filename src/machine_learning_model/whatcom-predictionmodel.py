import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load the dataset
file_path = "whatcom_filtered_file.csv"
df = pd.read_csv(file_path)

# Convert 'Sale Date' to datetime format
df['Sale Date'] = pd.to_datetime(df['Sale Date'])
df['Sale Price'] = df['Sale Price'].str.replace('$', '').str.replace(',', '').astype(float)

# Extracting year and month from the date for the model
df['year'] = df['Sale Date'].dt.year
df['month'] = df['Sale Date'].dt.month

# Features and Target
X = df[['Longitude', 'Latitude', 'year', 'month']]
y = df['Sale Price']

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions on the test set
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")

# Predict for a new property
new_data = pd.DataFrame({
    'Longitude': [],  # replace with the Longitude of the new property
    'Latitude': [],  # replace with the Latitude of the new property
    'year': [],  # replace with the year of interest
    'month': []  # replace with the month of interest
})

predicted_price = model.predict(new_data)
print(f"Predicted Price for the new property: ${predicted_price[0]:,.2f}")
