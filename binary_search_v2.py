def binary_search(keys, query):
    # write your code here
    left = 0
    right = len(keys)-1
    mid = (left+right) // 2
    
    while (right > (left+1)):
        if query == keys[mid]:
            return mid
        elif query > keys[mid]:
            left = mid + 1
            mid = (left+right) // 2
        else:
            right = mid - 1
            mid = (left+right) // 2
    
    if query == keys[left]:
        return left
    elif query == keys[right]:
        return right
    else:
        return -1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
