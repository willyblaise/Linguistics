


hero = {
        "Nicole": "Nurse",
        "Champ": "Engineer",
        "Ruben": "Finance"
        }

for k, v in hero.items():
    print(k)


hero_update = { k+" hard":v for (k, v) in hero.items() }


print(hero_update)

print(hero_update["Nicole hard"])
