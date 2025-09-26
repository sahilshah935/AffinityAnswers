import requests
from bs4 import BeautifulSoup
import csv

# Target URL for OLX search
URL = "https://www.olx.in/items/q-car-cover"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)

if response.status_code != 200:
    print("Failed to fetch page, status code:", response.status_code)
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# Extract listing data
results = []
for item in soup.find_all("li", {"data-aut-id": "itemBox"}):
    title = item.find("span")
    price = item.find("span", {"data-aut-id": "itemPrice"})
    location = item.find("span", {"data-aut-id": "item-location"})
    link_tag = item.find("a", href=True)

    results.append({
        "title": title.text.strip() if title else "N/A",
        "price": price.text.strip() if price else "N/A",
        "location": location.text.strip() if location else "N/A",
        "link": "https://www.olx.in" + link_tag["href"] if link_tag else "N/A"
    })

# Save to CSV
with open("olx_car_cover_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price", "location", "link"])
    writer.writeheader()
    writer.writerows(results)

print(f"✅ Scraped {len(results)} results and saved to olx_car_cover_results.csv")
