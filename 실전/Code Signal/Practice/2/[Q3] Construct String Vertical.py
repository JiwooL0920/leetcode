# You are given an array of strings arr. Your task is to construct a string from the words in arr, starting with the 0th character from each word (in the order they appear in arr), followed by the 1st character, then the 2nd character, etc. If one of the words doesn't have an ith character, skip that word.

# Return the resulting string.

# Example

# For arr = ["Daisy", "Rose", "Hyacinth", "Poppy"], the output should be solution(arr) = "DRHPaoyoisapsecpyiynth".

# First, we append all 0th characters and obtain string "DRHP";
# Then we append all 1st characters and obtain string "DRHPaoyo";
# Then we append all 2nd characters and obtain string "DRHPaoyoisap";
# Then we append all 3rd characters and obtain string "DRHPaoyoisapsecp";
# Then we append all 4th characters and obtain string "DRHPaoyoisapsecpyiy";
# Finally, only letters in the arr[2] are left, so we append the rest characters and get "DRHPaoyoisapsecpyiynth";

def solution(arr):
    # Find length of longest string
    longestLength = 0
    for n in arr:
        longestLength = max(longestLength, len(n))
    
    # construct empty matrix
    matrix = [[False]*longestLength for _ in range(len(arr))]
    ROWS, COLS = len(matrix), len(matrix[0])
    
    for r in range(ROWS):
        for c in range(COLS):
            if c > len(arr[r])-1:
                continue
            matrix[r][c] = arr[r][c]
    
    # go by column and construct string
    s = ""
    for c in range(COLS):
        for r in range(ROWS):
            char = matrix[r][c]
            if char != False:
                s += char
    return s
            
