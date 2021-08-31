#if

if 20>5:
    print("20 is greater ")



#if else 

a=10
n=int(input("Enter number "))

if a>n:
    print(a,"is greater ")
else :
    print(a,"is smaller")



#elif

if n>0:
    print("Positive number ")
elif n==0 :
    print("Number is zero")
else :
    print("Negative number")

#for loop
number=[1,2,3,6,5,6,7,8,9]
sum=0
num=0
for num in number:
    sum=sum+num
    print("sum : ",sum)

#range ()
print("Range Seque ",range(20))
print("Range sequanse allitems is ",list(range(20)))

#while loop

s=0
i=1
b=100
while i<=b:
    s=s+i
    i=i+1
print("sum = ",s)

#break  

if 10<5:
    pass

for b in "hello python" :
    if b=='l':
        break 
    print(b)


#continue

for b in "hello python" :
    if b=='l':
        continue
    print(b)

#pass 
list = [1,2,3,4,5]  
flag = 0  
for i in list:  
    print("Current element:",i,end=" ");  
    if i==3:  
         pass;  
         print("\nWe are inside pass block\n");  
         flag = 1 
    if flag==1:  
            print("\nCame out of pass\n");  
            flag=0;  
