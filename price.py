def get_summ(one, two,delimiter = '&'):
    str_one = str(one)
    str_two = str(two)
    sum_one_two = str_one+delimiter+str_two
    return sum_one_two

test_func = get_summ("Learn", "Python")
print (test_func)
print (test_func.upper())

def format_price(price):
    price_int = int(price)
    result = "Цена: "+ str(price_int)+ " руб."
    return result

test_price = format_price(56.24)
print(test_price)