inpt  = input("Введите дату (месяц и день через пробел): ").split()
year_time = ["Зима","Весна","Лето","Осень"]
def is_date_correct(inpt):
    output = []
    max_day_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if len(inpt) != 2:
        output.append("Представьте дату в формате месяц <пробел> день")
    else:
        month, day = inpt
        if not(month.isdigit()) or not(day.isdigit()):
            output.append("месяц и день должны быть представлены натуральными числами")
        else:
            month, day = map(int, inpt)
            month,day = int(month),int(day)
            if not (1 <= month <= 12):
                output.append("Месяц должен быть от 1 до 12.")
            else:
                if not (1 <= day <= max_day_in_month[month - 1]):
                    output.append("День введён неверно для указанного месяца.")

    if output:
        return "Введены недопустимые данные: " + " ".join(output)
    else:
        return False


if not(is_date_correct(inpt)):
    month,day = map(int,inpt)
    print(year_time[(month // 3) % 4])
else:
    print(is_date_correct(inpt))
