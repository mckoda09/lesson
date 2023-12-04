def lastsecond(num):
  if (num>-9 and num<10):
    return -1
  else:
    temp=num/10
    rem=temp%10
    return int(rem)

print(lastsecond(int(input("Enter number: "))))