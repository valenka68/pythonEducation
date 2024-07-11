product_name = input()
priсe = int(input())
weight = int(input())
money = int(input())
total = priсe * weight
change = money - total
print("Чек")
print("%s - %sкг - %sруб/кг" % (product_name, weight, priсe))
print("Итого: %sруб" % total)
print("Внесено: %sруб" % money)
print("Сдача: %sруб" % change)