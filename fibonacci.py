def fibonacci_number(n):
    
    if n <= 1:
        answer = n
    else:
        f_list = []
        f_list.append(0)
        f_list.append(1)
        for i in range(2, n+1):
            f_list.append(f_list[i-1] + f_list[i-2])
        answer = f_list[n]
    return answer

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
