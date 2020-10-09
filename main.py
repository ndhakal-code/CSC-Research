MEM_SIZE = 1024

def run_memory_compaction(mem_layout):
    temp_layout = []
    curr_memory = 1023
    for i in range(len(mem_layout) - 1, -1, -1):
        mem = mem_layout[i][1] - mem_layout[i][0]
        temp_layout.append((curr_memory - mem, curr_memory))
        curr_memory = curr_memory - mem - 1
    temp_layout = temp_layout[::-1]
    return temp_layout


# runs the first fit algorithm

def run_first_fit(new_proc_size, mem_layout):
    if mem_layout[0][0] >= new_proc_size:
        mem_layout.insert(0, (mem_layout[0][0] - new_proc_size, mem_layout[0][0] - 1))
        return mem_layout
    for i in range(len(mem_layout) - 1):
        if mem_layout[i + 1][0] - mem_layout[i][1] >= new_proc_size:
            mem_layout.insert(i + 1, (mem_layout[i + 1][0] - new_proc_size, mem_layout[i + 1][0] - 1))
            return mem_layout
    mem_layout.append((MEM_SIZE - new_proc_size, MEM_SIZE - 1))
    return mem_layout


# runs the best fit algorithm

def run_best_fit(new_proc_size, mem_layout):
    min = MEM_SIZE
    index = -1
    if mem_layout[0][0] >= new_proc_size:
        min = mem_layout[0][0] - new_proc_size
        index = 0

    for i in range(len(mem_layout) - 1):
        space = mem_layout[i + 1][0] - mem_layout[i][1]
        if space - new_proc_size >= 0 and space - new_proc_size < min:
            min = space - new_proc_size
            index = i
    if index == -1:
        mem_layout.append((MEM_SIZE - new_proc_size, MEM_SIZE - 1))
        return mem_layout
    mem_layout.insert(index + 1, (mem_layout[index + 1][0] - new_proc_size, mem_layout[index + 1][0] - 1))
    return mem_layout


def test_all_funcs(psize, mlay):
    print('\n' + (90 * '*'))
    print('New process of size', psize)

    print('Original memory layout:', mlay)

    print('Compacted memory:', run_memory_compaction(mlay[:]))

    print('Memory after first fit:', run_first_fit(psize, mlay[:]))

    print('Memory after best fit:', run_best_fit(psize, mlay[:]))

    print((90 * '*') + '\n')

mlay1 = [(40, 120), (140, 150)]

psize1 = 10

test_all_funcs(psize1, mlay1)

mlay2 = [(0, 10), (30, 100), (130, 332), (400, 450)]

psize2 = 25

test_all_funcs(psize2, mlay2)

mlay3 = [(0, 10), (30, 100), (130, 332), (400, 450)]

psize3 = 400

test_all_funcs(psize3, mlay3)
