def to_weird_case(string):
    nstring = ""
    for word in string.split():
        for x in range(len(word)):
            nstring += word[x].upper() if x % 2 == 0 else word[x].lower()
        
        nstring += " "
    
    return nstring.strip()