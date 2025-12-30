import random
s = [random.randint(0, 99) for _ in range(10)]
print(s)

def insertion_sort(s):
    for i in range(1, len(s)):
        j = i - 1
        while j >= 0 and s[j] > s[i]:
            s[j + 1] = s[j]
            j -= 1
        s[j + 1] = s[i]

print(insertion_sort(s))
#ЭТО НЕ ГОТОВЫЙ КОД, ЭТО ОТДЕЛЬНЫЙ КОД ТОЛЬКО С ПРИМЕРОМ РАБОТЫ СОРТИРОВКИ ВСТАВКАМИ
