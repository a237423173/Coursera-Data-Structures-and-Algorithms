def gcd(a, b):
    if a>b:
        while (a!=0 and b!=0):
            try:
                a = a % b
                b = b % a
            except:
                if a==0:
                    return b
                else:
                    return a
        if a==0:
            return b
        else:
            return a
    else:
        while (a!=0 and b!=0):
            try:
                b = b % a
                a = a % b            
            except:
                if a==0:
                    return b
                else:
                    return a
        if a==0:
            return b
        else:
            return a

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))


