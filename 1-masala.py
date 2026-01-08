cars = {
    "Malibu": 35000,
    "Spark": 12000,
    "Cobalt": 18000,
    "Tracker": 28000
}


max_price = max(cars.values())
min_price = min(cars.values())

max_car = [k for k, v in cars.items() if v == max_price][0]
min_car = [k for k, v in cars.items() if v == min_price][0]

average_price = sum(cars.values()) / len(cars)

print("Eng qimmat avtomobil:", max_car, "-", max_price)
print("Eng arzon avtomobil:", min_car, "-", min_price)
print("Avtomobillarning o'rtacha narxi:", average_price)