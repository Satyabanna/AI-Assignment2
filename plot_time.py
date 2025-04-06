import matplotlib.pyplot as plt
import pandas as pd

# Load the data
sa_data = pd.read_csv("sa_convergence.csv")
hc_data = pd.read_csv("hc_convergence.csv")

# Calculate average time to convergence
sa_avg_time = sa_data["TimeToConvergence"].mean()
hc_avg_time = hc_data["TimeToConvergence"].mean()

# Plot
algorithms = ['Simulated Annealing', 'Hill Climbing']
avg_times = [sa_avg_time, hc_avg_time]

plt.figure(figsize=(8, 5))
bars = plt.bar(algorithms, avg_times, color=['skyblue', 'salmon'])

# Add value labels on top
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, f"{yval:.2f}s", ha='center', va='bottom')

plt.title("Average Time to Reach Optimum")
plt.ylabel("Time (seconds)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
