def selSort(L):
    '''Assumes that L is a list of elements that can be compared (numbers).
        Sorts L in ascending order.'''
    for i in range(len(L)-1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal>L[j]:
                minIndx = j
                minVal = L[j]
            j+=1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp
        if i < len(L)-2: print 'Partially sorted list = ', L
        else: print 'final = ', L
                
        
