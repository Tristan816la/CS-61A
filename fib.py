def fb(n):
    pre, cur = 0 , 1
    index = 1
    while index < n:
        temp = pre
        pre = cur
        cur = cur + temp
        index +=1
    return cur
print (fb(5))
