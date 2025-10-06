import os
import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_data(source: str) -> pd.DataFrame:
    """
    Scrape table data from either a URL or a local HTML file.
    Returns a DataFrame.
    """

    # Check if source is a URL or local file
    if source.startswith("http://") or source.startswith("https://"):
        # Fetch from the web
        response = requests.get(source)
        response.raise_for_status()
        html_content = response.text
    else:
        # Load local file
        if not os.path.exists(source):
            raise FileNotFoundError(f"⚠️ File not found: {source}")
        with open(source, "r", encoding="utf-8") as f:
            html_content = f.read()

    # Parse HTML
    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find("table")

    if not table:
        raise ValueError("⚠️ No <table> found in the HTML!")

    # Extract headers
    headers = [th.get_text(strip=True) for th in table.find_all("th")]

    # Extract rows
    data = []
    for row in table.find_all("tr")[1:]:
        cols = [td.get_text(strip=True) for td in row.find_all("td")]
        if cols:
            data.append(cols)

    return pd.DataFrame(data, columns=headers)
