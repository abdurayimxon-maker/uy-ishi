professions = {
    "Bill Gates": "Dasturchi",
    "Cristiano Ronaldo": "Futbolchi",
    "Elon Musk": "Tadbirkor",
    "Messi": "Futbolchi"
}

name = input("Ismni kiriting: ")

if name in professions:
    print(name, "ning kasbi:", professions[name])
else:
    print("Bu shaxs haqida ma'lumot topilmadi.")