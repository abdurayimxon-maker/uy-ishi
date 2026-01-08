speed = {
    "Tesla": 250,
    "BMW": 240,
    "Mercedes": 260,
    "Audi": 230
}

for car, sp in sorted(speed.items(), key=lambda x: x[1], reverse=True):
    print(car, "-", sp)