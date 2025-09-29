"""
Create a tool, which will do user generated news feed:
1.User select what data type he wants to add
2.Provide record type required data
3.Record is published on text file in special format



You need to implement:
1.News – text and city as input. Date is calculated during publishing.
2.Private ad – text and expiration date as input. Day left is calculated during publishing.
3.Your unique one with unique publish rules.



Each new record should be added to the end of file. Commit file in git for review.
"""
import time
from datetime import datetime


class Article:
    def __init__(self, text):
        self.text = text
        self.date = datetime.today()

    def publish(self, text):
        pass

    def str(self):
        return f"{self.__class__.__name__}\n{self.text}\n{self.date.strftime("%Y-%m-%d %H:%M:%S")}"

    @staticmethod
    def input_text():
        return input("Provide the text\n")




class News(Article):
    def __init__(self, text, city):
        Article(text)
        self.text = text
        self.city = city
        self.date = datetime.today()

    def publish(self, text, city):
        pass

    def str(self):
        return f"{self.__class__.__name__}\n{self.text}\n{self.city}, {self.date.strftime("%Y-%m-%d %H:%M:%S")}\n\n"

class PrivateAd(Article):
    def __init__(self, text, expiration_date):
        Article(text)
        self.text = text
        self.date = datetime.today()
        self.expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")

    def publish(self):
        pass

    def str(self):
        return (f"{self.__class__.__name__}\n{self.text}\nUntil: {self.expiration_date.strftime("%Y-%m-%d %H:%M:%S")}, {self.expiration_date - datetime.today()} left\n\n")

class DailyHoroscope:
    def __init__(self, text, zodiac_sign):
        Article(text)
        self.text = text
        self.date = datetime.today()
        self.zodiac_sign = zodiac_sign

    def publish(self, text, expiration_date):
        pass

    def str(self):
        return f"{self.__class__.__name__}\n{self.text}\nZodiac sign: {self.zodiac_sign}, {self.date.strftime("%Y-%m-%d %H:%M:%S")}\n\n"

class Main:
    @staticmethod
    def main():
        welcoming_message = input("What do you want to add?\nNews - 1,\nPrivate Ad - 2,\nDailyHoroscope - 3.\n")
        while welcoming_message in ("1", "2", "3"):
            if welcoming_message.strip() == "1":
                article = News(Article.input_text(), input("Provide the city\n"))
            elif welcoming_message.strip() == "2":
                expiration_date = input("Provide the expiration date in format YYYY-MM-DD\n")
                try:
                    datetime.strptime(expiration_date, "%Y-%m-%d")
                except:
                    print("\nIncorrect value! Try again.")
                    break
                article = PrivateAd(Article.input_text(), expiration_date)
            elif welcoming_message.strip() == "3":
                article = DailyHoroscope(Article.input_text(), input("Provide the zodiac sign\n"))
            else:
                print("\nIncorrect value! Try again.")
                break
            with open("articles.txt", "a") as articles_txt:
                articles_txt.write(article.str())
                break








