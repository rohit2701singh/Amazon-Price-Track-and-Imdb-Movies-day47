# this is a versatile code for amazon. Their main product page detail is same for every product

import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

# ________________ e-mail detail ________________

MY_ITEM_PRICE = 2500
MY_EMAIL = "rohxxxxxxxxxxxxxom"
PASS = os.environ.get("SMTP_MAIL_PASS")
RECEIVER_EMAIL = "rxxxxxxxxxxxxxl.com"

# __________________amazon soup detail_________________

# URL = "https://www.amazon.in/Instant-Pot-Duo-Multi-Functional-Pressure/dp/B01NBKTPTS/ref=sr_1_4?keywords=Instant+Pot+Duo+Plus+9-in-1+Electric+Pressure+Cooker%2C+Slow+Cooker%2C+Rice+Cooker%2C+Steamer%2C+Saut%C3%A9%2C+Yogurt+Maker%2C+Warmer+%26+Sterilizer%2C+Includes+App+With+Over+800+Recipes%2C+Stainless+Steel%2C+3+Quart&nsdOptOutParam=true&qid=1698243087&sr=8-4"
URL = "https://www.amazon.in/OnePlus-Wireless-Earbuds-Titanium-Playback/dp/B0BYJ6ZMTS/ref=sr_1_4?crid=DTTYAEY1S3C7&keywords=oneplus%2Bearbuds&qid=1698251198&sprefix=oneplu%2Caps%2C282&sr=8-4&th=1"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6"
}

response = requests.get(url=URL, headers=header)
content = response.text
# print(content)
soup = BeautifulSoup(content, "lxml")

item_name = soup.find(name="span", class_="a-size-large product-title-word-break").getText().strip()
print(item_name)

try:
    old_price_tag = soup.find(name="span", class_="a-price a-text-price")
    old_price = (old_price_tag.find(name="span", class_="a-offscreen")).getText().strip("₹")
    print(old_price)
except:
    old_price = "old price not found"
    print(old_price)

new_price_tag = (soup.find(name="span", class_="a-price-whole")).getText()  # 10,000. this was response comma and fullstop included
new_price = (new_price_tag.strip(".")).replace(",", "")
print(new_price)

# _________________sending e-mail detail __________________

if int(new_price) <= MY_ITEM_PRICE:
    print("price is low, sending an mail.")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=f"Subject: Item price down info.\n\nHurry Up!\n\nProduct_name: {item_name}\n\nold_price: INR {old_price}\nnew_price: INR {new_price}\n\nlink: {URL}"
        )
