# """
# datatypes
# datastructure
# conditions -if while for
# function
# OOPS -classes --no need DE
# """

# #int char float bool string

# # a = 5
# # b = 'P.'
# # c = "polaiah"
# # d = 10.5
# # e = True

# # print(a,type(a))
# # print(b,type(b))
# # print(c,type(c))
# # print(d,type(d))
# # print(e,type(e))


# # x = a+e
# # print(x)
# # w = a+d
# # print(w)
# # y  = b+c
# # print(y)
# # # o = a+c
# # # print(o)

# # print(a/e)
# # print(b/c)


# ################
# # a = input("Enter your value:")
# # print(a,type(a))

# # a = int(input("Enter your value:"))
# # b = float(input("Enter your float value:"))
# # c = bool(input("Enter your value:"))
# # print(a,type(a))
# # print(b,type(b))
# # print(c,type(c))

# s = input("enter the value and check the count :")
# # print(dir(s))
# # print(len(s))
# # # print(sizeof(s))

# # z = s.upper() ##
# # print(z)

# # x = s.startswith("P")
# # print(x)

# # print(s[0],s[3])

# k = s[0:4] ## start:END:STEP  -- for loop -- deafult step =1
# # print(k)
# # print(s[0:4:2])  # raange 0<= <4

# # print(s[:5])  ## start with zero default

# # print(s[1:])  ## end is last value d=by default

# print(s[::-1])  ## step negative means index in negatives ->  -n,-n+1 ...... -3.-2.-1

# print(s[-3:-1:1])

# print(s[-5:-1:1])

### arayss - basics datastructure - list ,tuple,set, dict
# 

# ls = ['a',2,'f','g',5,10.5]  #or list('a',2,'f'.'g',5,10)   -- mutable 
# tp = ('a',2,'f','g',5,10)  #or tuple('a',2,'f'.'g',5,10)   -- immutable
# st = {'a',2,'f','g',5,10,5,10} #or set('a',2,'f'.'g',5,10.5,10)
# dt = {"a":1223,"c":"abcd","o":20.5}  ##or dictt((),())

# print(type(ls),ls,id(ls))
# ls.append(120)
# print(type(ls),ls,id(ls))
# print(type(tp),tp,id(tp))
# tp = tp + ("120",120)
# print(type(tp),tp,id(tp))
# print(type(st),st,id(st))
# print(type(dt),dt,id(dt))


# ls.append([1,2,1])
# print(ls)
# ls2 = ls.copy()
# print(id(ls2)),print(id(ls))
# print(ls.count(5))
# ls.extend([1,2,1])
# print(ls)
# print(ls.index(10.5))
# print(ls)
# ls.insert(0,1000)
# print(ls)
# ls.pop(2)
# print(ls)
# ls.remove(10.5)
# print(ls)
# ls.reverse()
# print(ls)
# ls.sort()
# print(ls)

# ls.clear()
# print(ls)

# print(tp.count(5))
# print(tp.index(10))

# print(st)
# st.pop()
# print(st)
# st.remove('f')
# print(st)
# st.pop()
# print(st)

# print(dt.items())

# a = int(input(" value is :"))
# if a > 10 and a < 20:
#     print("your value is greater than 10 to 20")
#     print(a)
# elif a > 5 and a < 10 :
#     print("your value is greater than 5 to 10")
# elif a == 2 or a == 0:
#     print("your value is greater than 2 or 0")
# else:
#     print("a value is",a)

ls = [1,3,4,'f','j']
# for i in ls:
#     print(i)

# for i in range(-1,-5,-1):
#     print(i)

# for i in range(5):
#     print(i)
# print(len(ls))
# for i in range(len(ls)):
#     print(i,end="  ")
#     print(ls[i])

# a = int(input(" value is :"))
# while a != 5:
#     print(a)
#     print("I am in while loop")
#     a = int(input(" value is :"))


# def add():
#     print("helllo i m in fun add")
#     return "Returing"

# k = add()
# print(k)

# def add(a: int,b: int):
#     print("helllo i m in fun add")
#     return a+b

# k = add(3,2)
# print(k)

# def add(a: int =10,b: int =20):
#     print("helllo i m in fun add")
#     return a+b

# k = add(3)
# print(k)
# k = add(b = 3)
# print(k)

# def add(*arg):
#     sum = 0
#     print(arg)
#     for i in arg:
#         sum = sum+i
#     return sum
# k = add(1,4,6,8,9)
# print(k)

# def add(**kwarg):
#     sum = 0
#     print(kwarg)
#     for key,value in kwarg.items():
#         sum = sum+value
#     return sum
# k = add(k=5,l=10,z=20)
# print(k)

# def add(a,b):
#     try:
#         print("I am in try")
#         s = a/b
#     except Exception as e:
#         print(e)
#         s = float('inf')
#     return s
# k = add(3,3)
# print(k)

# def add(a,b):
#     try:
#         print("I am in try")
#         s = a/b
#     except ZeroDivisionError:
#         print('ZeroDivisionError')
#         s = float('inf')
#     except TypeError:
#         print('value errror')
#         s = 0
#     finally :
#         print("always executing")
#     return s

# try:
#     k = add(3)
#     print(k)
# except TypeError:
#     k = add(1,b='j')
#     print(k)

# file = open("test2.txt",'w')
# file.write("I am wrttin g line in text 2")
# file.close()

# with open("test3.txt",'w') as file:
#     file.writelines("I am at 1m I am at 2")

# with open("test2.txt",'r') as file:
#     print(file.readlines())