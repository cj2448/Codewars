def high(x):
    mydict = {}
    
    for word in x.split():
        total = 0
        for letter in word:
            total += ord(letter) - ord('`')
        
        mydict[word] = total
        
    return max(mydict, key = mydict.get)