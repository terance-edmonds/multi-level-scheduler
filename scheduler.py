import _process
import _queue
from rich.table import Table
from rich.console import Console

console = Console()

# number of processes
num_processes = 0
# a list of processes
pool = []

def summarize(pool):
    queue_names = {
        1: "round robin",
        2: "shortest job first",
        3: "shortest job first",
        4: "first come first serve",
    }

    table = Table(title="Processes Summery")

    table.add_column("Name", style="cyan", no_wrap=True, min_width=15)
    table.add_column("Burst time", justify="right", style="green", min_width=25)
    table.add_column("Queue", justify="right", style="green", min_width=25)

    for p in pool:
        table.add_row(f"{p.name}", f"{p.burst}", f"{queue_names[p.queue]}")

    console.print(table, end="\n")

def init():
    # get the number of processes from the user
    global num_processes
    num_processes = int(input("Enter number of processes: "))

    # create processes and store in the processes pool
    for i in range(num_processes):
        p = _process.create("P" + str(i))
        
        # store the created process in the pool
        pool.append(p)

    # display a summery of processes
    summarize(pool)
    # initiate queue scheduler
    _queue.init(pool)


# start the app
init()