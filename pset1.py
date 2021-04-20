#python3

def sum_multiples(limit):
    elements = []
    for i in range(0,limit):
        if i % 3 == 0:
            elements.append(i)
            continue
        if i % 5 == 0:
            elements.append(i)
    
    sum = 0
    for i in elements:
        sum += i

    return sum


print(sum_multiples(1000))
