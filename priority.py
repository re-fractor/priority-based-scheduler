from typing import List, NamedTuple

class Proc(NamedTuple):
    proc_id : int
    arrival_time : int
    burst_time : int
    priority : int

class CompletedProc(NamedTuple):
    proc_id: int
    completion_time: int
    priority : int

n = int(input("Enter total number of processes:"))
procs: List[Proc] = []
for i in range(n):
    a = "Arrival time of p" + str(i+1) + ":"
    b = "Burst time of p" + str(i+1) + ":"
    p = "Priority of p" +str(i+1)+ ":"
    procs.append(Proc(i+1, int(input(a)), int(input(b)),int(input(p))))
#for proc in procs:
 #   print("\t", proc)

completed_procs: List[CompletedProc] = []
etime = 0
for i in range(n):
    ready : List[Proc] = []
    for proc in procs:
        if proc.arrival_time<=etime:
                ready.append(proc)

    ready.sort(key= lambda x: (x.priority))
    processing_proc = ready[0]
    #print(processing_proc)
    if processing_proc.arrival_time<=etime: 
        etime = etime + processing_proc.burst_time
    else:
        etime  = processing_proc.arrival_time
    
    completed_procs.append(CompletedProc(processing_proc.proc_id,etime,processing_proc.priority))
    procs.remove(processing_proc)

for proc in completed_procs:
    print("\t", proc)