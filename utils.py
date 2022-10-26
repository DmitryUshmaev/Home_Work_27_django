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


csvFilePath = 'datasets/user.csv'

jsonFilePath = 'datasets/user.json'


# Изменение формата json файла для загрузки в базу данных на основе моделей


def convert_json(csv_file, json_file, model):
    result = []
    with open(csv_file, encoding='utf-8') as csv_f:
        for row in csv.DictReader(csv_f):
            to_add = {
                "model": model,
                "pk": int(row['Id'] if 'Id' in row else row['id'])
            }
            if 'id' in row:
                del row['id']
            else:
                del row['Id']

            if 'location_id' in row:
                row['location'] = [int(row['location_id'])]
                del row['location_id']

            to_add["fields"] = row
            result.append(to_add)

    with open(json_file, 'w', encoding='utf-8') as json_f:
        json_f.write(json.dumps(result, indent=4, ensure_ascii=False))


convert_json(csvFilePath, jsonFilePath, 'users.User')
