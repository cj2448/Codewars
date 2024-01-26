def find_uniq(arr):
    count = {}
    for num in arr:
        count[num] = 1 if num not in count else count[num] + 1
        
    for item in arr:
        if count[item] == 1:
            return item
    
    
    #return [num for num in arr if arr.count(num) == 1][0]