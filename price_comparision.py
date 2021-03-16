import requests
from bs4 import BeautifulSoup
import smtplib
import time

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

def amazonPrice():
	item = input("Enter the item you would like to search for: ")
	URL = "https://www.amazon.in/s?k=" + item
	page = requests.get(URL, headers = headers)
	soup = BeautifulSoup(page.content, "html.parser")
	products = []
	links = []
	prices = []
	for link in soup.find_all("a",{"class":"a-link-normal a-text-normal"}, limit = 5):
		links.append(link["href"])
	for sp in soup.find_all("span", {"class": "a-size-base-plus a-color-base a-text-normal"}, limit = 5):
		products.append(sp.text)
	for p in soup.find_all("span", {"class": "a-price-whole"}, limit = 5):
		prices.append(p.text)
	print(prices)

def temp():
	price = soup.find(id = "priceblock_ourprice").text.split()[1] #finds price of the product and extracts just the text
	converted_price = [] 
	for i in price[0:5]: 
		if i.isdigit():
			converted_price.append(i) #The price reads as ₹&nbsp;4,199.00 on the site, hence the numbers need to be exracted.

	converted_price = int("".join(converted_price)) #Converting the string price to integer for comparison
	print("Current price: " + converted_price)

amazonPrice()