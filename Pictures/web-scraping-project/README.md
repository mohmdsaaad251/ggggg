# Web Scraping Project

This project is a web scraping application that utilizes Flask to serve a web interface for displaying scraped data. The application fetches data from specified websites, parses the HTML content, and presents the information in a user-friendly format.

## Project Structure

```
web-scraping-project
├── src
│   ├── app.py                # Entry point of the application
│   ├── scraper
│   │   ├── __init__.py       # Marks the scraper directory as a package
│   │   └── scraper.py         # Contains web scraping logic
│   └── templates
│       └── index.html         # HTML template for displaying scraped data
├── requirements.txt           # Lists project dependencies
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd web-scraping-project
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   Start the Flask server by running:
   ```
   python src/app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

## Usage Guidelines

- Navigate to the home page to view the scraped data.
- The application can be modified to scrape different websites by updating the scraping logic in `src/scraper/scraper.py`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.