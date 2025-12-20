vvod1 = input("Введите первое время (часы <Пробел> минуты): ").split()
vvod2 = input("Введите второе время (часы <Пробел> минуты): ").split()


def Is_input_correct(vvod1, vvod2):
    output = []

    if len(vvod1) != 2 or len(vvod2) != 2:
        output.append("Введите два времени, каждое в формате: часы пробел минуты.")
        return "Введены недопустимые данные: " + " ".join(output)

    vvod = vvod1 + vvod2
    for x in vvod:
        if not x.isdigit():
            output.append("Вводите только целые числа.")
            return "Введены недопустимые данные: " + " ".join(output)

    hours1, minutes1 = map(int, vvod1)
    hours2, minutes2 = map(int, vvod2)

    if not (0 <= hours1 <= 23) or not (0 <= hours2 <= 23):
        output.append("Часы должны быть от 0 до 23.")
    if not (0 <= minutes1 <= 59) or not (0 <= minutes2 <= 59):
        output.append("Минуты должны быть от 0 до 59.")

    if output:
        return "Введены недопустимые данные: " + " ".join(output)
    else:
        return ""


error = Is_input_correct(vvod1, vvod2)

if error:
    print(error)
else:
    hours1, minutes1 = map(int, vvod1)
    hours2, minutes2 = map(int, vvod2)

    time1 = hours1 * 60 + minutes1
    time2 = hours2 * 60 + minutes2

    if time2 >= time1:
        diff = time2 - time1
    else:
        diff = 24 * 60 - time1 + time2

    res_hours = diff // 60
    res_minutes = diff % 60

    print("Разница:"+ str(res_hours) +  "часов" + str(res_minutes) + "минут")
