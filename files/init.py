from rich.table import Table
from rich.console import Console

# import process features & functions
import _process
# import queue features & functions
import _queue

console = Console()

# number of processes
num_processes = 0
# a list of processes
pool = []

def summarize(pool, end=False, title="Processes Summary"):
    queue_names = {
        0: "round robin",
        1: "shortest job first",
        2: "shortest job first",
        3: "first come first serve",
    }

    table = Table(title=title)

    table.add_column("PID", style="cyan", no_wrap=True, min_width=15)
    table.add_column("Burst time", justify="right", style="green", min_width=25)
    table.add_column("Queue", justify="right", style="green", min_width=25)
    if(end):
        table.add_column("Waiting time", justify="right", style="green", min_width=25)
        table.add_column("Turnaround time", justify="right", style="green", min_width=25)

    for p in pool:
        if(end):
            table.add_row(
                f"{p.id}", 
                f"{p.init_burst}s", 
                f"{queue_names[p.queue]}",
                f"{int((p.complete_time - p.arrival_time) - p.init_burst)}s",
                f"{int(p.complete_time - p.arrival_time)}s",
            )
        else:
            table.add_row(
                f"{p.id}", 
                f"{p.init_burst}s", 
                f"{queue_names[p.queue]}"
            )

    console.print(table, end="\n")

def init():
    # get the number of processes from the user
    global num_processes
    num_processes = int(input("Enter number of processes: "))
    print("")

    # create processes and store in the processes pool
    for i in range(num_processes):
        p = _process.create("P" + str(i))
        
        # store the created process in the pool
        pool.append(p)
   

    # display a summary of processes
    summarize(pool)
    # initiate queue scheduler
    _queue.init(pool)
    
    # arrange the pool in ascending of completion time
    pool.sort(key=lambda x: x.complete_time)
    #  display a summary of completed processes
    summarize(pool , end=True, title="Processes Completion Summary")


# start the app
init()