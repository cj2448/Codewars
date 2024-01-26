def queue_time(customers, n):
    if not customers:
        return 0
    
    if len(customers) <= n:
        return max(customers)
    
    newlist = []
    total = 0
    next_index = n
    
    for x in range(n):
        newlist.append(customers[x])
        
    while next_index <= len(customers):
        smallest = min(newlist)
        total += smallest
        
        for index in range(len(newlist)):
            newlist[index] -= smallest
            
        for index in range(len(newlist)):
            if newlist[index] == 0 and next_index < len(customers):
                newlist[index] = customers[next_index]
                next_index += 1
            
            elif next_index >= len(customers):
                total += max(newlist)
                return total
    
    return