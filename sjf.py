def sjf_scheduling(processes):
    processes.sort(key=lambda x:(x[1],x[2]))#sort the processes based on arrival time and burst time
    comptime,wtime,tatime=[],[],[]
    currtime=0
    remprocess=processes[:]
    while(remprocess):
        avail=[p for p in remprocess if p[1]<=currtime]
        if not avail:
            currtime+=1
            continue
        short=min(avail,key=lambda x:x[2])
        remprocess.remove(short)
        pid,at,bt=short
        comptime.append(currtime+bt)
        tatime.append(comptime[-1]-at)
        wtime.append(tatime[-1]-bt)
        currtime+=bt
    return comptime,wtime,tatime