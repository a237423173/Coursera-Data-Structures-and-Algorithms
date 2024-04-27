def lcm(a, b):
    for r in range(1, b + 1):
        if (a * r) % b == 0:
            return (a * r)



if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

