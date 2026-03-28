import matplotlib.pyplot as plt

def plot_results(results):
    labels = results.keys()
    values = results.values()

    plt.bar(labels, values)
    plt.title("Coin Flip Results")
    plt.xlabel("Outcome")
    plt.ylabel("Count")
    plt.show()