def fibo(n, answer = 0):
    if n==2 or n==1:
        answer += 1
        return answer
    else:
        return fibo(n-2) + fibo(n-1)
    
print(fibo(6))