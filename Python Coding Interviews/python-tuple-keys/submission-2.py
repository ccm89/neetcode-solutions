from typing import List, Set, Tuple


def grid_to_set(grid: List[List[int]]) -> Set[Tuple[int, int]]:
    # Bruteforce approach:
    # res = set()
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if grid[i][j] == 1:
    #             res.add((i,j))
    # return res

    # Using enumerate:
    res = set()
    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            if column == 1:
                res.add((i,j))
    return res

    # Using enumerate and comprehension:
    {(i,j) for i, sublist in enumerate(grid) for j, value in enumerate(sublist) if value}

# do not modify below this line

output1 = grid_to_set([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
print(type(output1))
print(sorted(list(output1)))
      
output2 = grid_to_set([[1, 0, 0], [0, 0, 0]])
print(type(output2))
print(sorted(list(output2)))

output3 = grid_to_set([[1, 1, 1], [1, 1, 1]])
print(type(output3))
print(sorted(list(output3)))

output4 = grid_to_set([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print(type(output4))
print(sorted(list(output4)))
