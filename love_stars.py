for row in range(5):
    for col in range(7):
        if (row==0 and (col%3)!=0) or (row==1 and (col%3)==0) or ((row-col) == 1) or ((row+col)==7):
            print("*",end='')
        print(" ",end='')
    print("\n")