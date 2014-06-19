def multiout(n):
    F = []
    for i in range(n):
        F.append(open('f%s.txt'%(i),'w+'))
    return F         
   
