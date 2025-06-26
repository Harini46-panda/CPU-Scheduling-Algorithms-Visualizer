import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def visualize_gantt_chart(processes, completion_time):
    fig, ax = plt.subplots(figsize=(12, 4))  # Increased figure size for better spacing
    start_time = 0

    for i, (pid, arrival, burst, *_) in enumerate(processes):
        end_time = completion_time[i]
        ax.barh(y=0, width=burst, left=start_time, height=0.5, label=f'P{pid+1}')
        ax.text(start_time + burst / 2, 0, f"P{pid+1}", ha='center', va='center', color='white', fontsize=10)
        start_time = end_time
    
    ax.set_yticks([])  # Remove y-axis labels
    ax.set_xticks(range(0, completion_time[-1] + 1, max(1, completion_time[-1] // 10)))  # Reduce x-axis labels
    ax.xaxis.set_major_locator(MaxNLocator(integer=True, prune='both'))  # Optimize tick positions
    ax.set_xlabel("Time")
    ax.set_title("CPU Scheduling - Gantt Chart")

    plt.xticks(rotation=45, ha='right', fontsize=8)  # Rotate labels and adjust size
    plt.tight_layout()  # Adjust layout to prevent cutoff
    plt.legend()
    plt.show()