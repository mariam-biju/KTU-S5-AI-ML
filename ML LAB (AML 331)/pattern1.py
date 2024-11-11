import numpy as np
from collections import defaultdict

def find_repeating_patterns(arr):
    n = arr.shape[0]
    pattern_count = defaultdict(int)
   
    def extract_subpatterns(sequence, length):
        subpatterns = []
        for i in range(len(sequence) - length + 1):
            subpatterns.append(tuple(map(int, sequence[i:i + length])))  # Convert numpy ints to native ints
        return subpatterns
   
    # Check rows
    for row in arr:
        for length in range(2, n + 1):
            subpatterns = extract_subpatterns(row, length)
            for subpattern in subpatterns:
                pattern_count[subpattern] += 1
   
    # Check columns (transpose)
    for row in arr.T:
        for length in range(2, n + 1):
            subpatterns = extract_subpatterns(row, length)
            for subpattern in subpatterns:
                pattern_count[subpattern] += 1
               
    repeating_patterns = {k: v for k, v in pattern_count.items() if v > 1}
    return repeating_patterns

def get_matrix_from_user():
    n = int(input("Enter the dimensions: "))
    matrix = []
    print(f"Enter elements of {n}x{n} matrix row by row:")
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

if __name__ == "__main__":
    matrix = get_matrix_from_user()
    patterns = find_repeating_patterns(matrix)
    print("Repeating patterns:")
    for pattern, count in patterns.items():
        print(f"Pattern {pattern} appears {count} times")
