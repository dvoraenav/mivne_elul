from datetime import datetime,timedelta
def date_step(str_, n, step, fmt="%Y-%m-%d"):
    start=datetime.strptime(str_,fmt)
    return list(map(lambda k:(start+timedelta(days=k*step)).strftime(fmt),
                    range(n)
                    ))
print(date_step("2025-09-09", 5, 2))
