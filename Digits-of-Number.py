# All digits
n=int(input("Enter number: "))
while n>0:
    d=n%10
    print(d)
    n//=10
# Even digits
n=int(input("Enter number: "))
while n>0:
    d=n%10
    n//=10
    if d%2==0:
        print(d)
# Odd digits
n=int(input("Enter number: "))
while n>0:
    d=n%10
    n//=10
    if d%2!=0:
        print(d)
# Sum of digits
n=int(input("Enter number: "))
s=0
while n>0:
    d=n%10
    n//=10
    s+=d
print("Sum of digits:",s)
# Largest digit
n=int(input("Enter number: "))
ld=0
while n>0:
    r=n%10
    if ld<r:
        ld=r
    n//=10
print("The Largest Digit is :",ld)
# Number of odd digits
