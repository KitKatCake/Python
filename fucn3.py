from fn import F, _, op

from operator import add, mul, sub

# f = F(add,1)(10)

# print(f)
from fn.op import apply, flip, foldr, call

# f = F(add,1)<<F(mul,100)
#
#
# print(list(map(f,[0,1,2])))
#
#
#
# print(list(map(F()<<str<<(_**2)<<(_+1),range(3))))




# func = F()>>(filter,_<6)>>sum
#
# print(func(range(10)))
#
#
print(apply(add,[1,2]))

print(flip(sub)(20,10))

# print((sub)(20,10))



# folder = op.foldl(_*_,1)

# folder = op.foldl(_*_,1)
#
# print(op.foldl(_+_)([1,2,3]))
#
# print(folder([1,2,3]))
#
# print(foldr(call,0)([lambda x:x**2,lambda y:y+10]))
#
# print(foldr(call,10)([lambda x:x**2,lambda y:y+10]))



from fn import recur

@recur.tco

def even(x):
    if x==0:
        return False,True
    return odd,(x-1,)

@recur.tco
def odd(x):
    if x==0:
        return False,False
    return even,(x-1,)

print(even(100000))

print(odd(100000))




