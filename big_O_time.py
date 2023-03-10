"""
LEE HYUNHO, 201902927, Computer Enginnering and Science
"""
import time, random

def evaluate_n2(A,x):
    result = 0
    for i in range(0,n):
        temp = 1
        for j in range(0,i):
            temp *= x
        result += A[i]*temp

    return result

def evaluate_n(A,x):
    result = 0
    for i in range(0,n):
        if i == 0:
            temp = 0
        else:
            temp *= x
        result += A[i]*temp
    
    return result



random.seed()
for i in range(10):
    n = int(input('n= '))
    A = [random.randint(-999,999) for i in range(n)]
    x = random.randint(-99,99)

    before = time.process_time()
    evaluate_n2(A,x)
    after = time.process_time()
    print("evaluate_n2: ", after-before)

    before = time.process_time()
    evaluate_n(A,x)
    after = time.process_time()
    print("evaluate_n: ", after-before)

