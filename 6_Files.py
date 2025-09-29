"""
Expand previous Homework 5 with additional class, which allow to provide records by text file:
1.Define your input format (one or many records)
2.Default folder or user provided file path
3.Remove file if it was successfully processed
4.Apply case normalization functionality form Homework 3/4
"""
from datetime import datetime
import os
import json

from Classes import News
from Classes import PrivateAd
from Classes import DailyHoroscope

class Main:
    path = "inputs"
    for file in os.listdir(path):
        if isinstance(file, str) and file.endswith('.json'):
            recycle = f"{path}/recycle/{file}"
            file_path = f"{path}/{file}"
            with open(f"{file_path}", 'r') as input_file:
                str_json = input_file.read().replace("\n", "")
                articles_json = json.loads(str_json)
            try:
                for record in articles_json:
                    if record["type"] == "News":
                        article = News(record["text"], record["city"])
                    elif record["type"] == "Private Ad":
                        expiration_date = record["expiration_date"]
                        try:
                            datetime.strptime(expiration_date, "%Y-%m-%d")
                        except:
                            print(f"Incorrect expiration date in the record {record} in the {file_path}! Try another file.")
                            continue
                        article = PrivateAd(record["text"], expiration_date)
                    elif record["type"] == "Daily Horoscope":
                        article = DailyHoroscope(record["text"], record["zodiac_sign"])
                    else:
                        print(f"Incorrect type {file_path}! Try another file.")
                        continue
                    with open("articles.txt", "a") as articles_txt:
                        articles_txt.write(article.str())
            finally:
                os.rename(f"{file_path}", f"{recycle}")
