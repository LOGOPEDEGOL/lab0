print("Введите часы и минуты натуральными числами от 0 до 24 для часов"
             " и от 0 до 60 для минут через один пробел")
inpt = input().split()

def Is_input_correct(inpt):
    output = []
    if len(inpt) != 2:
        output.append("Представьте время в формате часы <пробел> минуты")
    else:
        hours, minutes = inpt
        if not(hours.isdigit()) or not(minutes.isdigit()):
            output.append("Часы и минуты должны быть представлены натуральными числами")
        if hours.isdigit():
            if not (0 <= int(hours) <= 23):
                output.append("Часы должны быть от 0 до 23.")
        if minutes.isdigit():
            if not (0 <= int(minutes) <= 59):
                output.append("Минуты должны быть от 0 до 59.")

    if output:
        return "Введены недопустимые данные: " + " ".join(output)
    else:
        return ""

def daytime(hours):
    hours = int(hours)
    if 0 <= hours < 6:
        return "ночи"
    elif 6 <= hours < 12:
        return "утра"
    elif 12 <= hours < 18:
        return "дня"
    else:
        return "вечера"

def find_wordform(number, timeform):
    if timeform == "минуты":
        if 11 <= number % 100 <= 14:
            return "минут"
        elif number % 10 == 1:
            return "минута"
        elif 2 <= number % 10 <= 4:
            return "минуты"
        else:
            return "минут"
    elif timeform == "часы":
        if 11 <= number % 100 <= 14:
            return "часов"
        elif number % 10 == 1:
            return "час"
        elif 2 <= number % 10 <= 4:
            return "часа"
        else:
            return "часов"

def main():

    if Is_input_correct(inpt):
        return Is_input_correct(inpt)
    else:
        hours, minutes = inpt
    int_hours, int_minutes = int(hours), int(minutes)

    if int_hours == 0 and int_minutes == 0:
        return "полночь"
    if int_hours == 12 and int_minutes == 0:
        return "полдень"
    hour_for_text = int_hours
    if int_hours == 0:
        hour_for_text = 12
    elif int_hours > 12:
        hour_for_text = int_hours - 12
    if int_minutes == 0:
        result = (str(hour_for_text) + " " + find_wordform(int(hour_for_text), "часы") + " "
                  + daytime(hours) + " ровно")
    else:
        result = (
            str(hour_for_text) + " " +
            find_wordform(int(hour_for_text), "часы") + " " +
            str(int_minutes) + " " +
            find_wordform(int_minutes, "минуты") + " " +
            daytime(hours)
        )
    return result

if __name__ == "__main__":
    print(main())
