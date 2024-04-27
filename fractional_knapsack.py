from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    v_divide_w = []
    for i in range(len(weights)):
        v_divide_w.append(values[i]/weights[i])
    newlist = []
    for i in range(len(weights)):
        newlist.append((v_divide_w[i], values[i], weights[i]))
    
    newlist.sort(reverse=True)

    
    for i in range(len(weights)):
        d, v, w = newlist[i]
        if w > capacity:
            value = value + d * capacity
            capacity = 0
        else:
            value = value + d * w
            capacity = capacity - w



    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
