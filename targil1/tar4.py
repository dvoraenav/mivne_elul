import math

#sec1
def prime(n):
    if n<2:return False     #1 הוא לא נחשב ראשוני
    if n%2==0:return n==2   #לסנן זוגיים  ורק 2 נחשב לראשוני

    return not any (map(lambda x:n%x==0,range(3,math.isqrt(n)+1,2)))  #ראשוני הוא אחד כזה שלא מתחלק באף מספר שונה מעצמו ומ1 - בודק אי זוגי
#sec2
def twin_prime(n):
    try:
        n = int(n)
    except(ValueError, TypeError):
        return "invalid input"
    if not prime(n):
        return "invalid input"
    if prime(n+2):return n+2
    if prime(n-2):return n-2

#sec3
def dict_prime(n):
    return dict(map(lambda p:(p,twin_prime(p)),filter(lambda p:prime(p),range(2,n+1))))
#אם אין תאום זה ישים None
print(dict_prime(11))
