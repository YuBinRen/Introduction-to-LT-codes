from random import choices
import numpy as np
def get_degrees_from(distribution_name, N, k):
    if distribution_name == "ideal":
        probabilities = ideal_distribution(N)
    elif distribution_name == "robust":
        probabilities = robust_distribution(N)
    else:
        probabilities = None
    population = list(range(0, N+1))
    return [1] + choices(population, probabilities, k=k-1)
def encode(blocks, drops_quantity):
    blocks_n = len(blocks)
    assert blocks_n <= drops_quantity, "Because of the unicity in the random neighbors, it is need to drop at least the same amount of blocks"
    random_degrees = get_degrees_from("ideal", blocks_n, k=drops_quantity)
    for i in range(drops_quantity):
    
        selection_indexes, deg = generate_indexes(i, random_degrees[i], blocks_n)
    
        drop = blocks[selection_indexes[0]]
    
        for n in range(1, deg):
            drop = np.bitwise_xor(drop, blocks[selection_indexes[n]])
            # drop = drop ^ blocks[selection_indexes[n]] # according to my tests, this has the same performance
        # Create symbol, then log the process
        symbol = Symbol(index=i, degree=deg, data=drop)
        
        yield symbol