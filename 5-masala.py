car_count = {
    "Chevrolet": 120,
    "Toyota": 95,
    "BMW": 60,
    "Kia": 75
}

max_count = max(car_count.values())
min_count = min(car_count.values())

max_car = [k for k, v in car_count.items() if v == max_count][0]
min_car = [k for k, v in car_count.items() if v == min_count][0]

print("Eng ko'p sotilgan mashina:", max_car, "-", max_count)
print("Eng kam sotilgan mashina:", min_car, "-", min_count)