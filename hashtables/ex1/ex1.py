def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # store in hashtable (key:weight,value:index)
    cache = {}
    index = 0
    for weight in weights:
        cache[weight] = index
        index += 1
    
    # check cache for limit - weight
    for weight in weights:
        if limit - weight in cache:
            max_w = max(weight, limit - weight)
            min_w = min(weight, limit - weight)
            return [cache[max_w], cache[min_w]]
    

    return None

if __name__ == "__main__":
    weights = [12, 6, 7, 14, 19, 3, 0, 25, 40]
    length = 1
    limit = 7

    print(get_indices_of_item_weights(weights, length, limit))