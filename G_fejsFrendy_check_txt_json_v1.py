# rozwiazanie za pomocą listy, brak użycia znaczników czasu, mało optymalne
# dobre do użycia kiedy mamy jeden z plików w txt bez znaczników czasu. Same imiona i nazwiska
import json

fejs_dane_1 = []
fejs_dane_2 = []
fejs_dane_json = None
# wczytanie z txt danych | stare dane
with open("friends_names.txt", encoding="utf8") as file:
    # print(file) # sprawdzanie jaki encoding
    for x in file.readlines():
        fejs_dane_1.append(x.strip())
# sprawdzenie wczytanych danych
# print(fejs_dane_1)

# wczytanie z json danych | nowe dane
with open("friends_1_fixed1.json", encoding="utf8") as file:
    fejs_dane_json = json.load(file)
# sprawdzenie wczytanych danych
# print(fejs_dane_json)

# frendy do listy
fejs_dane_2 = [x["name"] for x in fejs_dane_json["friends_v2"]]


# znajomi którzy przybyli
print("Znajomi którzy przybyli:")
for x in fejs_dane_2:
    if not x in fejs_dane_1:
        print(x)

print("-----------------------------------")

# znajomi którzy mnie usuneli
print("Znajomi którzy mnie usuneli:")
for x in fejs_dane_1:
    if not x in fejs_dane_2:
        print(x)

