def initialize_state(block_size):
    return [[0] * block_size for _ in range(block_size)]

def has_nonzero_lane(state, block_size):
    for row in state:
        for value in row:
            if value != 0:
                return True
    return False

def simulate_sha3(block_size):
    state = initialize_state(block_size)
    capacity_size = block_size // 2
    round_count = 0

    while not has_nonzero_lane(state, capacity_size):
        # Set non-zero bits in a deterministic manner
        for i in range(capacity_size):
            state[i][round_count % block_size] = 1

        round_count += 1

    return round_count

def main():
    block_size = 1024
    rounds = simulate_sha3(block_size)
    print(f"Rounds needed: {rounds}")

if __name__ == "__main__":
    main()
