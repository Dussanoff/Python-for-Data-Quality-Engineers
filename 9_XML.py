"""
Expand previous Homework 5/6/7/8 with additional class, which allow to provide records by XML file:
1.Define your input format (one or many records)
2.Default folder or user provided file path
3.Remove file if it was successfully processed
"""
from datetime import datetime
import os
import re
import xml.etree.ElementTree as ET

from Classes import News
from Classes import PrivateAd
from Classes import DailyHoroscope
import StringObject
import JSON


def read_xml():
    remove_list = []
    articles_dict = {}
    for file in os.listdir(JSON.inputs):
        file_path = JSON.set_file_paths(file)
        if file.endswith('.xml'):
            xml_file = ET.parse(file_path)
            root = xml_file.getroot()
            for record in root:
                text = record.find("text").text if isinstance(record.find("text").text, str) else ""
                if StringObject.normalize(record.attrib.get("type")) == "News":
                    city = record.find("city").text if isinstance(record.find("city").text, str) else ""
                    article = News(StringObject.normalize(text), city)
                    to_remove = True
                elif StringObject.normalize(record.attrib.get("type")) == "Privatead":
                    if re.search(r"^\d+(\.|,\d)?\d*$", record.find("expiration_date").text):
                        expiration_date = str(datetime.fromordinal(int(float(record.find("expiration_date").text)))).split(" ")[0]
                    else:
                        expiration_date = record.find("expiration_date").text
                    try:
                        datetime.strptime(expiration_date, "%Y-%m-%d")
                    except:
                        print(f"Incorrect expiration date in the record {ET.tostring(record).decode().replace("\n","")} in the {file}! Try another file.")
                        break
                    article = PrivateAd(StringObject.normalize(text), expiration_date)
                    to_remove = True
                elif StringObject.normalize(record.attrib.get("type")) == "Dailyhoroscope":
                    article = DailyHoroscope(StringObject.normalize(text), StringObject.normalize(record.find("zodiac_sign").text))
                    to_remove = True
                else:
                    print(f"Incorrect type {file}! Try another file.")
                    break
                articles_dict[article.str()] = file
                if to_remove: remove_list.append(file)
        # break
    return (articles_dict, set(remove_list))

def write_xml(arg):
    print(arg)
    root = ET.Element("articles")
    dict = arg[0]
    set = arg[1]
    for article, file in dict.items():
        file_path = JSON.set_file_paths(file)
        type = article.splitlines()[0]
        body = article.splitlines()[1:]
        text = '\n'.join(str(x) for x in body).strip().replace("\n", "")

        sub_element = ET.SubElement(root, "article", {"type": type})
        ET.SubElement(sub_element, "file").text = file
        ET.SubElement(sub_element, "text").text = text

    tree = ET.ElementTree(root)
    tree.write(f"{JSON.outputs}/articles.xml")
    for file in set:
        os.rename(f"{JSON.set_file_paths(file)}", f"{JSON.set_recycle(file)}")

write_xml(read_xml())