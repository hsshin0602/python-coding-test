n = 1260
count = 0

coin__type = [500, 100, 50, 10]

for coin in coin__type:
    count += n // coin
    n %= coin
print(count)
