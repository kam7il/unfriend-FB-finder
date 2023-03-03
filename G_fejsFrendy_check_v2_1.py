# rozwiązanie przy pomocy słownika, użycie znaczników czasu. Potrzebne dwa pliki json
# pliki jako argumenty w skrypcie w CMD | skrypt.py plik1.json plik2.json
import json
import sys

fejs_dane_usu = []
fejs_dane_dod = []

# sprawdzenie czy argumenty podane
if len(sys.argv) != 3:
    exit("Niepoprawna ilość argumentów, potrzebne są dwa")

# wczytanie z json danych | stare dane
with open(sys.argv[1], encoding="utf8") as file:
    fejs_dane_json_1 = json.load(file)
# sprawdzenie wczytanych danych
# print(fejs_dane_json_1)

# wczytanie z json danych | nowe dane
with open(sys.argv[2], encoding="utf8") as file:
    fejs_dane_json_2 = json.load(file)
# sprawdzenie wczytanych danych
# print(fejs_dane_json_2)

# znajomi którzy mnie usuneli
for x in fejs_dane_json_1["friends_v2"]:
    var_check = False
    for y in fejs_dane_json_2["friends_v2"]:
        if x.get("timestamp") == y.get("timestamp"):
            var_check = True
    if var_check == False:
        fejs_dane_usu.append(x.get("name"))

# znajomi którzy mnie dodali
for x in fejs_dane_json_2["friends_v2"]:
    var_check = False
    for y in fejs_dane_json_1["friends_v2"]:
        if x.get("timestamp") == y.get("timestamp"):
            var_check = True
    if var_check == False:
        fejs_dane_dod.append(x.get("name"))


# znajomi którzy przybyli
print("Znajomi którzy przybyli:")
for x in fejs_dane_dod:
    print(x)

print("-----------------------------------")

# znajomi którzy mnie usuneli
print("Znajomi którzy mnie usuneli:")
for x in fejs_dane_usu:
    print(x)
