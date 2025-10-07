import csv
import os
import re

"""
Calculate number of words and letters from previous Homeworks 5/6 output test file.
Create two csv:
1.word-count (all words are preprocessed in lowercase)
2.letter, count_all, count_uppercase, percentage (add header, space characters are not included)
CSVs should be recreated each time new record added.
"""

articles = "articles.txt"


def count(array, item):
    counter = 0
    for i in array:
        if i == item:
            counter += 1
    return counter



def count_words_csv_writer():
    fieldnames = ["word", "count"]
    with open(articles, "r") as file:
        list = re.sub(r",|\.|\'", "", file.read().lower()).strip().split()
    with open("countWords.csv", "w", newline = "") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        for word in list:
            counter = count(list, word)
            writer.writerow({fieldnames[0]: word, fieldnames[1]: counter})




def count_letters_csv_writer():
    fieldnames = ["letter", "count_all", "count_uppercase", "percentage"]
    list=[]
    count_uppercase = 0
    percentage = 0
    with (open(articles, "r") as file):
        for word in re.sub(r",|\.|\'", "", file.read()).strip().split():
            for letter in word:
                list.append(letter)
                #list_lover.append(letter.lower())
    with open("countLetters.csv", "w", newline = "") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        for i in range(len(list)):
            letter = list[i]
            count_all = count(list, letter.lower())
            if letter.isupper():
                count_uppercase = count(list, letter.upper())
                percentage = str(format(count_uppercase/count_all*100, ".2f"))+"%"
            writer.writerow({fieldnames[0]: letter, fieldnames[1]: count_all, fieldnames[2]: count_uppercase, fieldnames[3]: percentage})






count_words_csv_writer()
count_letters_csv_writer()