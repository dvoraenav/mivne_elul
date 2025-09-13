from functools import reduce
from operator import mul, add

#sec1
def pow_(exponent):
    def result(base):
        return base ** exponent
    return result

#sec2

def exponent_(n):

    return map(pow_, range(n))

# --- main ---
n    = int(input("Enter number of powers: "))
base = int(input("Enter base: "))

res = exponent_(n)
print(type(res))                          # <class 'map'>
print(tuple(f(base) for f in res))

#sec3

taylor_exp_via_pow = lambda x, n: reduce(
    add,
    map(lambda k: pow_(k)(x) / reduce(mul, range(1, k+1), 1),
        range(0, n+1)),
    0.0
)
print(taylor_exp_via_pow(1, 10))