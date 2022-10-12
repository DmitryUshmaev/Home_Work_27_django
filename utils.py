import csv
import json


# Конвертация csv в json

def csv_to_json(csvFilePath, jsonFilePath):
    with open(csvFilePath, encoding='utf-8') as csv_file:
        csvReader = csv.DictReader(csv_file)

        jsonArray = [row for row in csvReader]

    with open(jsonFilePath, 'w', encoding='utf-8') as json_file:
        jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
        json_file.write(jsonString)


csvFilePath = 'datasets/categories.csv'

jsonFilePath = 'datasets/ads.json'


# Изменение формата json файла для загрузки в базу данных на основе моделей

def reformat_json(jsonFilePath):
    with open(jsonFilePath, encoding='utf-8') as json_file:
        json_f = json.load(json_file)
        new_json = []

        for row in json_f:
            new_json.append({
                "model": "ads.ADS",
                "pk": row["Id"],
                "fields": {
                    "name": row["name"],
                    "author": row["author"],
                    "price": row["price"],
                    "description": row["description"],
                    "address": row["address"],
                    "is_published": row["is_published"]
                }
            })

    with open(jsonFilePath, 'w', encoding='utf-8') as json_file:
        json_reformat = json.dumps(new_json, ensure_ascii=False, indent=4)
        json_file.write(json_reformat)


reformat_json(jsonFilePath)
