"""
Expand previous Homework 5/6/7 with additional class, which allow to provide records by JSON file:
1.Define your input format (one or many records)
2.Default folder or user provided file path
3.Remove file if it was successfully processed
"""
from datetime import datetime
import os
import json

from Classes import News
from Classes import PrivateAd
from Classes import DailyHoroscope
import StringObject

inputs = "inputs"
outputs = "outputs"
def set_file_paths(file):
    return f"{inputs}/{file}"

def set_recycle(file):
    return f"{inputs}/recycle/{file}"


def read_json():
    remove_list = []
    articles_dict = {}
    for file in os.listdir(inputs):
        file_path = set_file_paths(file)
        if isinstance(file, str) and file.endswith('.json'):
            to_remove = False
            with open(f"{file_path}", 'r') as input_file:
                str_json = input_file.read().replace("\n", "")
                articles_json = json.loads(str_json)
            try:
                for record in articles_json:
                    text = "" if record["text"] is None else record["text"]
                    if StringObject.normalize(record["type"]) == "News":
                        article = News(StringObject.normalize(text), StringObject.normalize(record["city"]))
                        to_remove = True
                    elif StringObject.normalize(record["type"]) == "Private ad":
                        if isinstance(record["expiration_date"], float):
                            expiration_date = str(datetime.fromordinal(int(record["expiration_date"]))).split(" ")[0]
                        else:
                            expiration_date = record["expiration_date"]
                        try:
                            datetime.strptime(expiration_date, "%Y-%m-%d")
                        except:
                            print(f"Incorrect expiration date in the record {record} in the {file}! Try another file.")
                            break
                        article = PrivateAd(StringObject.normalize(text), expiration_date)
                        to_remove = True
                    elif StringObject.normalize(record["type"]) == "Daily horoscope":
                        article = DailyHoroscope(StringObject.normalize(text), StringObject.normalize(record["zodiac_sign"]))
                        to_remove = True
                    else:
                        print(f"Incorrect type {file}! Try another file.")
                        break
                    articles_dict[article.str()] = file
                    if to_remove: remove_list.append(file)
            except Exception as e: print(e)
    return (articles_dict, set(remove_list))

def write_json(arg):
    dict = arg[0]
    set = arg[1]
    json_list = []
    for article, file in dict.items():
        type = article.splitlines()[0]
        body = article.splitlines()[1:]
        text = '\n'.join(str(x) for x in body).strip()
        json_list.append({"file": file, "type": type, "text": text})
    json.dump(json_list, open(f"{outputs}/articles.json", "w"))
    for file in set:
        os.rename(f"{set_file_paths(file)}", f"{set_recycle(file)}")

write_json(read_json())
