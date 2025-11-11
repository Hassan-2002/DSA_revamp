def isPowerOfTwo(n: int) -> bool:
        numb = n & (n-1)
        if n and not numb:
            return True
        return False
n = int(input())
print(isPowerOfTwo(n))         
        