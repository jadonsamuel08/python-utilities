from simulation import run_simulation
from stats import calculate_probability, longest_streak
from visualization import plot_results

def main():
    n = int(input("How many flips? "))

    results, flips = run_simulation(n)

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