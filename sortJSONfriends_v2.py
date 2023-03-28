# sortowanie po timestamp pliku JSON
import json
import sys

# sprawdzanie ilości podanych argumentów
if len(sys.argv) != 2:
    exit("Niepoprawna ilość argumentów, potrzebny jest jeden")

with open(sys.argv[1], "r") as fileJS:
    data_json = json.load(fileJS)

# print(data_json)
# print(data_json["friends_v2"][1]["timestamp"])

data_json["friends_v2"] = sorted(data_json["friends_v2"], key=lambda x: x["timestamp"], reverse=True)

# nowa nazwa pliku
new_file_name = (sys.argv[1])[:-5] + "_sorted.json"

# print(data_json)
with open(new_file_name, "w") as fileJS:
    json.dump(data_json, fileJS, ensure_ascii=False, indent=2)
