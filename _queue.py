from rich.console import Console

# import process features & functions
import _process

console = Console()

# quantum seconds
quantum = {
    "queue": 20, # time period per queue (seconds)
    "rr": 5, # round robin process time period (seconds)
    "fcfs": 20, # fcfs process time period (seconds)
    "sjf": 20, # sjf process time period (seconds)
}
# current queue
queue_no = 0

# queues
queue_0 = []
queue_1 = []
queue_2 = []
queue_3 = []

# initiate the queues
def init(pool):
    global queue_no, queue_0, queue_1, queue_2, queue_3, quantum

    for p in pool:
        # if queue priority is 0 set to queue 0
        if(p.queue == 0):
            queue_0.append(p)
        # if queue priority is 1 set to queue 1
        elif(p.queue == 1):
            queue_1.append(p)
        # if queue priority is 2 set to queue 2
        elif(p.queue == 2):
            queue_2.append(p)
        # if queue priority is 3 set to queue 3
        elif(p.queue == 3):
            queue_3.append(p)
        else:
            print(f"%s process is not allocated to any queue", str(p.id))

    # initiate queue processing
    while (
        len(queue_0) > 0 or
        len(queue_1) > 0 or
        len(queue_2) > 0 or
        len(queue_3) > 0
    ):
        if(queue_no == 0 and len(queue_0) > 0):
            rr(queue_0)
        elif(queue_no == 1 and len(queue_1) > 0):
            sjf(queue_1)
        elif(queue_no == 2 and len(queue_2) > 0):
            sjf(queue_2)
        elif(queue_no == 3 and len(queue_3) > 0):
            fcfs(queue_3)
        
        # reset queue quantum
        quantum["queue"]= 20
        # switch to next queue
        queue_no = (queue_no + 1) % 4
       
# round robin schedular
def rr(queue):
    execute(queue, "rr")

# shortest job first schedular
def sjf(queue):
    # sort list by `burst` in the natural order
    queue.sort(key=lambda x: x.burst)  
    execute(queue, "sjf")

# first come fist server schedular
def fcfs(queue):
    execute(queue, "fcfs")
    
# execute the scheduler process
def execute(queue, scheduler):
    while len(queue) > 0 and quantum["queue"] > 0:    
        p = queue[0]
        _time = cal_time(quantum[scheduler], p)

        completed = _process.run(_time, p)
        end(p, _time, queue, completed)

# wrap the end of process
def end(p, _time, queue, completed):
    global quantum, queue_no

    # display the process status
    # _process.display(p, _time, queue_no)
    
    # if the current process is not completed in round robin 
    # pop from top and add it to the back of the queue 
    if(queue_no == 0):
        if(completed == 0):
            queue.append(p)
        
        queue.pop(0)

     # remove the completed process
    elif(completed):
        queue.pop(0)
    
    # reduce the queue time
    quantum["queue"] -= _time

# calculate time
def cal_time(_time, p):
    global quantum

    if(p.burst < _time):
        _time = p.burst
        
    if(_time > quantum["queue"]):
        _time = quantum["queue"]

    return _time