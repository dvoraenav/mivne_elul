"#sec1"
def double(x):
    return x * 2
def square(x):
    return x * x
def inv(x):
    return 1 / x if x != 0 else None
funcs=[double,square,inv]

"#sec2"
def fun_dict(funcs,nums):
#זיפ בין שם הפונקציה לבין התוצאה של הפעלת הפונקציה על כל ערך מהאוסף
    return dict(zip(map(lambda f:f.__name__,funcs),map(lambda f:list(map(f,nums)),funcs)))
print(fun_dict(funcs,(1,2,3)))

