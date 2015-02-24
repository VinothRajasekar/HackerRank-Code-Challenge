#!/usr/bin/py
# Head ends here
def lonelyinteger(a):
    answer = 0
    for number in a:
        answer = answer ^ number
    return answer
# Tail starts here
if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))
