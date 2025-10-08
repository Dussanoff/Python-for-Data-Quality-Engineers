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
import StringObject

class Main:
    path = "inputs"
    for file in os.listdir(path):
        if isinstance(file, str) and file.endswith('.json'):
            recycle = f"{path}/recycle/{file}"
            file_path = f"{path}/{file}"
            to_remove = False
            with open(f"{file_path}", 'r') as input_file:
                str_json = input_file.read().replace("\n", "")
                articles_json = json.loads(str_json)
            try:
                for record in articles_json:
                    if StringObject.normalize(record["type"]) == "News":
                        article = News(StringObject.normalize(record["text"]), StringObject.normalize(record["city"]))
                        to_remove = True
                    elif StringObject.normalize(record["type"]) == "Private ad":
                        expiration_date = StringObject.normalize(record["expiration_date"])
                        try:
                            datetime.strptime(expiration_date, "%Y-%m-%d")
                        except:
                            print(f"Incorrect expiration date in the record {record} in the {file}! Try another file.")
                            break
                        article = PrivateAd(StringObject.normalize(record["text"]), expiration_date)
                        to_remove = True
                    elif StringObject.normalize(record["type"]) == "Daily horoscope":
                        article = DailyHoroscope(StringObject.normalize(record["text"]), StringObject.normalize(record["zodiac_sign"]))
                        to_remove = True
                    else:
                        print(f"Incorrect type {file}! Try another file.")
                        break
                    with open("outputs/articles.txt", "a") as articles_txt:
                        articles_txt.write(article.str())
            except Exception as e: print(e)
            if to_remove: os.rename(f"{file_path}", f"{recycle}")

