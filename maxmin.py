num = int(input("Enter the number: "))
reversed_num = 0
max_digit = 0
min_digit = 9

while num != 0:
  digit = num % 10

  if(digit < min_digit):
    min_digit = digit
  if(digit > max_digit):
    max_digit = digit

  reversed_num = reversed_num * 10 + digit
  num //= 10

print(min_digit)
print(max_digit)