# Chapter 6. Functions and Recursion in Python.

# Function.

# a=5
# b=20
# sum=a+b
# print(sum)

# a=10
# b=7
# sum=a+b
# print(sum)

# a=8
# b=2
# sum=a+b
# print(sum)


#Function definition.
# def calc_sum(a,b):   #Parameters
#     sum=a+b
#     print(sum)
#     return sum
# sum=calc_sum(20,20)
# sum=calc_sum(50,5)
# sum=calc_sum(90,10)
# print(sum)

# def str():
#     print("hello")
# str()


# def calc_avg(a=1,b=1,c=1):
#     a=float(input("Enter first number : "))
#     b=float(input("Enter first number : "))
#     c=float(input("Enter first number : "))
#     avg=(a+b+c)/3
#     print(avg)
# (calc_avg())

# fruits=["Apple","Banana","Mango","Papaya","Pomegranate"]
# def len_fruits():
#     print(fruits)
#     print(len(fruits))
# len_fruits()

# n=int(input("Enter a number: "))

# def calc_fact(m):
#     fact=1
#     i=1
#     for i in range(1,m+1):
#         fact*=i
#     return fact
# factorial=calc_fact(n)
# print(factorial)

# usd=float(input("Enter currency in USD: "))
# euro=float(input("Enter currency in Euro: "))
# pound=float(input("Enter currency in Pound: "))
# def con_curr():
#     NR=141.74*usd
#     NC=166.34*euro
#     NCR=190.60*pound
#     return NR,NC,NCR
# result=con_curr()
# print(result)

# def check_num(num):
#     if(num%2==0):
#         return "(Even)"
#     else:
#         return "(Odd)"
# num=int(input("Enter a number: "))
# test=check_num(num)
# print(test)


# Recursion:
# def show(n):
#     if(n==0):
#         return 
#     show(n-1)
#     print(n)

# show(10)


# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n* factorial(n-1)
# fact=factorial(6)
# print("The factorial is ",fact)


# n=int(input("Enter a number: "))
# def calc_sum(n):
#     # for i in range(1,n+1,1):
#         if(n==0):
#             return 0
#         else:
#             return  calc_sum(n-1) + n
# sum=calc_sum(n)
# print("Total sum = " , sum)

# def print_list(list,idx=0):
#     if(idx==len(list)):
#         return 
#     print(list[idx])
#     print_list(list,idx+1)
# list=[1,3,4,5,66,7,5]
# print_list(list)