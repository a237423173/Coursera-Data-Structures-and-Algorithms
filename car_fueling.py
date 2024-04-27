from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here
    list(stops)
    stops.append(distance)
    refill = 0 
    now_run = stops[0]
    for i in range(len(stops)-1):
        if (stops[i+1] - stops[i] > tank) or (stops[0]> tank):
            return -1
  
        if (now_run + stops[i+1] - stops[i] > tank):
            refill = refill + 1
            now_run = stops[i+1] - stops[i]
        else:
            now_run = now_run + stops[i+1] - stops[i]
    
    return refill



if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
