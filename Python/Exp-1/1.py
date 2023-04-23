string = input("Enter your string: ")
string_check = string[::-1]
if string_check == string:
    print("Its a palindrome")
else:
    print("Its not a palindrome")
