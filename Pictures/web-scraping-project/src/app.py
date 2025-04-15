from flask import Flask, render_template
from scraper.scraper import fetch_data, parse_data

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://www.investing.com/"
    html_content = fetch_data(url)
    price = parse_data(html_content) if html_content else "Data not available"
    return render_template('index.html', price=price)

if __name__ == "__main__":
    app.run(debug=True)
