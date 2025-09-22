m=int(input("enter the number: "))
#calculate factorial of given number using for loop
mul=1
for i in range(1,m+1):
  mul*=i
print("factorial of given number:",mul)


'''#calculate factorial of given number using while loop
mul=1
while m>0:
    mul*=m
    m-=1
print("factorial of given number:",mul)


#calculate facorials of n numbers
i=1
fact=1
while i<=m:
    fact*=i
    i+=1
    print(f"Factorial of {i-1}:{fact}")'''