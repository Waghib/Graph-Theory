def is_graphical_havel_hakimi(degree_sequence):
    """Recursively determines if a degree sequence is graphical using the Havel-Hakimi algorithm.

    Args:
        degree_sequence: A list of integers representing the degrees of vertices.

    Returns:
        True if the degree sequence is graphical, False otherwise.
    """
    print(degree_sequence, "--sort-> ", end="")
    degree_sequence.sort(reverse=True)  # Sort in descending order
    print(degree_sequence)

    if degree_sequence[0] == 0:  # Base case: All degrees are 0
        return True

    d = degree_sequence.pop(0)  # Extract the highest degree 'd'

    if d > len(degree_sequence):  # Not enough vertices to satisfy 'd' connections
        return False

    # Reduce the degrees of the next 'd' vertices
    print(degree_sequence, "--alg--> ", end="")
    for i in range(d):
        degree_sequence[i] -= 1
        if degree_sequence[i] < 0:
            return False
        
    print(degree_sequence)
        

    # Recursive call with the modified degree sequence
    return is_graphical_havel_hakimi(degree_sequence)


# Test Cases
global degree_sequence1
global degree_sequence2 
degree_sequence1 = [6, 5, 5, 4, 3, 3, 2, 2, 2, 2]
degree_sequence2 = [7, 6, 4, 4, 4, 3, 2, 1]

if is_graphical_havel_hakimi(degree_sequence1.copy()):
    print("Degree sequence 1 is graphical")
else:
    print("Degree sequence 1 is not graphical")

print("\n\n")

if is_graphical_havel_hakimi(degree_sequence2.copy()):
    print("Degree sequence 2 is graphical")
else:
    print("\nDegree sequence 2 is not graphical")
