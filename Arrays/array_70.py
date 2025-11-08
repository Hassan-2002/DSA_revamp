#leetcode 70 easy array topics array, dp, memoization
#You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
def climbStairs(n :int)-> int:
    if n ==1:
        return 1
    first = 1
    second = 2
    for i in range(3,n+1):
        third = first + second 
        

val = climbStairs(3)
print(val)