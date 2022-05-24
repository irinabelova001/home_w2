gr_ASP=1799
dr_ASP="6 июня"
gr=int(input("Введите год рождения А.С. Пушкина: "))
if gr_ASP==gr:
    dr=input("Введите день рождения Ф.С. Пушкина: ")
    if dr==dr_ASP:
        print("Верно")
    else:
        print("Не верный день рождения")
else:
    print("Неверный год рождения")
