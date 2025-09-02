def sum_digit(num):
    try:
     n=abs(int(num))
    except(ValueError, TypeError):
        return "invalid input"
    return sum(map(int,str(n)))


if __name__ == '__main__':
    number=input("enter a integer number: ")
    print(sum_digit(number))
