# s = x+x^2+x^3+x^4+...+x^n
x = int(input("Enter a number: "))
n = int(input("Enter a power: "))
s = 0
for i in range(1,n+1):
    s = s+(x**i)
print("Sum of series:",s)

# s = 1-1/3+1/5-1/7+1/9-1/11+...+1/n
n = int(input("Enter odd number: "))
f,s=0,0
for i in range(1,n+1,2):
    if f==0:
        s+=1/i
        f=1
    else:
        s-=1/i
        f=0
print(s)

# s = 1/2+3/2+...+n/2
n = int(input("Enter a number: "))
s = 0
for i in range(1,n+1,2):
    s+=i/2
print("Sum of series:",s)

# s = x+x/3+x/5+...+x/n
x = int(input("Enter a number: "))
n = int(input("Enter an odd number: "))
s = 0
for i in range(1,n+1,2):
    s+=x/i
print("Sum of series:",s)

# s = x/x^2+x/x^4+x/x^6+x/x^8+...+x/x^n
x = int(input("Enter a number: "))
n = int(input("Enter another number: "))
s = 0
for i in range(1,n+1,2):
    s+=x/(x**2)
print("Sum of series:",s)

# s = 1-1/x+1/x^2-1/x^3+1/x^4-1/x^5+...+1/x^n
x = int(input("Enter a number: "))
n = int(input("Enter an odd number: "))
s = 1
for i in range(1,n+1):
    if i%2==0:
        s+=1/(x**i)
    else:
        s-=1/(x**i)
print("Sum of series:",s)

# s = 1+2-2^2+2^3-2^4+...+2^n
n = int(input("Enter a number: "))
s = 1
for i in range(1,n+1):
    if i%2==0:
        s-=2**i
    else:
        s+=2**i
print("Sum of series:",s)

# s=1+1/1!+2/2!+...+n/n!
## Simple for loop
n=int(input("Enter number: "))
s,fact=1,1
for i in range(1,n+1):
    fact*=i
    s+=i/fact
print("Sum of series:",s)
## Nested for loop
n=int(input("Enter number: "))
s=1
for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact*=j
    s+=i/fact
print("Sum of series:",s)

# s=1!+2!+3!+...+n!
n=int(input("Enter number: "))
s,fact=0,1
for i in range(1,n+1):
    fact*=i
    s+=fact
print("Sum of series:",s)

# s=1/1!+2/2!+3/3!+...+n/n!
n=int(input("Enter number: "))
s,fact=0,1
for i in range(1,n+1):
    fact*=i
    s+=i/fact
print("Sum of series:",s)

# s=1!+2^2/2!+...+n^n/n!
## Simple for loop
n=int(input("Enter number: "))
s,fact,p=0,1,1
for i in range(1,n+1):
    p=i**i
    fact*=i
    s+=p/fact
print("Sum of series:",s)
## Nested for loop
n=int(input("Enter number: "))
s=0 
for i in range(1,n+1):
  fact=1
  for j in range(1,i+1):
      fact*=j
  s=s+i**i/fact
print("Sum of series:",s)

# s=1-2*3/3!+3*4/4!-4*5/5!+...+(n-1)n/n!
n=int(input("Enter number: "))
s,f=0,0
for i in range(2,n+1):
    fact=1
    for j in range(2,i+1):
        fact*=j
    if f==0:
        s+=((i-1)*i)/fact
        f=1
    else:
        s-=((i-1)*i)/fact
        f=0
print("Sum of series:",s)

# s=1+(1+2)+(1+2+3)+(1+2+3+n)+...+(1+2+3+4+...+n)
n=int(input("Enter number: "))
s,s2=0,0
for i in range(1,n+1):
  for j in range(i,i+1):
    s2+=i
  s+=s2
print("Sum of series:",s)

# 1+1/x+1/x2+1/x3+...
s=1
x=int(input('Enter x: '))
n=int(input('Enter n: '))
for i in range(1,n+1):
    s+=1/(x**i)
print('Sum:',s)

# (x^2)/2!+(x^3)/3!+(x^4)/4!+...
s,fact=0,1
x=int(input('Enter x: '))
n=int(input('Enter n: '))
for i in range(2,n+1):
    fact*=i
    s+=x**i/fact
print('Sum:',s)
