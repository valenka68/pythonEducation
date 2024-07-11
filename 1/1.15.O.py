n = int(input()) * 60
m = int(input())
t = int(input())
time = (n + m + t) % (60 * 24)
hours = time // 60
minutes = time % 60
print(f'{hours:02}:{minutes:02}')

"""
hours = int(input())
minutes = int(input())
lag = int(input())

minutes = minutes + lag
hours = (hours + minutes // 60) % 24
minutes = minutes % 60

print(f'{hours:02d}:{minutes:02d}')
"""