import requests
import csv

# Download the NAV data
url = "https://www.amfiindia.com/spages/NAVAll.txt"
response = requests.get(url)
lines = response.text.splitlines()

# Extract Scheme Name (col 4) and NAV (col 5)
data = []
for line in lines:
    parts = line.split("|")
    if len(parts) >= 5 and parts[3] != "Scheme Name" and parts[3].strip():
        data.append([parts[3].strip(), parts[4].strip()])

# Save as TSV
with open("nav_data.tsv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerows(data)

print(f"✅ Extracted {len(data)} records into nav_data.tsv")


# ----------------------------------------------------------------------
# TSV vs JSON — Which is better?
#
# TSV/CSV:
#   - Easy to use with Excel, Google Sheets, Pandas, SQL imports.
#   - Compact, human-readable.
#   - Best for tabular data like NAVs.
#
# JSON:
#   - Better if you’re going to use the data in APIs, web apps, or scripting.
#   - Preserves structure and allows richer metadata.
#   - Example:
#       [
#         { "scheme": "Axis Bluechip Fund - Direct Plan-Growth", "nav": "71.4253" },
#         { "scheme": "SBI Equity Hybrid Fund - Regular Plan-Growth", "nav": "289.4125" }
#       ]
#
# 👉 Recommendation:
#   - If analyzing in spreadsheets or databases → TSV is best.
#   - If building an API or integrating into an app → JSON is better.
# ----------------------------------------------------------------------
