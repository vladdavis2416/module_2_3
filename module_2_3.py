my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
lenght = len(my_list)
c = 0
while c<lenght and my_list[c]>-1:
    if my_list[c] == 0:
        c=c+1
    else:
        print(my_list[c])
        c=c+1

