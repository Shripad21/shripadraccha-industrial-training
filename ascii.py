a='X'
print("The ascii value of X is",ord(a))
a='x'
print("The ascii value of x is",ord(a))

#Write a program compute quotient and remainder
s=4
r=8

q = s//r
print("Quotient: ", q)
r = s%r
print("Remainder", r)

#Write a program to swap numbers
a=10
b=20
temp=a
a=b
b=temp
print("A value after swapping is ",a)
print("B value after swapping is ",b)

#Write a program to Check Whether a Number is Even or Odd-
x=76

if (x % 2) == 0 :
    print("Number is Even ",x)
else :
    print("Number is Odd ",x)

#Write a program to Check whether an alphabet is vowel or consonant using if..else statement 
x='a'

if x in ('a','e','i','o','u') :
    print("The given Alphabet is vowel",x)
else :
    print("The given Alphabet is consonant",x)

#Write a program to calculate GST i.e. 18% on base price 34900/- 
gst = ((18/100) * 34900)

print("gst is ",gst)

#Write a program to calculate monthly simple intrest and compound intrest(5%/Month) on amount - 161258/-
p=453672
r=7
t=2

si=p*r*t*0.01

print("Si : ",si)


Amount = p * (pow((1 + r / 100), t))
ci = Amount - p 
print("Compound interest is", ci)

#Write a program to calculate monthly simple intrest and compound intrest(5%/Month) on amount - 161258/-
a=657843

e2=a/24

e4=a/48

emi2=e2+(0.07*e2)

emi4=e4+(0.07*e4)

print("EMI for 2 years with intrest 7%",emi2)

print("EMI for 4 years with intrest 7%",emi4)