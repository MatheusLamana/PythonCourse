# for p,r in enumerate(range(10, 1, -1)):
#     print(p,r)

for i in range(5):
    print(i, end = "")
    if i == 1:
        continue
else:
    print("end")


[x for x in range(0,10) if x % 2]