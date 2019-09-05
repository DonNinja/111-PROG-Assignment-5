# Formula: n_sum = n1 + n2 + n3
# n1 er talan í staki n - 1, n2 er talan í staki n - 2 og n3 er talan í staki n - 3
# þannig ef 0, 2, 6, 7 þar sem n = 7, þá er n = 7, n1 = 6, n2 = 2 og n3 = 0

n = int(input("Enter the length of the sequence: ")) # Do not change this line
n1 = 1
n2 = 0
n3 = 0
n_sum = 0

for i in range(0, n):
    n_sum = n1 + n2 + n3
    if i == 1:
        n3 = 0
    else:
        n3 = n2
    n2 = n1
    n1 = n_sum
    print(n_sum, end=", ")