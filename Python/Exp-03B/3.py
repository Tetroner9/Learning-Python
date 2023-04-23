numbers = [15, 19, 26, 39, 52, 65, 78, 91, 104, 117, 130]

divisible_by_19_or_13 = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))

print(divisible_by_19_or_13)