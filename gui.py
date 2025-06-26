import tkinter as tk
from tkinter import messagebox
from fcfs import fcfs_scheduling
from sjf import sjf_scheduling
from round_robin import round_robin_scheduling
from priority import priority_scheduling
from srtf import srtf_scheduling
from visualiser import visualize_gantt_chart

# Create GUI Window
root = tk.Tk()
root.title("CPU Scheduling Algorithms")
root.configure(bg="#e6f7ff")  # Light blue background
root.geometry("700x500")  # Set window size

# Styling
button_style = {"bg": "#4682B4", "fg": "#FFD700", "font": ("Arial", 10, "bold"), "relief": "raised", "padx": 10, "pady": 5}
visual_button_style = {"bg": "#32CD32", "fg": "#000000", "font": ("Arial", 10, "bold"), "relief": "raised", "padx": 10, "pady": 5}  # Green background with black text
label_style = {"bg": "#e6f7ff", "font": ("Arial", 10)}

# Input for number of processes
tk.Label(root, text="Number of Processes:", **label_style).grid(row=0, column=0, padx=10, pady=5, sticky="w")
num_entry = tk.Entry(root, width=10)
num_entry.grid(row=0, column=1, padx=5, pady=5)

# Dropdown for algorithm selection
tk.Label(root, text="Select Algorithm:", **label_style).grid(row=0, column=2, padx=10, pady=5, sticky="w")
algorithm_var = tk.StringVar(root)
algorithm_var.set("FCFS")  # Default algorithm
algorithms = ["FCFS", "SJF", "Round Robin", "Priority"]
algo_menu = tk.OptionMenu(root, algorithm_var, *algorithms)
algo_menu.grid(row=0, column=3, padx=5, pady=5)

# Button to generate input fields
generate_btn = tk.Button(root, text="Generate Fields", command=lambda: generate_fields(), **button_style)
generate_btn.grid(row=0, column=4, padx=10, pady=5)

arrival_entries = []
burst_entries = []
priority_entries = []
quantum_entry = None
visualize_button = None
processes = []
cptime = []

# Function to run the selected scheduling algorithm
def run_scheduling():
    global processes, cptime
    try:
        num_processes = int(num_entry.get())
        selected_algo = algorithm_var.get()
        processes = []

        for i in range(num_processes):
            arrival = int(arrival_entries[i].get())
            burst = int(burst_entries[i].get())
            priority = int(priority_entries[i].get()) if selected_algo == "Priority" else None
            processes.append((i, arrival, burst, priority) if priority is not None else (i, arrival, burst))

        if selected_algo == "FCFS":
            cptime, wtime, tatime = fcfs_scheduling(processes)
        elif selected_algo == "SJF":
            cptime, wtime, tatime = sjf_scheduling(processes)
        elif selected_algo == "Round Robin":
            quantum = int(quantum_entry.get())
            cptime, wtime, tatime = round_robin_scheduling(processes, quantum)
        elif selected_algo == "Priority":
            cptime, wtime, tatime = priority_scheduling(processes)

        # Display results in table format
        result_text.set("{:<10} {:<10} {:<10} {:<12} {:<10} {:<10}\n".format(
            "Process", "Arrival", "Burst", "Completion", "Waiting", "Turnaround"))
        for i in range(num_processes):
            result_text.set(result_text.get() + "{:<10} {:<10} {:<10} {:<12} {:<10} {:<10}\n".format(
                f"P{i+1}", processes[i][1], processes[i][2], cptime[i], wtime[i], tatime[i]))

        if visualize_button:
            visualize_button.config(state=tk.NORMAL)

    except Exception as e:
        messagebox.showerror("Error ! Enter a valid input", str(e))

# Function to create input fields dynamically
def create_input_fields(n):
    global arrival_entries, burst_entries, priority_entries, quantum_entry, visualize_button
    selected_algo = algorithm_var.get()

    # Clear previous fields
    for widget in root.winfo_children()[5:]:
        widget.destroy()

    arrival_entries.clear()
    burst_entries.clear()
    priority_entries.clear()

    for i in range(n):
        tk.Label(root, text=f"P{i+1} Arrival:", **label_style).grid(row=i+1, column=0, padx=5, pady=2, sticky="w")
        arrival = tk.Entry(root, width=10)
        arrival.grid(row=i+1, column=1, padx=5, pady=2)
        arrival_entries.append(arrival)

        tk.Label(root, text=f"P{i+1} Burst:", **label_style).grid(row=i+1, column=2, padx=5, pady=2, sticky="w")
        burst = tk.Entry(root, width=10)
        burst.grid(row=i+1, column=3, padx=5, pady=2)
        burst_entries.append(burst)

        if selected_algo == "Priority":
            tk.Label(root, text=f"P{i+1} Priority:", **label_style).grid(row=i+1, column=4, padx=5, pady=2, sticky="w")
            priority = tk.Entry(root, width=10)
            priority.grid(row=i+1, column=5, padx=5, pady=2)
            priority_entries.append(priority)

    # Time Quantum for Round Robin
    if selected_algo == "Round Robin":
        tk.Label(root, text="Time Quantum:", **label_style).grid(row=n+1, column=0, padx=5, pady=5, sticky="w")
        quantum_entry = tk.Entry(root, width=10)
        quantum_entry.grid(row=n+1, column=1, padx=5, pady=5)

    # Run Button
    run_btn = tk.Button(root, text=f"Run {selected_algo}", command=run_scheduling, **button_style)
    run_btn.grid(row=n+2, column=0, columnspan=2, padx=10, pady=10)

    # Visualize Button
    visualize_button = tk.Button(root, text="Visualize", command=lambda: visualize_gantt_chart(processes, cptime),
                                 state=tk.DISABLED, **visual_button_style)
    visualize_button.grid(row=n+2, column=2, columnspan=2, padx=10, pady=10)

    # Results Label
    result_label = tk.Label(root, textvariable=result_text, **label_style, justify="left")
    result_label.grid(row=n+3, column=0, columnspan=6, padx=10, pady=10, sticky="w")

# Function to generate input fields
def generate_fields():
    try:
        n = int(num_entry.get())
        create_input_fields(n)
    except Exception as e:
        messagebox.showerror("Error ! Enter a valid input", str(e))

result_text = tk.StringVar()

root.mainloop()
