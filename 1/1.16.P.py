storehouse = int(input())
shop = int(input())
speed = int(input())
distance = ((shop - storehouse) / speed)
print(f'{distance:.2f}')

#"{:.2f}".format(distance)