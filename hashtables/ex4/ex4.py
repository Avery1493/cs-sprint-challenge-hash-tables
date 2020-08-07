def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # store positives in cache
    cache = {}
    result = []
    for integer in a:
        # 0 has no negative 
        if integer == abs(integer) and integer != 0:
            # key: -
            # value: +
            cache[-integer] = integer

    # if negative in list 
    for integer in a:
        if integer in cache:
            result.append(cache[integer])
            
    # return cache
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
