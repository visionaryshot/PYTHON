number = int(input("Enter any five numbers: "))
if number >= 10000 and number <= 99999:
	num1 = number // 10000
	num2 = (number // 1000) % 10
	num4 = (number // 10) % 10
	num5 = number % 10
if num1 == num5 and num2 == num4:
	print("This is a palindrome.")
else:
	print("This is not a palindrome.")


