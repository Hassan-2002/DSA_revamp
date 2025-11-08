# Given two integers n and i, return true if the ith bit in the binary 
# representation of n (counting from the least significant bit, 0-indexed) is set (i.e., equal to 1). 
# Otherwise, return false.


def ithBit(num : int, i : int):
    if((num >> i) & 1 == 0):
        return False
    return True
print(ithBit(13,1))
