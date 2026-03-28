def calculate_probability(results):
    total = sum(results.values())
    return {k: v / total for k, v in results.items()}

def longest_streak(flips):
    max_streak = 1
    current_streak = 1

    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 1

    return max_streak