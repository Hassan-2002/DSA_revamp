def myPow(x: float , n: int)-> float :
    if n<0:
        x=1/x
        n*=-1
    if n==1:
        return x
    if n==2:
        return x*x
    if n%2==0:
        return myPow(x,int(n/2)) * myPow(x , int(n/2))
    else:
        return myPow(x,int(n/2)+1) * myPow(x , int(n/2))

answer = myPow(2,-5)
print(answer)