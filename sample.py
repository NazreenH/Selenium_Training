
def even_odd(start,stop):
    for num in range(start,stop):
        if num%2==0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")

even_odd(1,10)