import random

def flip_coin():
    return random.choice(["Heads", "Tails"])

def run_simulation(n):
    results = {"Heads": 0, "Tails": 0}
    flips = []

    for _ in range(n):
        result = flip_coin()
        results[result] += 1
        flips.append(result)

    return results, flips