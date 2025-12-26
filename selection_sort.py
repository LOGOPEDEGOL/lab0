import random
s = [random.randint(0, 99) for _ in range(10)]
print(s)

def selection_sort(s):
    for i in range(len(s)-1):
        s[s.index(max(s[:len(s) - i]))],s[len(s) - 1 - i] = s[len(s) - 1 - i],s[s.index(max(s[:len(s) - i]))]
    return s

print(selection_sort(s))

#ЭТО НЕ ГОТОВЫЙ КОД, ЭТО ОТДЕЛЬНЫЙ КОД ТОЛЬКО С ПРИМЕРОМ РАБОТЫ СОРТИРОВКИ ВЫБОРОМ
