import random

items = [
    "Toga Rektora", "Tablica z kredą", "Stara książka w bibliotece", "Laptop wykładowcy", 
    "Kawa z automatu", "Projektor z sali wykładowej", "Mikrofon do wykładów", 
    "Mysz komputerowa", "Biurko dziekana", "Flagi państwowe z sali wykładowej", 
    "Stary monitor CRT", "Tablica interaktywna", "Drzwi od sali wykładowej", 
    "Kreda do tablicy", "Krzesło ergonomiczne", "Głośnik z auli", 
    "Rzutnik slajdów", "Stolik z kawiarni", "Znacznik do markerów", 
    "Automat z napojami", "Kolega z ławki", "Fajka wykładowcy", "Korona rektora", "Sztandar uczelni", 
    "Kubek z napisem 'Najlepszy wykładowca'"
]

values = [random.randint(3, 30) for _ in range(25)]
volumes = [random.randint(1, 12) for _ in range(25)]

max_capacity = 50
num_items = len(items)

with open('items.txt', 'w') as file:
    file.write(f"{max_capacity}\n")
    file.write(f"{num_items}\n")
    for i in range(num_items):
        file.write(f"{values[i]}; {volumes[i]}; {items[i]}\n")