import math

def calculate_possible_keys(unique_positions):
    return math.factorial(unique_positions)

def calculate_effectively_unique_keys(total_keys, identical_keys):
    return total_keys // identical_keys

def main():
    total_positions = 25  # Total unique positions in the Playfair matrix
    total_letters = 26    # Total letters in the English alphabet
    identical_keys = 2    # Two keys may produce identical results due to the symmetry of the matrix

    possible_keys = calculate_possible_keys(total_positions)
    effectively_unique_keys = calculate_effectively_unique_keys(possible_keys, identical_keys)

    print("Possible keys without considering duplicate results:", possible_keys)
    print("Effectively unique keys considering duplicate results:", effectively_unique_keys)

if __name__ == "__main__":
    main()
