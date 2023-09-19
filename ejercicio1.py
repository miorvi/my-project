fizz = "FIZZ"
buzz = "BUZZ"
for i in range(100):
    div_3 = (1 + i) % 3 == 0
    div_5 = (1 + i) % 5 == 0

    if div_3 and div_5:
        print(fizz + buzz)
    elif div_3:
        print(fizz)
    elif div_5:
        print(buzz)
    else:
        print(i)