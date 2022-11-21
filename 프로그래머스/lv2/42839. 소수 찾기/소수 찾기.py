from itertools import permutations
def is_prime_number(num):
    if num <2:
        return False
    
    for i in range(2,num):
        if num%i == 0:
            return False
    
    return True 

def solution(numbers): 
    numbers = list(numbers)
    array = []
    answer = []
    
    for i in range(1,len(numbers)+1):
        array = list(map(''.join,permutations(numbers,i)))
        for j in set(array):
            if  is_prime_number(int(j))==True:
                answer.append(int(j))

    return len(set(answer))