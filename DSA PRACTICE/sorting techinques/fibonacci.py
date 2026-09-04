
#factorial  sequence   using   iterative approach:
"""principle  of  factorial :
1!=1
2!=1x2
3!=1x2x3""" 
# def factorial_iterative(num):
#     if num<0:
#         return "error factorial of a negative  number does'nt exists "
#     if  num==0 or num==1:
#         return 1
#     fact=1
#     for i  in range(2,num+1):
#         fact=fact*i
#     return  f"factorial of {num}:{fact},count:{num}"

def factorial_recursive(num):
    if num<0:
        return "error factorial of a negative  number does'nt exists "
    if  num==0 or num==1:
        return 1
    
    fact=num*factorial_recursive(num-1)
    return f"factorial of {num}:{fact}"


  

print(factorial_recursive(3))

#  fibonacci  sequence