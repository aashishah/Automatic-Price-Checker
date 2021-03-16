import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.in/XP-Pen-Graphic-8-35X5-33-Pressure-Sensitivity/dp/B085HJKTK3/ref=sr_1_8?dchild=1&keywords=digital+tablet&qid=1610712614&sr=8-8"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

page = requests.get(URL, headers = headers) #to get page content
soup = BeautifulSoup(page.content, "html.parser") #BeautifulSoup object with the parsed html content

#print(soup.prettify())
#title = soup.find(id = "productTitle").text.strip()
#print(title)
def checkPrice():
	price = soup.find(id = "priceblock_ourprice").text.split()[1] #finds price of the product and extracts just the text
	converted_price = [] 
	for i in price[0:5]: 
		if i.isdigit():
			converted_price.append(i) #The price reads as ₹&nbsp;4,199.00 on the site, hence the numbers need to be exracted.

	converted_price = int("".join(converted_price)) #Converting the string price to integer for comparison
	print("Current price: " + converted_price)

	if converted_price < 4300:
		sendEmail()

def sendEmail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo() #command sent by an email server when connecting to another server to start process of sending an email
	server.starttls()
	server.ehlo()

	server.login('abc@gmail.com', "your password")

	subject = "The price has fallen down!"
	body = "Check price for the tablet."
	msg = f"Subject: {subject}\n{body}"

	server.sendmail(
		"xyz@gmail.com", #replace with actual sender
		"abc@gmail.com", #replace with actual reciever
		msg #what to send
		) #sending the mail to myself

	print("Email sent.") #console log (lol)

	server.quit() #terminate server connection


while True:
	checkPrice()
	time.sleep(432000)
