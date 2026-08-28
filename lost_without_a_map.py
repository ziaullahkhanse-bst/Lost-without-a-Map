def maps(a):
    result = []  # Empty list to store doubled numbers
    
    for num in a:
        result.append(num * 2)  
    
    return result

# Test
print(maps([1, 2, 3]))    # [2, 4, 6]
print(maps([4, 5, 6]))    # [8, 10, 12]
print(maps([-1, 0, 1]))   # [-2, 0, 2]
