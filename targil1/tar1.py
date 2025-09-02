
def  get_penta_num(n):
    return (n*(3*n-1))/2
def pentaNumRange(n1,n2):
    return list(map(get_penta_num,range(n1,n2)))


