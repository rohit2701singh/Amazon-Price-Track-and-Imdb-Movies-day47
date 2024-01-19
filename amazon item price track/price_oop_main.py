from price_tracker_oop import ProductPrice

url = ("https://www.amazon.in/dp/B09G9BL5CP?pd_rd_w=KYx7h&content-id=amzn1.sym.1478d6c6-988f-4d72-8837-8c9870832d12"
       "&pf_rd_p=1478d6c6-988f-4d72-8837-8c9870832d12&pf_rd_r=6D9S679BWFB8R98NXKFT&pd_rd_wg=fiwJW&pd_rd_r=6574e7bf"
       "-96af-4c49-ad41-18bdc52da31a")
user_aget = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 "
             "Safari/537.36")
language = "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6"

obj = ProductPrice(web_url=url, header_user_agent=user_aget, header_accepted_language=language)
# print(obj)

name = obj.item_name()
old_price = obj.item_new_price()
new_price = obj.item_old_price()

print(f"{name}\n{old_price}\n{new_price}")

email = obj.detail_send_mail(
    user_price=51000,
    email_host="smtp.gmail.com",
    user_password="tqxxxxxxxh",
    user_mail="rohxxxxxom",
    receiver_mail="rohixxxxxxxil.com"
)

print(email)
