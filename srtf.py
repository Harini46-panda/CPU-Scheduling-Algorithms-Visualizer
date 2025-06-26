def srtf_scheduling(processes):
    remtime={p[0]:p[2] for p in processes}
    comptime={}
    wtime={}
    tatime={}
    currtime=0
    comp=0
    execorder=[]
    while(comp<len(processes)):
        avail=[p for p in processes if p[1]<=currtime and remtime[p[0]]>0]
        if not avail:
            currtime+=1
            continue
        short=min(avail,key=lambda x:remtime[x[0]])
        pid=short[0]
        remtime[pid]-=1
        execorder.append(pid)
        if remtime[pid]==0:
            comp+=1
            comptime[pid]=currtime+1
            tatime[pid]=comptime[pid]-short[1]
            wtime[pid]=tatime[pid]-short[2]
        currtime+=1  
    completion_time_list = [comptime[i] for i in range(len(processes))]
    waiting_time_list = [wtime[i] for i in range(len(processes))]
    turnaround_time_list = [tatime[i] for i in range(len(processes))]
    return completion_time_list, waiting_time_list, turnaround_time_list