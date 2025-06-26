def priority_scheduling(processes):
    processes.sort(key=lambda x: (x[1], x[3]))  # Sort by arrival time, then priority
    completion_time, waiting_time, turnaround_time = [], [], []
    current_time = 0
    executed = []
    for pid, arrival, burst, priority in processes:
        current_time = max(current_time, arrival) + burst
        completion_time.append(current_time)
        turnaround_time.append(current_time - arrival)
        waiting_time.append(turnaround_time[-1] - burst)
        executed.append((pid, arrival, burst, priority))
        return completion_time, waiting_time, turnaround_time, executed