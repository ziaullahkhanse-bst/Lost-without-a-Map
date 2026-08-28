def maps(a):
    result = []  
    
    for num in a:
        result.append(num * 2)  
    
    return result


print(maps([1, 2, 3]))    
print(maps([4, 5, 6]))  
print(maps([-1, 0, 1]))   
