def distributeCandies(candyType):
    max_types = len(set(candyType))  
    max_eaten = len(candyType) // 2  

    return min(max_types, max_eaten)


candyType = [1, 1, 2, 2, 3, 3]
result = distributeCandies(candyType)
print(result)
