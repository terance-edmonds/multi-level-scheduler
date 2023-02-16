import _process
from rich.console import Console

console = Console()

# quantum seconds
quantum = {
    "queue": 20, # time period per queue (seconds)
    "round_robin": 5, # round robin process time period (seconds)
    "fcfs": 20, # fcfs process time period (seconds)
    "sjf": 20, # sjf process time period (seconds)
}
# current queue
queue_no = 1
display_title=False

# queues
queue_1 = []
queue_2 = []
queue_3 = []
queue_4 = []

# initiate the queues
def init(pool):
    global queue_no, queue_1, queue_2, queue_3, queue_4

    for p in pool:
        # if queue priority is 1 set to queue 1
        if(p.queue == 1):
            queue_1.append(p)
        # if queue priority is 2 set to queue 2
        elif(p.queue == 2):
            queue_2.append(p)
        # if queue priority is 3 set to queue 3
        elif(p.queue == 3):
            queue_3.append(p)
        # if queue priority is 4 set to queue 4
        elif(p.queue == 4):
            queue_4.append(p)
        else:
            print(f"%s process is not allocated to any queue", str(p.name))

    # log the started time
    console.log("[bold purple]================================")
    console.log("[bold purple]        Started Processing      ")
    console.log("[bold purple]================================")
    console.log("")

    # initiate queue processing
    while (
        len(queue_1) > 0 or
        len(queue_2) > 0 or
        len(queue_3) > 0 or
        len(queue_4) > 0
    ):
        if(queue_no == 1 and len(queue_1) > 0):
            rr(queue_1)
        elif(queue_no == 2 and len(queue_2) > 0):
            sjf(queue_2)
        elif(queue_no == 3 and len(queue_3) > 0):
            sjf(queue_3)
        elif(queue_no == 4 and len(queue_4) > 0):
            fcfs(queue_4)
        
        queue_no = queue_no % 4 + 1
    
    # log the started time
    console.log("")
    console.log("[bold purple]================================")
    console.log("[bold purple]       Finished Processing      ")
    console.log("[bold purple]================================")
       

# round robin schedular
def rr(queue):
    if(display_title): console.log(f"[bold yellow]Round Robin Schedular - (Queue {queue_no})\n")

    for i, p in enumerate(queue):
        _time = quantum["round_robin"]

        if(p.burst < _time):
            _time = p.burst

        state = _process.run(_time, p)

        wrap(p, _time, queue, state, i)

# shortest job first schedular
def sjf(queue):
    if(display_title): console.log(f"[bold yellow]Shortest Job First Schedular - (Queue {queue_no})\n")

    # sort list by `burst` in the natural order
    queue.sort(key=lambda x: x.burst)

    for i, p in enumerate(queue):    
        _time = quantum["sjf"]
        
        if(p.burst < _time):
            _time = p.burst

        state = _process.run(_time, p)

        wrap(p, _time, queue, state, i)

# first come fist server schedular
def fcfs(queue):
    if(display_title): console.log(f"[bold yellow]First Come First Serve Schedular - (Queue {queue_no})\n")

    for i, p in enumerate(queue):    
        _time = quantum["fcfs"]
        
        if(p.burst < _time):
            _time = p.burst

        state = _process.run(_time, p)

        wrap(p, _time, queue, state, i)

# wrap the end of queue process
def wrap(p, _time, queue, state, index):
    if(state): 
        p.burst -= _time

        if(p.burst == 0):
            # remove the process from queue
            queue.pop(index)
        
        console.log(f"{p.name} burst time (s): {_time}")
        # display the process status
        # _process.display(p, _time, queue_no)
    else:
        console.log(f"[red] something went wrong with {p.name} process")