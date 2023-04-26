lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# lst = list(map(int, input("Enter elements: ").split()))
print(lst)

even = list(filter(lambda x: x % 2 == 0, lst))
print(even)

