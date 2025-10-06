import os
from flask import Flask, jsonify
from scraper import scrape_data

app = Flask(__name__)


@app.route("/")
def home():
    return "🚀 Web Scraping Data Processing API is running! Try /scrape"


@app.route("/scrape")
def scrape():
    # Load the HTML file directly from the repo
    filepath = os.path.join(os.path.dirname(__file__), "baseball_stats.html")
    df = scrape_data(filepath)
    return jsonify(df.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
