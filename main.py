import requests
import json
import sys
import os


API_ENDPOINT = "https://api.poeditor.com/v2/terms/list"
API_KEY = "345deb62750138e88476d51cd8c18d5a"
API_ID = 180800
PATH= os.path.dirname(os.path.realpath(__file__))

def main():
    try:
        language = sys.argv[1]
    except:
        print("Need language code at argument line(exp: ru)")
        exit()

    json_file = PATH + '/' + language + '.json'

    data = {'api_token':API_KEY,
            'id':API_ID,
            'language':language
        }
    dataParse = dict()

    try:
        responseData = json.loads(requests.post(url = API_ENDPOINT, data = data).text)
        for line in responseData["result"]["terms"]:
            key = line["term"]
            value = line["translation"]["content"]
            dataParse[key] = value
        with open(json_file, 'w', encoding="utf-8") as json_file:
            json.dump(dataParse, json_file, indent=4, ensure_ascii=False)
    except:
        print("No correct responce's")
        exit()

if __name__ == "__main__":
    main()