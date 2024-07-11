"""
Решение 1 сложение строк:
never_string = "Я больше никогда не буду писать "
number_of_repetitions = int(input())
phrase = "\"" + input() + "\"!" + "\n"
print((never_string + phrase) * number_of_repetitions)

Решение 2 интерполяция строк:
number_of_repetitions = int(input())
phrase = input()
total_string = "Я больше никогда не буду писать \"%s\"!\n" % phrase
print(total_string * number_of_repetitions)
"""
number_of_repetitions = int(input())
phrase = input()
print(f'Я больше никогда не буду писать "{phrase}"!\n' * number_of_repetitions)