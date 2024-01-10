# naprawa kodowania pobranego json'a
# plik do poprawy jako argumenty w skrypcie w CMD | | skrypt.py plik1.json
import json
import sys

# sprawdzenie czy argumenty podane
if len(sys.argv) != 2:
    exit("Niepoprawna ilość argumentów, potrzebny jest jeden")

with open(sys.argv[1], mode="r") as friends_file:
    data_friends = json.load(friends_file)
# print(friends_file)  # sprawdzenie kodowania cp1250, utf8

# poprawa kodowania
for dict_object in data_friends["friends_v2"]:
    dict_object["name"] = dict_object["name"].encode("latin1").decode("utf8")

# nowa nazwa pliku | uzyte string[:-5]
new_file_name = (sys.argv[1])[:-5] + "_fixed.json"

# zapis poprawionego pliku json
with open(new_file_name, "w", encoding="utf8") as file:
    json.dump(data_friends, file, ensure_ascii=False, indent=2)

print("Zapisano do pliku:", new_file_name)

