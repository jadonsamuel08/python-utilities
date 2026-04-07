from simulation import run_simulation
from stats import calculate_probability, longest_streak
from visualization import plot_results

def main():
    n = int(input("How many flips? "))

    if n == -1: exit()

    if n <= 0:
        print("Please enter a positive number of flips.")
        return

    weight_raw = input("Heads weight 0-1 (press Enter for 0.5): ").strip()

    try:
        heads_weight = float(weight_raw) if weight_raw else 0.5
    except ValueError:
        print("Heads weight must be a number between 0 and 1.")
        return

    if not 0 <= heads_weight <= 1:
        print("Heads weight must be between 0 and 1.")
        return

    results, flips = run_simulation(n, heads_weight)

    probabilities = calculate_probability(results)
    streak = longest_streak(flips)

    print("\nResults:")
    print(results)

    print("\nProbabilities:")
    for k, v in probabilities.items():
        print(f"{k}: {v:.2%}")

    print(f"\nLongest streak: {streak}")

    plot_results(results)

if __name__ == "__main__":
    main()