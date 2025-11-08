import sys


def selectSort(numss:list)-> list:
    i=0
    idx = 0
    
    while i<len(numss):
        smallest = sys.maxsize
        for j in range(i,len(numss)):
            
            print("for loop running")
            if numss[j]<smallest:
                smallest = numss[j]
                idx = j
        print(numss[i] , numss[idx])
        numss[idx],numss[i] = numss[i],numss[idx]
        i+=1
    return numss




numbers = [4,2,1,8,5,3,0]
print(selectSort(numbers))