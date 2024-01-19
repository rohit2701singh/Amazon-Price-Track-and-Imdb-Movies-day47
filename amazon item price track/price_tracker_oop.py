import requests
from bs4 import BeautifulSoup
import lxml
import smtplib


class ProductPrice:
    def __init__(self, web_url: str, header_user_agent: str, header_accepted_language: str):
        self.__item_name = None
        self.__old_price = None
        self.__new_price = None

        self.__URL = web_url
        self.__header = {
            "User-Agent": header_user_agent,
            "Accept-Language": header_accepted_language
        }
        self.__get_content()
        self.item_name()
        self.item_old_price()
        self.item_new_price()

    def __str__(self):
        return self.__content

    def __get_content(self):
        response = requests.get(url=self.__URL, headers=self.__header)
        self.__content = response.text
        self.__soup = BeautifulSoup(self.__content, "lxml")

    def item_name(self):
        """return item name"""
        self.__item_name = self.__soup.find(name="span", class_="a-size-large product-title-word-break").getText().strip()
        return self.__item_name

    def item_old_price(self):
        """return old price of item if available otherwise returns 'old price not found'"""
        try:
            old_price_tag = self.__soup.find(name="span", class_="a-price a-text-price")
            self.__old_price = (old_price_tag.find(name="span", class_="a-offscreen")).getText().strip("₹")
            return self.__old_price
        except:
            old_price = "old price not found"
            return old_price

    def item_new_price(self):
        """return discounted new price"""
        new_price_tag = (self.__soup.find(name="span", class_="a-price-whole")).getText()
        self.__new_price = (new_price_tag.strip(".")).replace(",", "")
        return self.__new_price

    def detail_send_mail(self, user_price: int, email_host: str, user_mail: str, user_password: str, receiver_mail: str):
        """send mail when price is below user's price"""

        if int(self.__new_price) <= user_price:
            with smtplib.SMTP(email_host, 587) as connection:
                connection.starttls()
                connection.login(user=user_mail, password=user_password)
                connection.sendmail(
                    from_addr=user_mail,
                    to_addrs=receiver_mail,
                    msg=f"Subject: Item price down info.\n\nHurry Up!\n\nProduct_name: {self.__item_name}\n\nold_price: INR {self.__old_price}\nnew_price: INR {self.__new_price}\n\nlink: {self.__URL}"
                )
            return f"email send successful"
        else:
            return f"item price is not below user price"