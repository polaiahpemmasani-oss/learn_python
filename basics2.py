# a = 9
# b = 'c.'
# c = "pemmasani"
# d = 20.5
# e = True


# #print(a,type(a))
# #print(b,type(b))
# # print(c,type(c))
# # print(d,type(d))
# # print(e,type(e))

# # a=int(input("Enter your value:"))
# # # print(a,type(a))
# # b=int(input("Enter your value:"))
# # c=a+b
# # d=a/b
# # print(c,type(c))
# # print(d,type(d))
# # print(a+b)
# s=input("enter your value:")
# print(s.upper())
# # print(s[0],s[5],s[7])
# # print(s[:3])
# # print(s[3:])
# # print(s[1:5:2])
# # print(s[0:10:2])
# # print(s[::])
# # print(s[::-1])
# print(s[::2])
# print(s[::-2])

ls=['p',0,'t',6,9,0,'u']
tp=('p',0,'t',6,9,0,'u')
st={'p',0,'t',6,9,0,'u'}

# print(type(ls),ls,id(ls))
# ls.append(120)
# print(ls,id(ls))
# print(type(tp),tp,id(tp))
# tp.append(120)
# print(tp)
# print(st)
# ls.append([1,2,4])
# print(ls)
# ls.extend([1,2,4])
# print(ls)
# k=ls.count(0)
# print(k)
# d=ls.index(2)
# print(d)
# ls.insert(0,89)
# print(ls)
# ls.pop(1)
# print(ls)
# ls.remove(0)
# print(ls)
# # ls.reverse()
# print(ls)

# print(ls[::3])
# print(ls[3::])
# print(ls[:3:])
# print(tp[::-1])

# a=int(input("enter the value:"))
# if a>10 and a<30 :
#     print("your given value is greter than 10 to 30")
# elif a>5 and a<2 :
#     print("your given value is greter than 5 to 2")
# elif a==2 or a==0 :
#      print("your given value is 0 or 2")
# else :
#      print("your given value",a)
# print(len('5225'))
# ls=['f',0,4,'g','y','h','u',8,]
# for i in range(len(ls)):
#     print(i,ls[i])     
# 
# i = int(input("enter the value"))
# while i!=20:
#     print('i am in while loop')
#     i=int(input("enter the value"))

def addf( a,b,c):
    try:
        d=0
        l =0
        sum=a+b+c
        d=a/b
        l=a*c
    except ZeroDivisionError:
        print("zero division error")
        d=float('inf')
    except TypeError:
        print('type error')
        sum=str(a)+str(b)+str(c)
    except UnboundLocalError:
        l=a*c
    finally:
        print('i am in final')
    return sum,d,l

k,l,m=addf(5,0,"g")
print(k,l,m)

