def intersection(arrays):
    length = len(arrays)
    cache = {}
    results = []
    
    # store elements in first array in cache
    for integer in arrays[0]:
        cache[integer] = 0
    
    # check if items in cache
    for array in arrays:
        for integer in array:
            if integer in cache:
                # increment count
                cache[integer] += 1
    
    for item in cache:
        if cache[item] == length:
            results.append(item)
             
    return results


# def intersection(arrays):s
#     length = len(arrays)
#     cache = {}
#     results = []
    
#     for integer in arrays[0]:
#         count = 0
#         for array in arrays:
#             if integer in array: 
#                 count += 1
#                 if count == length:
#                     results.append(integer)
#                     cache[length] = results
                
#     return cache[length]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

    # arrays = [
    # [1,2,3,4],
    # [1,2,5,6],
    # [1,2,7,8]
    # ]
    # print(intersection(arrays))