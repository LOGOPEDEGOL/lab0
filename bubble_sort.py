import random
s = [random.randint(0, 99) for i in range(10)]
print(s)

def bubble_sort(s):
    obsh_kolvo_perest = 0
    sravn = 0
    kolvo_perest = -1
    while kolvo_perest != 0:
        kolvo_perest = 0
        for i in range(len(s)-1):
            if s[i] > s[i+1]:
                s[i],s[i+1] = s[i+1],s[i]
                kolvo_perest += 1
                obsh_kolvo_perest += 1
            sravn += 1

    return s,obsh_kolvo_perest,sravn

print(bubble_sort(s))
#ЭТО НЕ ГОТОВЫЙ КОД, ЭТО ОТДЕЛЬНЫЙ КОД ТОЛЬКО С ПРИМЕРОМ РАБОТЫ СОРТИРОВКИ ПУЗЫРЬКОМ
