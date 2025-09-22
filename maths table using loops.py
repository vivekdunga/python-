n=int(input("Enter number:"))
m=int(input("Enter number:"))
#maths tables printing using while loop     
i=0
while i<n:
    i+=1 
    j=0
    while j<m:
        j+=1
        print(f"{i}x{j}={j*i}")
#maths tables printing using for loop  
'''for i in range(1,n+1):
    for j in range(1,m+1):
        print(f"{i}x{j}={i*j}")'''