capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Japan": "Tokyo",
    "China": "Beijing",
    "India": "New Delhi",
    "Russia": "Moscow",
    "Brazil": "Brasília",
    "Canada": "Ottawa",
    "Australia": "Canberra",
    "Mexico": "Mexico City",
    "South Africa": "Pretoria",
    "Argentina": "Buenos Aires",
    "United Kingdom": "London",
    "South Korea": "Seoul",
    "Turkey": "Ankara",
    "Saudi Arabia": "Riyadh",
    "Egypt": "Cairo",
    "Indonesia": "Jakarta",
    "Nigeria": "Abuja",
    "Pakistan": "Islamabad",
    "Bangladesh": "Dhaka",
    "Philippines": "Manila",
    "Vietnam": "Hanoi",
    "Thailand": "Bangkok",
    "Malaysia": "Kuala Lumpur",
    "Singapore": "Singapore",
    "New Zealand": "Wellington",
    "Ireland": "Dublin",
    "Portugal": "Lisbon",
    "Greece": "Athens",
    "Norway": "Oslo",
    "Sweden": "Stockholm",
    "Finland": "Helsinki",
    "Denmark": "Copenhagen",
    "Iceland": "Reykjavik",
    "Belgium": "Brussels",
    "Netherlands": "Amsterdam",
}

# capitals.update({"Germany": "Berlin"})
# capitals.pop("Germany")
# capitals.popitem()
# capitals.clear()

# for key in capitals.keys():
#      print(key)

items = capitals.items()

for key, value in items:
    print(f"{key}: {value:>40}", end="\n")
