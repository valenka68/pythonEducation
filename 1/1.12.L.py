first_number = int(input())
second_number = int(input())
end = ((first_number % 10) + (second_number % 10)) % 10
middle = ((first_number // 10 % 10) + (second_number // 10 % 10)) % 10
beginning = ((first_number // 100) + (second_number // 100)) % 10
print(f'{beginning}{middle}{end}')