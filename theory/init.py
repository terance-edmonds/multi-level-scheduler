import _process
import _queue
from rich.table import Table
from rich.console import Console

console = Console()

# number of processes
num_processes = 0
# a list of processes
pool = []

# test case pools
pool_1 = [
    _process.Process("P1.1", 4, 1),
    _process.Process("P1.2", 4, 1),
    _process.Process("P1.3", 4, 1),
    _process.Process("P1.4", 4, 1),
    _process.Process("P1.5", 4, 1),
    _process.Process("P1.6", 4, 1),
    _process.Process("P2.1", 5, 2),
    _process.Process("P2.2", 2, 2),
    _process.Process("P2.3", 2, 2),
    _process.Process("P2.4", 2, 2),
    _process.Process("P2.5", 2, 2),
    _process.Process("P3.1", 5, 3),
    _process.Process("P4.1", 10, 4),
]

pool_2 = [
    _process.Process("P1.1", 4, 1),
    _process.Process("P2.1", 5, 2),
    _process.Process("P3.1", 2, 2),
    _process.Process("P4.1", 5, 4),
]

# test with pool 2
# pool = pool_2

def summarize(pool, end=False):
    queue_names = {
        1: "round robin",
        2: "shortest job first",
        3: "shortest job first",
        4: "first come first serve",
    }

    table = Table(title="Processes Summary")

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

    summarize(pool, end=True)


# start the app
init()