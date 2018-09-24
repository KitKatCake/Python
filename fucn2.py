from fn import recur

# @recur.tco
# def fact(n,acc=1):
#     if n==0:
#         return False,acc
#     return True,(n-1,acc*n)
#
# print(fact(5,1))


from fn.iters import take,drop,map

from operator import add

from fn import Stream

# f = Stream()
#
# fib = f<<[0,1]<<map(add,f,drop(1,f))
#
# print(list(take(10,fib)))
#
# print(fib[20])
#
# print(list(fib[30:35]))

from fn.func import curried
from fn.op import zipwith


@curried

def sum5(a,b,c,d,e):
    return a+b+c+d+e

print(sum5(1)(2)(3)(4)(5))

print(sum5(1,2,3)(4,5))

from itertools import repeat


print(list(zipwith(_+_)([0,1,2],repeat(10))))








