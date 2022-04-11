#https://docs.python.org/3/library/exceptions.html

def divide(n1, n2):
    if n2 == 0:
        raise ValueError("N2 não pode ser zero.")
    return n1 / n2

print(divide(2, 0))



# def divide(n1, n2):
#     try:
#         return n1 / n2
#     except ZeroDivisionError as error:
#         print('Log: ', error)
#         raise

# try:
#     print(divide(10,0))
# except ZeroDivisionError as error:
#     print(error)