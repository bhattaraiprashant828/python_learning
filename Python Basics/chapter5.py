#  Chapter.5 Loops in Python

#  Practice Qns Using While loops.
# 1.Print numbers from 1 to 100.
# a=1
# while a<=10:
    # print(a)
    # a=a+1

# Q.2
# a=10
# while a>=1:
#  print(a)
#  a=a-1

# Q.3
# i=1
# n=int(input("Enter a number: "))
# while i<=10:
#     print(n*i)
#     i=i+1

# Searching......
# i=0
# tup=(1,4,9,16,25,36,49,64,81,100)
# x=int(input("Enter any number: "))
# while i< len(tup):
#     if(tup[i]==x):
#         print(f"Found at idx",(i))
#         break
#     elif(tup[i]!=x):
#         print("Not found at idx",i)
        
#     i=i+1

# For loops.
# Practice Questions.

# idx=0
# list=[1,4,9,16,25,36,49,64,81,100,49]
# x=49
# for i in list:
#     if(i==x):
#         print("found at idx",idx)
#         # break
#     else:
#         print("not found")
#         idx+=1

# Range  function
# Methods of defining Range function.

# for i in range(10): #range(stop)
#     print(i)
# for i in range(2,10): #range(start,stop):
    # print(i)
# for i in range(2,10,2): #range(start,stop,step)
#     print(i)
    

# Practice Qns using For and range 
# n=int(input("Enter a number: "))
# for i in range(1,11):
#     print(n*i)

# for i in range(100,0,-1):i
#     print(i)

# Use of pass.
# for i in range(5):
    # pass#(Used to skip work.)

# print("Homework")


# Practice

# Using while loop.
# i=1
# sum=0
# n=int(input("Enter a number: " ))
# while i<=n:
#     print(i)
#     sum=sum+i
#     i+=1
# print("Total sum=",sum)

# # Using for loop.
# sum=0
# n=int(input("Enter a number: " ))
# for i in range(1,n+1,1):
#     sum+=i
# print("Total sum = ",sum)

# fact=1
# n=int(input("Enter a number: " ))
# for i in range(1,n+1):
#     fact*=i
# print(f"The factorial of {n} is = " ,fact)