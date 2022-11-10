import requests

url = "https://akabab.github.io/superhero-api/api/all.json"
names_hero = ["Captain America", "Hulk", "Thanos"]
resp = requests.get(url)
data = resp.json()
i = 0
while i < len(data):
    max_intelligence = 0
    if data[i]["name"] in names_hero:
        if data[i]["powerstats"]['intelligence'] > max_intelligence:
            max_intelligence = data[i]["powerstats"]['intelligence']
            number_list = i
    i += 1
print(f'Самый умный {data[number_list]["name"]}')
