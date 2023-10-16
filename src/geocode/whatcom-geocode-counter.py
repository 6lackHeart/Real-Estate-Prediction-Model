import csv

# Path to your CSV file
csv_path = 'GCed_property_sales.csv'

# Counters
geocoded_count = 0
not_geocoded_count = 0

with open(csv_path, 'r') as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        # Assuming that if latitude is missing, longitude will also be missing
        if row['Latitude'] and row['Longitude']:
            geocoded_count += 1
        else:
            not_geocoded_count += 1

print(f"Entries with geocodes: {geocoded_count}")
print(f"Entries without geocodes: {not_geocoded_count}")
