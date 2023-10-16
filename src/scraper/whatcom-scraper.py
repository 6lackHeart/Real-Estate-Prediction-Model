import requests
from bs4 import BeautifulSoup
import csv

# Base URL
base_url = "https://property.whatcomcounty.us/PropertyAccess/SearchResultsSales.aspx?cid=0&rtype=address&page={}"

# Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Referer": "https://property.whatcomcounty.us/PropertyAccess/SaleSearch.aspx?cid=0",
    "Sec-Ch-Ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
}

# Cookies expire you need to go get the current cookies from the page after the search request has been sent.
cookies = {
    "nmstat": "f5768d13-2a32-158c-cb50-b267bc257efb",
    "_gid": "GA1.2.907384452.1696993095",
    "_ga": "GA1.1.1293878984.1696993095",
    "_ga_MX1X8H9SNZ": "GS1.2.1697066754.2.1.1697066760.0.0.0",
    "ASP.NET_SessionId": "u15rmglqoacddflecunegihs",
    "_ga_DEX14T1BW4": "GS1.1.1697066754.2.1.1697066859.0.0.0",
    "_ga_9WMTWRB03D": "GS1.1.1697066754.2.1.1697066859.0.0.0"
}


# Open a CSV file for writing
with open('property_sales.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Address', 'City, State', 'Sale Date', 'Sale Price'])  # Writing headers

    # Looping through pages
    for page_number in range(1, 760):
        # Form the URL for the current page
        url = base_url.format(page_number)

        # Make the GET request
        response = requests.get(url, headers=headers, cookies=cookies)

        # Ensure the request was successful
        if response.status_code == 200:
            # Get the content
            html_content = response.text

            # Parse with BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')

            # Your data extraction logic
            data_rows = soup.select("td.ss-situs, td.ss-sale-date, td.ss-sale-price")

            # Assuming data comes in 3 rows for each property: Address, Sale Date, Sale Price
            for i in range(0, len(data_rows), 3):
                address_lines = data_rows[i].text.split("\n")
                address = address_lines[0]
                city_state = address_lines[1]
                sale_date = data_rows[i + 1].text
                sale_price = data_rows[i + 2].text

                # Writing to the CSV
                writer.writerow([address, city_state, sale_date, sale_price])

        else:
            print(f"Error on page {page_number}: Received status code {response.status_code}")

        # Optional: Add a delay between requests
        # time.sleep(1)
