import random

def flip_coin(heads_weight=0.5):
    return "Heads" if random.random() < heads_weight else "Tails"

def run_simulation(n, heads_weight=0.5):
    results = {"Heads": 0, "Tails": 0}
    flips = []

    for _ in range(n):
        result = flip_coin(heads_weight)
        results[result] += 1
        flips.append(result)

    return results, flips