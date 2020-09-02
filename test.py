with open('newbrain.txt','w+') as fp:
    #0 moves
    fp.write('11')
    for i in range(9):
        fp.write(",.1111111111")
    fp.write('\n')

    #1 move
    for i in range(9):
        fp.write(str(i))
        for j in range(9):
            if j == i:
                fp.write(",0.0")
            else:
                fp.write(",.125")
        fp.write('\n')
        
    #2 moves
    for i in range(9):
        for j in range(9):            
            if j != i:
                fp.write(str(i))
                fp.write(str(j))
                for a in range(9):
                    if a == i or a == j:
                        fp.write(",0.0")
                    else:
                        fp.write(",.1428571429")
                fp.write('\n')

    #3 moves
    for i in range(9):
        for j in range(9):
            for k in range(9):           
                if j != k and k != i and i != j:
                    fp.write(str(i)+str(j)+str(k))
                    for a in range(9):
                        if a == i or a == j or a == k:
                            fp.write(",0.0")
                        else:
                            fp.write(",.1666666667")
                    fp.write('\n')

    #4 moves
    for i in range(9):
        for j in range(9):
            for k in range(9): 
                for l in range(9):          
                    if j != k and k != i and i != j and l != j and l != k and l != i:
                        fp.write(str(i)+str(j)+str(k)+str(l))
                        for a in range(9):
                            if a == i or a == j or a == k or a == l:
                                fp.write(",0.0")
                            else:
                                fp.write(",.200")
                        fp.write('\n')

    #5 moves
    for i in range(9):
        for j in range(9):
            for k in range(9): 
                for l in range(9):  
                    for m in range(9):        
                        if j != k and k != i and i != j and l != j and l != k and l != i and m != i and m != j and m != k and m != l:
                            fp.write(str(i)+str(j)+str(k)+str(l)+str(m))
                            for a in range(9):
                                if a == i or a == j or a == k or a == l or a == m:
                                    fp.write(",0.0")
                                else:
                                    fp.write(",.250")
                            fp.write('\n')

    #6 moves
    for i in range(9):
        for j in range(9):
            for k in range(9): 
                for l in range(9):  
                    for m in range(9):   
                        for n in range(9):     
                            if j != k and k != i and i != j and l != j and l != k and l != i and m != i and m != j and m != k and m != l and n != i and n != j and n != k and n != l and n != m:
                                fp.write(str(i)+str(j)+str(k)+str(l)+str(m)+str(n))
                                for a in range(9):
                                    if a == i or a == j or a == k or a == l or a == m or a == n:
                                        fp.write(",0.0")
                                    else:
                                        fp.write(",.3333333333")
                                fp.write('\n')

    #7 moves
    for i in range(9):
        for j in range(9):
            for k in range(9): 
                for l in range(9):  
                    for m in range(9):   
                        for n in range(9): 
                            for o in range(9):    
                                if j != k and k != i and i != j and l != j and l != k and l != i and m != i and m != j and m != k and m != l and n != i and n != j and n != k and n != l and n != m and o != i and o != j and o != k and o != l and o != m and o != n:
                                    fp.write(str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o))
                                    for a in range(9):
                                        if a == i or a == j or a == k or a == l or a == m or a == n or a == o:
                                            fp.write(",0.0")
                                        else:
                                            fp.write(",.500")
                                    fp.write('\n')

    #8 moves
    for i in range(9):
        for j in range(9):
            for k in range(9): 
                for l in range(9):  
                    for m in range(9):   
                        for n in range(9): 
                            for o in range(9):
                                for p in range(9):    
                                    if j != k and k != i and i != j and l != j and l != k and l != i and m != i and m != j and m != k and m != l and n != i and n != j and n != k and n != l and n != m and o != i and o != j and o != k and o != l and o != m and o != n and p != i and p != j and p != k and p != l and p != m and p != n and p != o:
                                        fp.write(str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p))
                                        for a in range(9):
                                            if a == i or a == j or a == k or a == l or a == m or a == n or a == o or a == p:
                                                fp.write(",0.0")
                                            else:
                                                fp.write(",1")
                                        fp.write('\n')





# from fileinput import FileInput

# with FileInput(files=['test.txt'], inplace=True) as f:
#     for line in f:
#         line = line.rstrip()
#         words = line.split(",")
#         if words[0] == ".11":
#             newline = '0123' + ',' + '4567'
#             print(newline)
#             line = ','.join(str(x) for x in words)
            
#             #line = ",".join(str(x) for x in words)
#         print(line)

# fp = open("test.txt","r+")
# cpl = 8
# line_num = 0
# for line in fp:
#     words = line.split(',')
#     if words[0] == '.001':
#         fp.seek(cpl*line_num)
#         fp.write(".999"+','+".888"+','+'.222'+'\n')
#         break
#     line_num += 1
# fp.close()