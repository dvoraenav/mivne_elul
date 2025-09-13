from functools import reduce
#sec1
y=lambda x:x/2+2
l=list(range(1,1001))
even=[ x for x in l if x%2==0]
odd=[x for x in l if x%2!=0]

running_product = lambda k, sub: reduce(
    lambda st, x: (st[0]*x, st[1] + [st[0]*x]),
    sub,
    (k, [])
)[1]

running_sum=lambda odd_:reduce(
    lambda st,pair:(st[0]+pair[0],st[1]+[y(st[0]+pair[0])+pair[1]],
                    ),
    zip(odd_,odd_[1:]),#(current,next)
    (0,[])
)[1] #st[1] is the list of results
# st[0] is the Cumulative amount
#pair[o] is the current item
#pair[1] is the next item

#sec2
#for sub list and not all the list because it is too long but we can remove the slice
product,sum_=map(lambda f:f(),
                [
  lambda : running_product(1,even[0:8]),
  lambda :running_sum(odd[0:8]),]
)
print(f"product:{product}")
print(f"sum:{sum_}")

#sec3
sum1,sum2=map(lambda f:reduce(lambda acc,x:x+acc,f(),0),
              (
                  lambda: running_product(1,even[0:8]),
                  lambda: running_sum(odd[0:8]),
              )
        )
print(f"sum1:{sum1}")
print(f"sum2:{sum2}")





