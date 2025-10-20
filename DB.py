"""
Expand previous Homework 5/6/7/8/9 with additional class, which allow to save records into database:
1.Different types of records require different data tables
2.New record creates new row in data table
3.Implement “no duplicate” check.
"""
import json
import os
import re

import pyodbc
from datetime import datetime

import StringObject
from Classes import News, PrivateAd, DailyHoroscope
from JSON import inputs, set_file_paths, set_recycle


class DB:
    def __init__(self, connection_string):
        self.create_connection(connection_string)
        self.cursor = self.connection.cursor()

    def __exit__(self):
        self.cursor.close()
        self.connection.close()

    def create_connection(self, connection_string):
        self.connection = pyodbc.connect(connection_string)

    def execute(self, command):
        try:
            result = self.cursor.execute(command)
            self.connection.commit()
        except Exception as e:
            raise f"{e}\n\t{command}"
        return result

    def create_table(self, table_name, columns):
        if self.cursor.tables(table=table_name, tableType='TABLE').fetchone() is None:
            self.execute(f"CREATE TABLE {table_name} ({columns})")

    def insert_into_table(self, table_name, values):
        rows = self.select_from_table(table_name).fetchall()
        if rows:
            for row in rows:
                result = re.sub(r"\(|\)", "", str(row).replace("None", "null")) + "\n"
                if result == values:
                    print(f"Row ({values})  has already exist in the table {table_name}! Try another file.")
                    return
        self.execute(f"INSERT INTO {table_name} VALUES({values})")
        print(f"Row successfully added {values} into the table {table_name}! Try another file.")


    def select_from_table(self, table_name, columns="*"):
        columns = "*" if None or "" else columns
        return self.execute(f"SELECT {columns} FROM {table_name}")

    @staticmethod
    def delete_json(file):
        os.rename(f"{set_file_paths(file)}", f"{set_recycle(file)}")

    @staticmethod
    def load_folder():
        articles = []
        delete = False
        for file in os.listdir(inputs):
            if isinstance(file, str) and file.endswith('.json'):
                with open(f"{set_file_paths(file)}", 'r') as input_file:
                    records = json.load(input_file)
                    input_file.close()
                try:
                    for record in records:
                        text = "" if record["text"] is None else record["text"]
                        if StringObject.normalize(record["type"]) == "News":
                            article = News(StringObject.normalize(text), StringObject.normalize(record["city"]))
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
                        elif StringObject.normalize(record["type"]) == "Daily horoscope":
                            article = DailyHoroscope(StringObject.normalize(text), StringObject.normalize(record["zodiac_sign"]))
                        else:
                            print(f"Incorrect type {file}! Try another file.")
                            continue
                        articles.append(article)
                        delete = True
                except Exception as e: print(e)
                #if delete == True: DB.delete_json(file)
            else:
                print(f"Incorrect type {file}! Try another file.")
        return articles

    @staticmethod
    def write_json(articles):
        db = DB(connection_string)
        for article in articles:
            table = type(article).__name__
            text = "null" if article.text is None or article.text == "" else "'" + article.text.replace("'", "''") + "'"
            date = "null" if article.date is None else "'" + str(article.date) + "'"
            values = text + ", " + date + ", "

            if table == "News":
                columns = "text, date, city"
                city = "'" + article.city + "'"
                values = values + city
            elif table == "PrivateAd":
                columns = "text, date, expiration_date"
                expiration_date = "'" + str(article.expiration_date) + "'"
                values = values + expiration_date
            elif table == "DailyHoroscope":
                columns = "text, date, zodiac_sign"
                zodiac_sign = "'" + article.zodiac_sign + "'"
                values = values + zodiac_sign
            else:
                continue
            db.create_table(table, columns)
            db.insert_into_table(table, values)


if __name__ == "__main__":
    connection_string = f"DRIVER={{SQLite3 ODBC Driver}};Direct=True;Database={os.path.join(os.path.dirname(__file__), "outputs", "articles.db")}"
    DB.write_json(DB.load_folder())


