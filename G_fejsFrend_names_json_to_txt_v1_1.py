# wczytywanie pliku do przetworzenia przez file input stream z CMD (skrypt.py < data.json)
# nie ma na to wpływu chcp w CMD, 852 czy 65001, ten sam wynik
# brakuje zabezpieczenia przed brakiem input stream file (skrypt.py < data.txt)
import fileinput
import json

string_json = ""
data_json = None

with fileinput.input(encoding="utf-8") as file:
    for line in file:
        # print(line.encode('cp1250', 'surrogateescape').decode('utf-8'))  # windows1250 - cp1250
        string_json += line
data_json = json.loads(string_json)


with open("friends_namesToText.txt", "w", encoding="utf8") as file:
    for x in data_json["friends_v2"]:
        file.write((x["name"] + "\n").encode('cp1250', 'surrogateescape').decode('utf-8'))

print("Zapisano do pliku friends_namesToText.txt")
