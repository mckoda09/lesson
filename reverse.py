num = int(input("Enter the number: "))
reversed_num = 0

while num != 0:
  digit = num % 10
  reversed_num = reversed_num * 10 + digit
  num //= 10

print(reversed_num)
reversed_num=str(reversed_num)

i = 0
while i != len(reversed_num):
  print(reversed_num[i])
  i += 1