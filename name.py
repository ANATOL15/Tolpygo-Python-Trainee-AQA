Name1 = str(input("Введите имя: "))

if Name1 == "Вячеслав":
    print('Привет, Вячеслав')
elif Name1.islower() == 'вячеслав':
    print('Привет, Вячеслав')

elif Name1.upper() == 'ВЯЧЕСЛАВ':
    print('Привет, Вячеслав')
else:
    print("Нет такого имени")
