num=5
for i in range(num):
    if i == 0 or i == (num-1):
        print('*'*num)
    else:
        print(' '*(num-i-1)+"*")
