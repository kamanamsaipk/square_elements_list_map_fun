numbers_list = [4,2,9,5,7]
def square_number(numbers_list):
    return list(map(lambda x:x**2,numbers_list))
squaring_numbers = square_number(numbers_list)
print(squaring_numbers)