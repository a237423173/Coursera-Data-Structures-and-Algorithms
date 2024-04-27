def max_pairwise_product(numbers):
    
    sorted_numbers = sorted(numbers, reverse=True)
    max_product = sorted_numbers[0] * sorted_numbers[1]
    

    return max_product


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
