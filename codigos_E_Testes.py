def simple_interest(p,t,r):
    print('The simple Principal is ', p)
    print('The time Period is ', t)
    print('The Rate of interest is ', r)
    si = (p * t * r) / 100
    print('The simple interest is ', si) #a taxa de juros é.
    return si

simple_interest(8,6,8)

#finding (Compound Interest)
# def compound_interest(principal, rate, time):
#     Amount = principal * (pow(( 1 + rate / 1000), time))
#     ci = Amount - principal
#     print("Compound interest is", ci)

# compound_interest(10000, 10.25, 5)

# print all prime no's in an interval.
# start = 11
# end = 25
# for i in range(start, end +1 ):
#     if i > 1:
#         for j in range(2, i):
#             if (i % j == 0):
#                 break
#             else:
#                 print(i)
