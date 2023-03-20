# Zadanie 2
import random

cities = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań", "Gdańsk", "Szczecin",
          "Bydgoszcz", "Lublin", "Białystok"]

tour = []
while len(tour) < 10:
    index = random.randint(0, len(cities)-1)
    c = cities[index]
    if c not in tour:
        tour.append(c)

print("\nPLAN WYCIECZKI")
for el in tour:
    print(el)
