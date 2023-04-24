lst = list(map(int, input("Enter elements: ").split()))
print(lst)

even = list(filter(lambda x: x % 2 == 0, lst))
print(even)

