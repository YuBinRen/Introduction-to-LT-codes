def decode(symbols, blocks_quantity):
    symbols_n = len(symbols)
    assert symbols_n > 0, "There are no symbols to decode."
    blocks_n = blocks_quantity
    blocks = [None] * blocks_n
    symbols = recover_graph(symbols, blocks_n)
    
    solved_blocks_count = 0
    iteration_solved_count = 0
    start_time = time.time()
    
    while iteration_solved_count > 0 or solved_blocks_count == 0:
    
        iteration_solved_count = 0
        for i, symbol in enumerate(symbols):
            if symbol.degree == 1: 
                iteration_solved_count += 1 
                block_index = next(iter(symbol.neighbors)) 
                symbols.pop(i)
                if blocks[block_index] is not None:
                    continue
                blocks[block_index] = symbol.data
                solved_blocks_count += 1
                reduce_neighbors(block_index, blocks, symbols)
    return np.asarray(blocks), solved_blocks_count
def reduce_neighbors(block_index, blocks, symbols):  
    for other_symbol in symbols:
        if other_symbol.degree > 1 and block_index in other_symbol.neighbors:

            other_symbol.data = np.bitwise_xor(blocks[block_index], other_symbol.data)
            other_symbol.neighbors.remove(block_index)
            other_symbol.degree -= 1
