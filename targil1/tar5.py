from itertools import compress
def add_3_dicts(d1,d2,d3):
     keys=d1.keys()|d2.keys()|d3.keys()#כל המפתחות משלושת המילונים
     dicts=(d1,d2,d3)

     return dict(map(lambda k:(k,
                               tuple(dict.fromkeys(
                                   compress(map(lambda d:d.get(k),dicts),map(lambda d:k in d,dicts))
                               ))
                               ) ,keys))
#הקומפרס מחזיר רק את האיברים מהערכים במילון שהמיקום המקביל להם הוא אמת כלומר שקיים באמת מפתח כזה במילון
#print(add_3_dicts({'a':1,'b':2},{'a':1},{'b':5,'a':7}))