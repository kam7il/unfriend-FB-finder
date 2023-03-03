# naprawa kodowania pobranego json'a
# plik do poprawy jako argumenty w skrypcie w CMD | | skrypt.py plik1.json
import json
import sys

# sprawdzenie czy argumenty podane
if len(sys.argv) != 2:
    exit("Niepoprawna ilość argumentów, potrzebny jest jeden")

friends_file = open(sys.argv[1], mode="r")
# print(friends_file)  # sprawdzenie kodowania cp1250, utf8
data_friends = json.load(friends_file)
friends_file.close()
data_friends_fixed = data_friends.copy()

# poprawa kodowania
for x, y in enumerate(data_friends["friends_v2"]):
    data_friends_fixed["friends_v2"][x]["name"] = y["name"].encode("latin1").decode("utf8")

# nowa nazwa pliku | uzyte string[:-5]
new_file_name = (sys.argv[1])[:-5] + "_fixed.json"

# zapis poprawionego pliku json
with open(new_file_name, "w", encoding="utf8") as file:
    json.dump(data_friends_fixed, file, ensure_ascii=False, indent=2)

print("Zapisano do pliku:", new_file_name)

