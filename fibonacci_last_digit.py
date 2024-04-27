def fibonacci_last_digit(n):
    if n <= 1:
        return n
    
    now, pre = (1, 0)

    for i in range(n-1):
        now, pre = ((now+pre) % 10, now % 10)
    
    return now


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
