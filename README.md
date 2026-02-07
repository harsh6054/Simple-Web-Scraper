# 🕸️ Simple Web Scraper in Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Issues](https://img.shields.io/github/issues/<your-username>/<your-repo>)

---

## 🔹 Description
This project is a **simple Python web scraper** that extracts data from a **user-provided website** and saves it into a **CSV file**. It demonstrates:

- Sending HTTP requests to websites.
- Parsing HTML content using **BeautifulSoup**.
- Exporting structured data into CSV format.

The script is **flexible**: it accepts any public URL. In the example, it extracts all `<h2>` headings from a webpage (like book titles), but it can be modified to scrape links, images, tables, or product details.

---

## 🔹 Features
- Takes **URL input from the user**.
- Extracts data from **HTML elements** using BeautifulSoup.
- Saves scraped data in **CSV format** (`scraped_data.csv`).
- Works on **any public website** with simple modification.
- Easy to extend for **real-world scraping tasks**.

---

## 🔹 Requirements
- **Python 3.x**
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `csv` (built-in)

Install dependencies:

```bash
pip install requests beautifulsoup4

