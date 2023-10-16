import csv
import requests
import time

# Your Google Cloud API Key
API_KEY = ''

# URLs
GEOCODING_ENDPOINT = 'https://maps.googleapis.com/maps/api/geocode/json'


def geocode_address(address, max_retries=3, delay_between_retries=3600):
    """Return the lat, lon of an address using Google Geocoding API."""
    params = {'address': address, 'key': API_KEY}

    time.sleep(2)  # Delay of 2 seconds before each request

    for attempt in range(max_retries):
        try:
            response = requests.get(GEOCODING_ENDPOINT, params=params, timeout=10)  # 10 seconds timeout
            data = response.json()

            if data['status'] == 'OK':
                lat = data['results'][0]['geometry']['location']['lat']
                lon = data['results'][0]['geometry']['location']['lng']
                return lat, lon
            else:
                print(f"Error geocoding {address}: {data['status']}")
                return None, None
        except requests.RequestException as e:
            print(f"Network error on attempt {attempt + 1} for address: {address}. Error: {e}")
            if attempt < max_retries - 1:  # Only sleep if not the last attempt
                time.sleep(delay_between_retries)
        except Exception as e:
            print(f"Unexpected error on attempt {attempt + 1} for address: {address}. Error: {e}")
            return None, None

    print(f"Failed to geocode address after {max_retries} attempts: {address}")
    return None, None



# Read the CSV, geocode each address and write the result to a new CSV
with open('property_sales2.csv', 'r') as csv_input:
    with open('GCed_property_sales.csv', 'w', newline='') as csv_output:
        reader = csv.DictReader(csv_input)
        fieldnames = reader.fieldnames + ['Latitude', 'Longitude']
        writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            address = row['Address']
            lat, lon = geocode_address(address)
            row['Latitude'] = lat
            row['Longitude'] = lon
            writer.writerow(row)
