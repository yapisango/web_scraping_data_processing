# Step 3.1: Fetch HTML Content
# Please be careful to follow instructions on how to run the program; 
# the Run menu or right-click > Run options do not work in the simulated environment. 
# Ensure you have run the terminal command to install the correct libraries using pip.
# You must use the terminal window as directed in Step 3.

import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5500/baseball_stats.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract the Required Data

table = soup.find("table")
headers = [th.text.strip() for th in table.find("thead").find_all("th")]
rows = table.find("tbody").find_all("tr")

data = []
for row in rows:
    cols = [td.text.strip() for td in row.find_all("td")]
    data.append(cols)

# Convert to a DataFrame

# Convert the game data into a pandas DataFrame

df = pd.DataFrame(data, columns=headers)

# Inspect the DataFrame

print("📊 Scraped DataFrame:")
print(df.head())   # show first 5 rows
print("\nShape:", df.shape)

# Save and print the shaped data

print("\nData ready for saving!")

# Save the DataFrame to a CSV file named sports_statistics.csv

df.to_csv("sports_statistics.csv", index=False)
print("✅ Data saved to sports_statistics.csv")
