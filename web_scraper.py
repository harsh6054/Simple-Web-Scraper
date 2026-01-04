import requests
from bs4 import BeautifulSoup
import csv


url = input("Enter the website URL to scrape: ")
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
headings = soup.find_all("h2")
data = []

for heading in headings:
    data.append([heading.text.strip()])
    
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Extracted Data"])
    writer.writerows(data)

print("Data successfully scraped and saved to scraped_data.csv")
