# def bharath():
#     print("danceing")
# def basu():
#     print("singing")
# bharath()
# basu()
# bharath()
# print("end")

# 1.function without return and without argument
# def add_two_numbers():
#     a = int(input("a="))
#     b = int(input("b="))
#     c = a+b
#     print(c)
# add_two_numbers()

#2.function with return and without argument
# def add_two_numbers():
#     a=int(input("a="))
#     b=int(input("b="))
#     c=a+b
#     return c
# res=add_two_numbers
# print(res)

# def add_two_numbers(a,b):
#     c = a+b
#     print(c)
# add_two_numbers(1,2)

# # function with return and with argument

# def add_two_numbers(a,b):
#     return a+b
# res=add_two_numbers(1,90)
# print(res)

# def fun(a,b,/,*,c,d):
#     print(a,b,c,d)
# fun(10,20,c=30,d=40)

# def demo(**args):
#     print(args)
# demo(name="bharath")
# def fun():
#     print(" i am bharath")
#     def inner_fun():
#         print(" i am basu")
#     inner_fun()
#     print("suiii")
        
# jolly = fun
# print("start")
# jolly()
# print("end")

# n=int(input("n:"))
# if n>0:
#     print("poistive")
# else:
#     print("negtive")

# n=int(input("n:"))
# if n<0:
#     print(f"{n} is negative")
# else:
#     print(f"{n}is not negative")
# n=int(input("n:"))
# if n%2==0:
#     print(f"{n}is even")
# else:
#     print(f"{n}is odd")
# age = 45
# if age > 18:
#     print("adult")
# elif age == 18:
#     print("just turned adult")
# else:
#     print("minor")
# b=100
# def fun():
#     b=200
#     def inner_fun():
#       print(b)
#     inner_fun()
# fun()
# print(b)
# b=500
# def fun():
#   a=200
#   print(a)
#   def inner_fun():
#     a=300
#     print(a)
#   inner_fun()
#   print(a)
# print(b)
# fun()
# print(b)


# n = int(input("enter="))
# if n%2==0 and n%3==0 and n%4==0:
#     print("divisable by 2,3,4")
# else:
#     print("not divisble")c

# class bharath:
#     def __init__(self,name):
#         self.name = name

# s1 = bharath("bharath")
# print(s1.name)       


# class employee:
#     def putdata(self):
#         self.id=int(input("entrer emp id"))
#         self.name=input("enter emp name")

#         self.salary=float(input("enter emp salary"))
#     def display(self):
#         print("emplyee id:",self.id)
#         print("employee name:",self.name)
#         print("employee salary",self.salary)
# a=employee()
# a.putdata()
# a.display()  

# class first:
#     x=50
# obj=first()
# print(obj.x)


# class faculty:
#     def putdata(bho):
#         bho.id=int(input("enter the id"))
#         bho.name=input("enter name")
#         bho.salary=float(input("enter faculty salary"))
#     def dispaly(self):
#         print("faculty id:",bho.id) 
#         print("faculty name:",bho.name)
#         print("faculty salary",bho.salary) 
# a=faculty()
# a.putdata()
# a.dispaly()          



# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def bharath(self):
#         print(f"hello,my name is {self.name} and i am {self.age} years old")
# person1 = person("arjun",30)
# person2 = person("megha",25) 

# person2.bharath()
# person1.bharath()

# class student:
#     name = "bharath"
# s1=student()
# print(s1)

# class car:
#     name = "bmw42"
#     model = 23
# s1 = car()
# print(s1.name)
# print(s1.model)

# class bharath:
#     def __init__(self,place,gender):
#      self.suooo=place
#      self.no=gender


#      def __str__(self):
#         return f"place: {self.suooo},gender: {self,no}"
# s1 = bharath("bk kuntii","male")
# s2=bharath("banglore","yelhanka")
# print(s1)

# class car:
#     name = "bmw"
# # showroom = car()
# print(car)

# class weakpasswordError(Exception):
#     def __init__(self, *args):
#         super().__init__(self,password,msg):
#         self.password = password
#         self.msg = msg
# try:

# import re
# date1 = '2026-Jan-01'
# reg_pat = r'\d{4}[-/]\d{3}[-/]\d{2}'

# reg_pat = r'^\d{4}-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-([0][1-9]|[12][0-9]|3[01])'
# res = re.fullmatch(reg_pat,date1)
# print(res)
# if res !=None:
#     print("valid date")
# else:
#     print("invalid date")

# import re

# date = input("Enter a date: ")

# patterns = {
#     "yyyy/MM/dd": r"^\d{4}/\d{2}/\d{2}$",

#     "yyyy-MM-dd": r"^\d{4}-\d{2}-\d{2}$",

#     "dd.MM.yyyy": r"^\d{2}\.\d{2}\.\d{4}$",

#     "yyyy.MM.dd": r"^\d{4}\.\d{2}\.\d{2}$",

#     "dd-Mon-yyyy": r"^\d{2}-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-\d{4}$",

#     "yyyy-Mon-dd": r"^\d{4}-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-\d{2}$"
# }

# found = False

# for format_name, pattern in patterns.items():
#     if re.fullmatch(pattern, date, re.IGNORECASE):
#         print("Valid Date")
#         print("Matched Format:", format_name)
#         found = True
#         break

#if not found:
    #print("Invalid Date")


# import re
# name = input("enter valid name:")
# regex = r'^[A-Za-z]+(?:[.][A-Za-z]+)*$'
# res = re.fullmatch(regex,name)
# if res != None:
#     print("valid number")
# else:
#     print("invalid number


# swapping of two numbers
# a = input(('a:'))
# b = input(('b:'))
# print(f'before swaping \n a={a}\tb={b}')
# c=a
# a=b
# b=c
# print(f'after swapping \n a={a}\tb={b}')

# num1 = int(input(('num1:')))
# num2 = int(input(('num2:')))
# sum = num1+num2
# print("the sum of given two numbers is",sum)

# num = int(input('enter the:'))
# sr = num**(1/2)
# print("the square root of the given number",sr)

# import math
# num = int(input("enter a number here:"))
# sr = math.sqrt(num)
# print("enter the square root of the given number is",sr)

# n=5int('',end='')
# for j in range(n):
#   for i in range(n):
#      print('*',end='')
#   print()

# for i in range(5):
#     for j in range(5):
#         if i+j <=5-1:
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()


# n=int(input("n:"))
# for i in range(n,0,-1):
#     print('*' *i)

# for i in range(5):
#    for j in range(5):
#     if i>=j:   
#       print("*",end='')
# #    for j in range(i,5):
# #       print("*",end='   ')
#    print()

# ch=65
# for i in range(4):
#     for j in range(4):
#         print(chr(ch),end=' ')
#         ch+=1
#     print()

# for i in range(4):
#     for j in range(4):
#         print(chr(65+i),end=' ')
#     print()

# n = int(input("n:"))
# spc=n-1
# str=1
# for i in range(n):
#     for j in range(spc):
#         print(' ',end=' ')
#     for k in range(str):
#         print('*',end=' ')
#     print()
#     spc-=1
#     str+=2

# n = int(input("n:"))
# for i in range(n):
#     for j in range(n-1-i):
#         print(' ',end=' ')
#     for k in range(2*i+1):
#         print('*',end=' ')
#     print()

# n = int(input('n:'))
# for i in range(n):
#     print(' '*(n-1-i)+'*'*(2*i+1))


# n = int(input('n:'))
# val=1
# for i in range(n):
#     print(' '*(n-1-i)+(str(val)+'')*(2*i+1))
#     val+=1

# n = int(input("n:"))
# spc=0
# str=2*n-1
# for i in range(n):
#     for j in range(spc):
#          print(' ',end=' ')
#     for k in range(str):
#          print('*',end=' ')     
#     print()
#     spc+=1
#     str-=2

# n = int(input('n:'))
# val=1
# for i in range(n):
#     print(' '*(i)+(str(val)+' ')*(2*(n-i)-1))
#     val+=1

# n = int(input('n:'))
# for i in range(n-1,-n,-1):
#      print(' '*abs(i)+'* '(n-abs(i)))


# n = int(input('n:'))
# for i in range(n):
#     for j in range(i+1):
#         print(1,end='')
#     print()


# food=input('enter the food you like(q to quit)')
# while not food =="q":
#     print(f'you like{food}')
#     food = input("enter another food you like(q for quit)")
# print("bye")

# online = False
# if online:
#     print("bharath is online")
# else:
#     print("bharath is offline")
  
# rows=int(input("enter the rows:"))
# col=int(input("enter the colums:"))
# symbol=input("enter the symbol")

# for i in range(rows):
#     for j in range(col):
#         print(symbol,end=' ')
#     print()
  

# n= int(input("enter the number:"))
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# for i in range(1,6):
#     for j in range(i):
#         print(j+1,end='')
#     print()

n = int(input("enter your name:"))
k=ord("A")
for i in range(n):
    for j in range(i+1):
        print(chr(k),end=" ")

        k+=1
    print()
        


    