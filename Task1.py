month,day  = map(int, input("Введите дату (месяц и день через пробел): ").split())
year_time = ["Зима","Весна","Лето","Осень"]
def is_date_correct(day, month):

    output = []
    max_day_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if not (1 <= month <= 12):
        output.append("Месяц должен быть от 1 до 12.")
    else:
        if not (1 <= day <= max_day_in_month[month - 1]):
            output.append("День указан неверно для указанного месяца.")

    if output:
        return "Введены недопустимые данные: " + " ".join(output)
    else:
        return False


if not(is_date_correct(day, month)):
    print(year_time[(month // 3) % 4])
