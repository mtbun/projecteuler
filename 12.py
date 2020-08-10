def tringular_n(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum

def diviors(num):
    list = []
    for i in range(1,num+1):
        if num % i == 0:
            list.append(i)
    
    return list

i = 0
while True:
    i += 1
    if len(diviors(tringular_n(i))) > 500:
        print (tringular_n(i))
        break
    