import requests
import json
from flask import Flask, request, render_template
import logging
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
            }
        
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
        
data = []
titles = soup.select("div._4rR01T")  # CSS selector for product titles
prices = soup.select("div._30jeq3._1_WHN1")  # CSS selector for product prices

print("Number of titles:", len(titles))
print("Number of prices:", len(prices))

for title, price in zip(titles, prices):
                title_text = title.text.strip()
                price_text = price.text.strip().replace('\u20b9', '')


                data.append({
                       "Title":title.text,
                       "Price":price.text
                              })
                
with open("product_data.json", "w") as file:
    json.dump(data, file, indent=4)