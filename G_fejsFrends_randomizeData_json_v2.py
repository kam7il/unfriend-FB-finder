# tworzy losowe dane fejsFrend w formacie FB json
import json
import names
import random
import datetime as dt
from datetime import timedelta


def random_timestamp(today_date_):
    random_date = today_date_ - timedelta(days=1825) * random.random()
    return int(random_date.timestamp())


# tworzenie szablonu json FB
fejs_dane_random = {
  "friends_v2": [
  ]
}

# ustawianie losowego timestamp po dacie
today_date = dt.datetime.now()

# randomizacja danych
for x in range(0, 100):
    fejs_dane_random["friends_v2"].append({})
    fejs_dane_random["friends_v2"][x]["name"] = names.get_full_name()
    fejs_dane_random["friends_v2"][x]["timestamp"] = random_timestamp(today_date)

# # sprawdzenie danych
# for x in fejs_dane_random["friends_v2"]:
#     print(x)

with open("friends_random.json", "w", encoding="utf8") as file:
    json.dump(fejs_dane_random, file, ensure_ascii=False, indent=2)

print("Zapisano do pliku friends_random.json")
