from pprint import pprint
import requests
import json

url = "https://akabab.github.io/superhero-api/api/all.json"
resp = requests.get(url)
hero_dict = resp.json()
heroes_list =[]
for hero in hero_dict:
    if hero['name'] == 'Hulk':
       heroes_list.append(hero)
    elif hero['name'] == 'Captain America':
       heroes_list.append(hero)
    elif hero['name'] == 'Thanos':
       heroes_list.append(hero)
       
       max_intelligence = 0
       hero_name = ""
       
       for hero in heroes_list:
        intelligence = int(hero['powerstats']['intelligence'])
        if intelligence > max_intelligence:
           max_intelligence = intelligence
           hero_name = hero['name']

       print(hero_name)
     
     

