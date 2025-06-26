def fcfs_scheduling(processes) :#each process is represented in the form of a tuple (pid,arrival_time,burst_time)
    processes.sort(key=lambda x:x[1])#x[1] refers to the arrival time of each processes and we are arranging them in the ascending order 
    #lambda arguments:expression, x->each process tuple and x[1] extracts the arrival time of each process
    n=len(processes)
    cptime,wtime,tatime=[0]*n,[0]*n,[0]*n#initializing the completion time,waiting time and turn around time of each process to 0
    starttime=processes[0][1]
    for i in range(n):
        pid,at,burst=processes[i]
        if(starttime<at):
            starttime=at
        cptime[i]=starttime+burst
        tatime[i]=cptime[i]-at
        wtime[i]=tatime[i]-burst
        starttime+=burst
    return cptime,wtime,tatime


