from collections import deque
def round_robin_scheduling(processes, quantum):
    queue = deque(processes)
    remaining_time = {p[0]: p[2] for p in processes}
    completion_time, waiting_time, turnaround_time = {}, {}, {}
    executed_order = []
    current_time = 0
    while queue:
        pid, arrival, burst = queue.popleft()
        if remaining_time[pid] > quantum:
            remaining_time[pid] -= quantum
            current_time += quantum
            queue.append((pid, arrival, burst))  # Requeue unfinished process
        else:
            current_time += remaining_time[pid]
            remaining_time[pid] = 0
            completion_time[pid] = current_time
            turnaround_time[pid] = completion_time[pid] - arrival
            waiting_time[pid] = turnaround_time[pid] - burst
        executed_order.append(pid)
    completion_time_list = [completion_time[i] for i in range(len(processes))]
    waiting_time_list = [waiting_time[i] for i in range(len(processes))]
    turnaround_time_list = [turnaround_time[i] for i in range(len(processes))]
    return completion_time_list, waiting_time_list, turnaround_time_list