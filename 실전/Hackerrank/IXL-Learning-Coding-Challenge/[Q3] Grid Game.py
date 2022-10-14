# # Grid Game

# Julia is playing a game on an infinite two-dimensional grid, where the bottom left cell is referenced as (1,1) and each cell contains an initial value of 0. The game consists of *n* steps; during each step:

# 1. Julia has two integers *r* and *c*.
# 2. Julia increments the value in every *(i, j)* cell satisfying 1 <= i <= r and 1 <= j <= c by 1.

# After performing *n* such steps, Julia finds the maximum value, *x*, in any cell on the board, and counts the number of occurrences of *x*.

# Complete the function in the editor below. It has the following parameter:

# | Name | Type | Description |
# | ---- | ---- | ----------- |
# | steps | string array | Each index contains a string of two-space separated integers describing the respective values of *r* and *c* for each step. |

# The function must return a long integer denoting the total number of ocurrences of the greatest integer *x* in the grid after *n* steps.

# # Input format 
# The first line contains an integer, *n*, denoting the number of elements in steps. Each of the subsequent lines contains a string of two space-separated integers describing an index in steps.

# # Constraints

# * 1 <= n <= 100
# * 1 <= r, c <= 10^6

# # Output format 

# Return a long integer denoting the total number of occurrences of the greatest integer *x* in the grid after *n* steps.




def function(steps, n):
    """
    The trick here is to realize that the cells with the highest value are those
    that are incremented the most amount of times -- but, since the lower bounds
    start at (0, 0), note that there is at least one cell being incremented at every
    step. This then means that the cell that is incremented every time is the one
    that has the highest value; to find these cells, we take the union across all
    the rows/columns that are incremented at each time, the union will tell us which
    row/column got incremented each time, and thus which is the maximum value.
    """
    row_sets = []
    col_sets = []
    for step in steps:
        row_bound, col_bound = map(int, step.split(' '))
        row_range = list(range(0, row_bound))
        col_range = list(range(0, col_bound))

        row_sets.append(set(row_range))
        col_sets.append(set(col_range))

    row_intersection = set.intersection(*row_sets)
    col_intersection = set.intersection(*col_sets)

    cells = len(row_intersection) * len(col_intersection)

    return cells