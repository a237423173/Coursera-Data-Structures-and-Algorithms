def max_pairwise_product(numbers):
    n = len(numbers)
    first_number = -1
    first_index = -1
    second_number = -1
    
    for i in range(n):
        if numbers[i] > first_number:
            first_number = numbers[i]
            first_index = i
    
    for j in range(n):
        if (j!=first_index) & (numbers[j] > second_number):
            second_number = numbers[j]
            
    
    
    max_product = first_number * second_number
    

    return max_product


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
