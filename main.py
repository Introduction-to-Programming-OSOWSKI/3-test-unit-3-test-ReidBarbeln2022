def countB(a):
    count = 0
    for i in range(0, len(a)):
        
        if a[i] == "a":
            count = (count + 1)
    return count
print (countB("baseball"))

def removeLast(b):
    hi = ""
    for i in range(0, len(b) - 1):
        hi = hi + b[i]
       
    return hi
        
        
print (removeLast("winter"))



def sumBetweenOdd(c, d):
    total = 0
    
    for i in range (c , d):
        if c / d == c % d:
            total == total + i

    return total
print (sumBetweenOdd(5, 13))


def firstLast(e):
    if  e[len(e) - 1] == e[0]:
        return True

    else:
        return False
print (firstLast("roar"))