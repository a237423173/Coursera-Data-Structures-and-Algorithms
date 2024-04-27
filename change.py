def change(money):
    # write your code here
    d1 = money // 1

    d5 = d1 // 5
    d1 = d1 - d5 * 5

    d10 = d5 // 2
    d5 = d5 - d10 * 2

    return (d1 + d5 + d10)


if __name__ == '__main__':
    m = int(input())
    print(change(m))
